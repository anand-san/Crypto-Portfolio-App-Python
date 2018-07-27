# Author : seanjin17
# Twitter : twitter.com/seanjin17
# Discord : https://discord.gg/z6ksxDA
# Feel Free to contact me if you fine any issues

import threading
import requests
import json
import time
import hashlib
import base64
import hmac


btcdata=requests.get("https://api.bitfinex.com/v1/pubticker/btcusd")
btc=btcdata.json()
btcusd=float(btc["last_price"])
url = 'https://api.bitfinex.com/v1/balances'
payloadObject = {
                'request':'/v1/balances',
                'nonce':str((time.time() * 100000)),
                'options':{}
                }
payload_json = json.dumps(payloadObject)
data_bytes = payload_json.encode("utf-8")
payload = base64.b64encode(data_bytes)
api_secret=bytes("Your Api Key", 'latin-1')
api_key=bytes("Your Api Secret",'latin-1')
m=hmac.new(api_secret, payload, hashlib.sha384)
signature=m.hexdigest()
headers = {
        'X-BFX-APIKEY' : api_key,
        'X-BFX-PAYLOAD' : base64.b64encode(data_bytes),
        'X-BFX-SIGNATURE' : signature
        }
r = requests.get(url, data={}, headers=headers)
info=r.json()
coin=[]
holding=[]
totalusdbal=[0.0]
val_finex=[]
coinval=[]
percentportfolio=[]
totalportfoliofinex=[]
def clear_finex():
                coin.clear()
                holding.clear()
                val_finex.clear()
                coinval.clear()
                percentportfolio.clear()
                totalportfoliofinex.clear()
def loop(i):
                try:
                                if float(info[i]["amount"]) > 0.0:
                                    if str(info[i]["currency"]) == "usd":
                                        	totalusdbal[0]+=float(info[i]["amount"])
                                    else:
                                                coinval=str(info[i]["currency"])
                                                coinval=coinval.upper()
                                                totalbalance=float(info[i]["amount"])
                                                coin.append(coinval)
                                                holding.append(totalbalance)		
                                loop(i+1)
                except:
                        coin.append("USD")
                        holding.append(totalusdbal[0])
                        usdcalc()

def usdcalc():
	for x in coin:
		if x != "USD":
			getusdval=requests.get("https://api.bitfinex.com/v1/pubticker/"+x+"usd")
			getusdvaljson=getusdval.json()
			usdval=float(getusdvaljson["last_price"])
			coinval.append(usdval)
		else:
			coinval.append(1)
	finalusd = [a * b for a, b in zip(holding, coinval)]
	totalportfolio=sum(finalusd)
	totalportfoliofinex.append(str(round(totalportfolio,2)))
	for y in finalusd:
		perc=y/totalportfolio
		perc1=float(perc*100)
		percentportfolio.append(round(perc1,2))
	printresults()
def printresults():
        totalusdbal.clear()
        totalusdbal.append(0.0)
        for a,b in zip(coin,percentportfolio):
            val_finex.append((str(a)+ ": " +str(b)) +"%")

