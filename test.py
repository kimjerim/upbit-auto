import pyupbit
import requests


access="2p9uZnoIoEAealnAwqTNgYQxxJeJIZI6EY1u2boS"
secret="ijuCWEMpDdxxmRlHlbVXHW6x4vJ6pqta08m0J9YR"
myToken="xoxb-2065052070515-2065055793955-p5ZVzRniMbn6vym7CVOVYaBJ"

 
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)

upbit = pyupbit.Upbit(access, secret)
print("autotrade start")
post_message(myToken,"#자동매매","Autotrade Start")

def get_balance(ticker):
  balances = upbit.get_balances()
  for b in balances:
    if b['currency'] == ticker:
      if b['balance'] is not None:
        return float(b['balance'])
      else:
        return 0 
  return 0

  
btc = get_balance("BTC")
sell_result = upbit.sell_market_order("KRW-BTC", btc*0.9995)
post_message(myToken,"#자동매매", "BTC buy: " +str(sell_result))    



 


