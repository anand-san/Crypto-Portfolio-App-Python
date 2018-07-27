# Author : seanjin17
# Twitter : twitter.com/seanjin17
# Discord : https://discord.gg/z6ksxDA
# Feel Free to contact me if you fine any issues

from client import Client
import requests,json
#Api Variables
api_key_binance="Your Api key"
api_secret_binance="Your Secret"

#Variables

btc_data_binance=requests.get("https://api.binance.com/api/v1/ticker/24hr?symbol=BTCUSDT")
btc_binance=btc_data_binance.json()
btcusd_binance=float(btc_binance["lastPrice"])
client = Client(api_key_binance, api_secret_binance)
info_binance = client.get_account()
#print(info_binance)
coin_binance=[]
holding_binance=[]
coinval_binance=[]
percentportfolio_binance=[]
val_binance=[]
totalportfoliobinance=[]
def clear_binance():
        coin_binance.clear()
        holding_binance.clear()
        coinval_binance.clear()
        percentportfolio_binance.clear()
        val_binance.clear()
        totalportfoliobinance.clear()

def start_binance(i):
        try:
                if float(info_binance["balances"][i]["free"]) > 0.0 :
                        #if float(info_binance["balances"][i]["locked"]) > 0.0:
                        coinval_binance=str(info_binance["balances"][i]["asset"])
                        freebalance_binance=float(info_binance["balances"][i]["free"])
                        lockedbalance_binance=float(info_binance["balances"][i]["locked"])
                        totalbalance_binance=freebalance_binance+lockedbalance_binance
                        totalusd_binance=totalbalance_binance*btcusd_binance
                        coin_binance.append(coinval_binance)
                        holding_binance.append(totalbalance_binance)
                start_binance(i+1)
        except:
                usdcalc_binance()
		

def usdcalc_binance():
	for x in coin_binance:
		if x == "BTC":
			coinval_binance.append(btcusd_binance)
		elif x=="USDT":
			coinval_binance.append(1)
		else:
			getbtcval_binance=requests.get("https://api.binance.com/api/v1/ticker/24hr?symbol="+x+"BTC")
			getbtcvaljson_binance=getbtcval_binance.json()
			btcval_binance=float(getbtcvaljson_binance["lastPrice"])
			usdval_binance=btcval_binance*btcusd_binance
			coinval_binance.append(usdval_binance)
	finalusd_binance = [a * b for a, b in zip(holding_binance, coinval_binance)]
	totalportfolio_binance=sum(finalusd_binance)
	totalportfoliobinance.append(str(round(totalportfolio_binance,2)))
	for y in finalusd_binance:
		perc_binance=y/totalportfolio_binance
		perc1_binance=float(perc_binance*100)
		percentportfolio_binance.append(round(perc1_binance,2))
	printresults_binance()
	
def printresults_binance():
	for a,b in zip(coin_binance,percentportfolio_binance):
		if b > 0.0:
			val_binance.append (((str(a)+ ": " +str(b)) +"%"))
