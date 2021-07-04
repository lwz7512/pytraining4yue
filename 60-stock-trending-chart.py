# stock market trending chart
# @2021/07/04
# 
# Knowledge Points:
# 1. API invoking
# 2. Chart Drawing
# 
# Reference:
# 
# Graph Plotting in Python | Set 1
# https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/?ref=leftbar-rightbar
# 
# Matplotlib:
# https://matplotlib.org/
# 
# seaborn: statistical data visualization¶
# https://seaborn.pydata.org/
# 
# Build Your Own Stock Charts with Yahoo Finance API and Python
# https://rapidapi.com/blog/yahoo-finance-api-python/
# 
# JSON FORMATOR
# https://jsonformatter.curiousconcept.com/#

# Preparations:
# 1. install matplotlib > pip3 install matplotlib
# 2. signin and subscribe Yahoo Finance test plan:
# https://rapidapi.com/apidojo/api/yahoo-finance1



# ============ STEP 1: test matplotlib ================
import matplotlib.pyplot as plt

plt.subplots(1, 1, figsize=(16, 4))

# # x axis values
# x = [1,2,3]
# # corresponding y axis values
# y = [2,4,1]

# # plotting the points
# plt.plot(x, y)

# # naming the x axis
# plt.xlabel('x - axis')
# # naming the y axis
# plt.ylabel('y - axis')

# # giving a title to my graph
# plt.title('My first graph!')

# # function to show the plot
# plt.show()

# ============ STEP 2: test stock API ===================
# query Tesla stock historical data in:
# https://rapidapi.com/apidojo/api/yahoo-finance1

import requests

RAPIDAPI_KEY  = "f485d68c54msheb2801d8c5166e7p14a601jsnf8378d101955"
RAPIDAPI_HOST = "apidojo-yahoo-finance-v1.p.rapidapi.com"

def fetchStockDataFor(symbol):
  url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-charts"
  querystring = {
    "symbol":symbol,
    "interval":"5m",
    "range":"1d",
    "region":"US"
  }
  headers = {
    'x-rapidapi-key': RAPIDAPI_KEY,
    'x-rapidapi-host': RAPIDAPI_HOST
  }
  return requests.request("GET", url, headers=headers, params=querystring)

response = fetchStockDataFor("TSLA")

# =========== STEP 3: parse result to what we want ========
from library.JsonParser import JsonParser
parser = JsonParser()
# parser.json_str_to_file(response.text, "data/tesla-stock-data.json")
stock_data = parser.parse(response.text)

# =========== STEP 4: test timestamp conversion using timezone =======
# because our fetched data using EDT time(America/New_York, UTC-4)
from datetime import datetime, timezone, timedelta
tzinfo = timezone(timedelta(seconds=-14400)) # 14400 = 3600*4 seconds
# dt = datetime.fromtimestamp(1625232600, tzinfo)
# mdy = dt.strftime("%m/%d/%Y")
# dby = dt.strftime("%d %B, %Y")
# hm  = dt.strftime("%H:%M")
# print(mdy)
# print(dby)
# print(hm)

# now = datetime.now() # current date and time

# year = now.strftime("%Y")
# print("year:", year)

# month = now.strftime("%m")
# print("month:", month)

# day = now.strftime("%d")
# print("day:", day)

# time = now.strftime("%H:%M:%S")
# print("time:", time)

# date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
# print("date and time:",date_time)	

# ========== STEP 5: extract timestamp list ==============
timestamplist = []
timestamplist.extend(stock_data["chart"]["result"][0]["timestamp"])
# print(timestamplist)
calendertime = []
for ts in timestamplist:
  dt = datetime.fromtimestamp(ts, tzinfo)
  calendertime.append(dt.strftime("%H:%M"))
# print(calendertime)
# print(">>> time length: "+str(len(calendertime))) # 78 points

closedata = []
float_values = stock_data["chart"]["result"][0]["indicators"]["quote"][0]["close"]
fixed_2_points = list(map(lambda x: round(x*100)/100, float_values))
closedata.extend(fixed_2_points)
# print(closedata)
# print(">>> data length: "+str(len(closedata)))

# ========= STEP 6: draw line chart with real data ========
# x axis values
x = calendertime
# corresponding y axis values
y = closedata

# plotting the points
plt.plot(x, y, 'o-')
for a,b in zip(x, y): 
    plt.text(a, b, str(b))
# naming the x axis
plt.xlabel('value')
# naming the y axis
plt.ylabel('time')

# giving a title to my graph
plt.title('Tesla Stock Chart - 2021/07/02')
# rotate x axis labels
plt.xticks(rotation=30)
# function to show the plot
plt.show()