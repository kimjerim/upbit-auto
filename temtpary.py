import time 
import pyupbit
import datetime
import requests
from requests.adapters import Response
from requests.api import post


access="DxIkC32RnuzLntH2dw2tNWxRwRGxq7ugw8f1TsHK"
secret="b5KG1CatTQ1CVqoxl8Z7WTlzEHSHUZixSSV5wcZG"
myToken="xoxb-2065052070515-2065055793955-p5ZVzRniMbn6vym7CVOVYaBJ"


# 슬랙 메시지 
def post_message(token, channel, text):
  response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text})  


# 변동성 돌파 전략
def get_target_price(ticker, k):
  df = pyupbit.get_ohlcv(ticker,count=2)
  target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
  return target_price

# 시작시간 조회
def get_start_time(ticker):
  df = pyupbit.get_ohlcv(ticker, count=1)
  stat_time = df.index[0]
  return stat_time

# 잔고 조회
def get_balance(ticker):
  balances = upbit.get_balances()
  for b in balances:
    if b['currency'] == ticker:
      if b['balance'] is not None:
        return float(b['balance'])
      else:
        return 0 
  return 0

# 현재가 조회
def get_current_price(ticker):
  return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")
post_message(myToken,"#자동매매","Autotrade Start")


# 매매 시작
while True:
  try:
    now = datetime.datetime.now()
    start_time  = get_start_time("KRW-BTC")
    end_time = start_time + datetime.timedelta(days=1)

    if start_time < now < end_time - datetime.timedelta(seconds=10):
      target_price = get_target_price("KRW-BTC", 0.5)
      current_price = get_current_price("KRW-BTC")
      if target_price < current_price:
        krw = get_balance("KRW")
        if krw > 5000:
          buy_result = upbit.buy_market_order("KRW-BTC", 200000)
          post_message(myToken,"#자동매매", "BTC buy:" +str(buy_result))

    else:
      btc = get_balance("BTC")
      if btc > 0.00005: 
        sell_result = upbit.sell_market_order("KRW-BTC", btc*0.9995)
        post_message(myToken,"#자동매매", "BTC buy: " +str(sell_result))
    time.sleep(1)

  except Exception as e:
    print(e)
    post_message(myToken,"#자동매매", e)
    time.sleep(1)









