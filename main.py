from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn
import sqlite3


conn = sqlite3.connect('cars.db')
c = conn.cursor()

app = FastAPI(title="REST API using electric cars")

#@app.get('/')
#def home(request: Request):
#  return templates.TemplateResponse("/home.html", {
#      "request": request
#  })

@app.get("/annonces")
async def annonce_id ():
    annonce = {}
    c.execute("SELECT * FROM newfile1;")
    annonce = c.fetchall()
    conn.commit()
    return annonce

@app.get('/year/{car_year}')
async def car_year (car_year):
  year = {}
  c.execute("SELECT * FROM newfile2 WHERE FirstRegistration = ?;", (car_year,))
  year = c.fetchall()
  conn.commit()
  return year

@app.get('/kms/{car_kms}')
async def car_kms (car_kms):
  kms = {}
  c.execute('SELECT * FROM newfile1 WHERE "Kilometrage(km)"<= ?;', (car_kms,))
  kms = c.fetchall()
  conn.commit()
  return kms