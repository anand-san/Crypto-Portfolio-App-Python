# Author : seanjin17
# Twitter : twitter.com/seanjin17
# Discord : https://discord.gg/z6ksxDA
# Feel Free to contact me if you fine any issues


from finex import *
from binance import *
import random
import asyncio
from discord.ext.commands import Bot
import discord
import requests
import json

BOT_PREFIX = ("!")
TOKEN = "Your Bot Token"
client = Bot(command_prefix=BOT_PREFIX)
domi=requests.get("https://api.coinmarketcap.com/v2/global/")
domin=domi.json()
dominan=str(str(domin["data"]["bitcoin_percentage_of_market_cap"]))
dominanc=(dominan+"%")
def finex():
  threading.Timer(603.0, finex).start()
  clear_finex()
  loop(1)
  #readable=time.time()
  #readable = time.ctime(readable)
  #print("Finex Data reloaded : " +str(readable))

def binance():
  threading.Timer(470.0, binance).start()
  clear_binance()
  start_binance(0)
  #readable=time.time()
  #readable = time.ctime(readable)
  #print("Binance Data reloaded : " +str(readable))

binance()
finex()
#print(fila)
@client.event
async def on_message(message):
	if message.content.startswith('!port'):
		embed = discord.Embed(title="Current Holdings", description="", color=0x00ff00)
		embed.add_field(name="Binance", value="\n".join(val_binance), inline=True)
		embed.add_field(name="BitFinex", value="\n".join(val_finex), inline=True)
		embed.set_footer(text="Update Frequency : 505 Seconds")		
		embed.add_field(name="Total Portfolio Worth", value="Binance : "+"".join(totalportfoliobinance)+" USD \nBitFinex : "+"".join(totalportfoliofinex)+" USD", inline=False)
		await client.send_message(message.channel, embed=embed)
	elif message.content.startswith('!dominance'):
		embed = discord.Embed(title="Bitcoin Market Dominance", description="", color=0x00ff00)
		embed.set_thumbnail(url="https://en.bitcoin.it/w/images/en/2/29/BC_Logo_.png")
		embed.add_field(name=dominanc, value=str(time.ctime(time.time()))+" UTC", inline=True)
		await client.send_message(message.channel, embed=embed)
		
async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600000)


client.loop.create_task(list_servers())
client.run(TOKEN)
