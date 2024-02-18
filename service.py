import twstock
twstock.__update_codes()
import pandas as pd
import mplfinance as mpf
import os
import requests
from bs4 import BeautifulSoup
#%%查詢股票號
def stockNum(num):
    now =[]
    stockdict = {}
    stockName = num
    nowstock = twstock.realtime.get(stockName)
    stockdict['code'] = nowstock['info']['code']
    stockdict['name'] = nowstock['info']['name']
    stockdict['time'] = nowstock['info']['time']
    stockdict['highp'] = nowstock['realtime']['high']
    stockdict['lowp'] = nowstock['realtime']['low']
    stockdict['openp'] = nowstock['realtime']['open']
    stockdict['nowp'] = nowstock['realtime']['latest_trade_price']
    stockdict['teade'] = nowstock['realtime']['trade_volume']
    
    now.append(stockdict)
    
    
    return now

def buy_sell(num):   
    repoint = []
    stock = twstock.Stock(num)
    bfp = twstock.BestFourPoint(stock)    
    point = bfp.best_four_point() 
    if point[0] == True:
        repoint.append('可以買進')
    else:
        repoint.append('不可賣出')
    repoint.append(point[1])
    return repoint

def news():
    url = 'https://tw.stock.yahoo.com/tw-market/'

    data = requests.get(url).text
    soup = BeautifulSoup(data,'html.parser')

    soups = soup.find(id = 'YDC-Stream')
    div = soups.find_all('h3')
    news = []
    for row in div:
        try:
            newsdict = {}
            newsdict['title'] = row.find('a').text.strip()
            newsdict['url'] = row.find('a')['href']
            news.append(newsdict)
        except:
            continue    

    return news

