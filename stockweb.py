from flask import Flask,render_template,request
# from flask_paginate import Pagination
import db,service

app = Flask(__name__)

@app.route('/')
def index():    
    sql = "select stocknum,stockname,industry from lsn order by industry "         
    db.cursor.execute(sql)        
    result = db.cursor.fetchall()          
    return render_template('index.html',**locals())

@app.route('/stock')
def product():
    stocknum= request.args.get('stocknum','')    
    stockname = request.args.get('stockname','')
    
    if len(stocknum) == 0 and len(stockname) == 0 :
       now = service.stockNum('2330')
       point = service.buy_sell('2330')
    elif len(stocknum) > 0 and len(stockname) == 0 :
        now = service.stockNum(stocknum)
        point = service.buy_sell(stocknum)
    elif len(stocknum) == 0 and len(stockname) > 0 :
        sql = "select stocknum from lsn where stockname like '%{}%' ".format(stockname)
        db.cursor.execute(sql)        
        stocknum = db.cursor.fetchone()
        stocknum = stocknum[0]
        now = service.stockNum(stocknum)
        point = service.buy_sell(stocknum)
    
    
               
    return render_template('stock.html',**locals())

@app.route('/stock/<string:num>')
def stock(num):
    now = service.stockNum(num)
    point = service.buy_sell(num)
    news = service.news()
    return render_template('stock.html',**locals())










app.run()