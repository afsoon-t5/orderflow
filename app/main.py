from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import sqlite3
from datetime import datetime

app=FastAPI(title="OrderFlow API",version="1.0.0")
templates=Jinja2Templates(directory="templates")
DB="orderflow.db"
STATUSES=["جدید","در حال پردازش","ارسال شد","تکمیل شد","لغو شد"]

def conn():
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; return c

def init_db():
    c=conn()
    c.execute("""CREATE TABLE IF NOT EXISTS orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT, customer TEXT, phone TEXT,
    product TEXT, amount INTEGER, status TEXT, created_at TEXT)""")
    c.commit(); c.close()
init_db()

@app.get("/",response_class=HTMLResponse)
def dashboard(request:Request):
    c=conn()
    orders=c.execute("SELECT * FROM orders ORDER BY id DESC").fetchall()
    stats={
    "all":c.execute("SELECT COUNT(*) n FROM orders").fetchone()["n"],
    "new":c.execute("SELECT COUNT(*) n FROM orders WHERE status='جدید'").fetchone()["n"],
    "processing":c.execute("SELECT COUNT(*) n FROM orders WHERE status='در حال پردازش'").fetchone()["n"],
    "done":c.execute("SELECT COUNT(*) n FROM orders WHERE status='تکمیل شد'").fetchone()["n"],
    "revenue":c.execute("SELECT COALESCE(SUM(amount),0) n FROM orders WHERE status='تکمیل شد'").fetchone()["n"]}
    c.close()
    return templates.TemplateResponse("dashboard.html",{"request":request,"orders":orders,"stats":stats,"statuses":STATUSES})

@app.post("/orders")
def create_order(customer:str=Form(...),phone:str=Form(...),product:str=Form(...),amount:int=Form(...)):
    c=conn(); c.execute("INSERT INTO orders(customer,phone,product,amount,status,created_at) VALUES(?,?,?,?,?,?)",
    (customer,phone,product,amount,"جدید",datetime.now().isoformat(timespec="minutes")))
    c.commit(); c.close(); return RedirectResponse("/",status_code=303)

@app.post("/orders/{order_id}/status")
def update_status(order_id:int,status:str=Form(...)):
    if status in STATUSES:
        c=conn(); c.execute("UPDATE orders SET status=? WHERE id=?",(status,order_id)); c.commit(); c.close()
    return RedirectResponse("/",status_code=303)

@app.get("/api/orders")
def api_orders(status:str|None=None):
    c=conn()
    rows=c.execute("SELECT * FROM orders WHERE status=? ORDER BY id DESC",(status,)).fetchall() if status else c.execute("SELECT * FROM orders ORDER BY id DESC").fetchall()
    c.close(); return [dict(r) for r in rows]

@app.get("/health")
def health(): return {"status":"ok","service":"OrderFlow"}
