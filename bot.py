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
start_loop()
start_finex()


@client.event
async def on_message(message):
	if message.content.startswith('!help'):		
		myid = '<@'+message.author.id+'>'
		print(message.author.avatar_url)
		await client.send_message(message.channel, "%s\n```Here are the list of commands available to you : \n!port		Displays Davinci Portfolio\n!dominance		Displays Bitcoin Market dominance\n\n(Only Administrators)\n!worth	Displays Davinci Portfolio worth ```"%myid)	
	elif message.content.startswith('!port'):
		myid = '<@'+message.author.id+'>'	
		if(message.channel.name!="trading"):
			loading = discord.Embed(title="Hey Hey", description="Please use the command in CryptoSurge #trading channel. Here is the invite link http://gg.gg/cryptosurge", color=0xffffff)
			await client.send_message(message.channel, embed=loading)	
			await client.send_message(message.channel, "%s"%myid)
		else:
			loading = discord.Embed(title="Getting Updated Portfolio, Please Wait", description="It wont take long", color=0xffffff)
			await client.send_message(message.channel, embed=loading)		
			start_finex()
			start_loop()
			curr_bal = float(start_finex.total[0])+float(start_loop.total[0])
			ch7d=(((curr_bal-change7d.out)/(change7d.out))*100)
			ch7d=str("{0:.2f}".format(round(ch7d,2)))
			ch24h=(((curr_bal-change24h.out)/(change24h.out))*100)
			ch24h=str("{0:.2f}".format(round(ch24h,2)))
			embed = discord.Embed(title="Davinci Current Holdings", description="", color=0x00ff00)
			embed.add_field(name="Binance", value="\n".join(start_loop.out), inline=True)
			embed.add_field(name="BitFinex", value="\n".join(start_finex.out), inline=True)
			embed.add_field(name="Percentage Change", value="7d : "+ch7d+"%\n24 Hour : "+ch24h+"%", inline=True)
			embed.set_thumbnail(url="http://elewat.com/cryptosurge/discord_thumb.jpg")
			#embed.set_footer(text="Update Frequency : realtime")		
			#embed.add_field(name="Total Portfolio Worth", value="Binance : "+"".join(start_loop.total)+" USD \nBitFinex : "+"".join(start_finex.total)+" USD", inline=False)
			await client.send_message(message.channel, embed=embed)	
			await client.send_message(message.channel, "%s"%myid)
	elif message.content.startswith('!dominance'):
		myid = '<@'+message.author.id+'>'
		if(message.channel.name!="trading"):
			loading = discord.Embed(title="Hey Hey", description="Please use the command in CryptoSurge #trading channel. Here is the invite link http://gg.gg/cryptosurge", color=0xffffff)
			await client.send_message(message.channel, embed=loading)	
			await client.send_message(message.channel, "%s"%myid)
		else:
			domi=requests.get("https://api.coinmarketcap.com/v2/global/")
			domin=domi.json()
			dominan=str(str(domin["data"]["bitcoin_percentage_of_market_cap"]))
			dominanc=(dominan+"%")
			embed = discord.Embed(title="Bitcoin Market Dominance", description="", color=0x00ff00)
			embed.set_thumbnail(url="https://en.bitcoin.it/w/images/en/2/29/BC_Logo_.png")
			embed.add_field(name=dominanc, value=str(time.ctime(time.time()))+" UTC", inline=True)
			embed.set_footer(text="As on coinmarketcap.com")	
			await client.send_message(message.channel, embed=embed)	
			await client.send_message(message.channel, "%s"%myid)			
	elif message.content.startswith('!worth'):
		myid = '<@'+message.author.id+'>'
		#Get discord USER ID and put it here
		if(str(message.author.id)=="Admin ID 1") or (str(message.author.id)=="Admin ID 2"):
			total = float(start_finex.total[0])+float(start_loop.total[0])
			if total < 455000:
				change=455000-total 
				stat = "$"+("{0:.2f}".format(round(total,2)))+"\nDown by $"+("{0:.2f}".format(round(change,2)))
				embed = discord.Embed(title="This data is updated when !port command is used", description="", color=0xff0000)
			elif total > 455000:
				change=total-455000 
				stat = "$"+("{0:.2f}".format(round(total,3)))+"\nUp by $"+("{0:.2f}".format(round(change,2)))
				embed = discord.Embed(title="This data is updated when !port command is used", description="", color=0x00ff00)
			embed.set_thumbnail(url="http://elewat.com/cryptosurge/discord_thumb.jpg")
			embed.add_field(name="Current worth : ", value=stat, inline=True)
			embed.add_field(name="Change", value="7 Day : $"+str("{0:.2f}".format(round(total-change7d.out,2)))+"\n24 Hour : $"+str("{0:.2f}".format(round(total-change24h.out,2))), inline=True)
			await client.send_message(message.channel, embed=embed)
			await client.send_message(message.channel, "%s"%myid)
		else:
			loading = discord.Embed(title="Hey Hey", description="Am not allowed to provide you this information. Only Administrators can access this command", color=0xffffff)
			await client.send_message(message.channel, embed=loading)
			await client.send_message(message.channel, "%s"%myid)
print("Portfolio Bot Online")
client.run(TOKEN)
