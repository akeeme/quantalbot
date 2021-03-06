import discord
from discord.ext import commands
import os
import yfinance as yf
import asyncio
from datetime import date
import requests
import numpy as np

token = os.getenv('token')
rKey = os.getenv('rKey')
rHost = os.getenv('rHost')


class MyClient(discord.Client):
    async def on_ready(self):
        await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name = "the Stock Market"))
        print('Logged in as', client.user.name)

    
    async def on_message(self, message: discord.message.Message):
      

        if message.author.id != client.user.id:

          try:
            if message.content.startswith('$stock'):
              await message.channel.trigger_typing()
              stock = message.content.split(' ')[1].upper()
              ticker = yf.Ticker(stock)
              s_high = ticker.info.get("dayHigh")
              s_low = ticker.info.get("dayLow")
              s_url = ticker.info.get("website")
              s_name = ticker.info.get("longName")
              s_logo = ticker.info.get("logo_url")
              prev_close = ticker.info.get("previousClose")

              embed=discord.Embed(
              title= stock,
                  url=s_url,
                  description=f"Stock info for {s_name}" ,
                  color=discord.Color.purple())
              embed.set_author(name=f"{s_name}", url=f"{s_url}", icon_url=f"{s_logo}")     
              embed.add_field(name="**Day High**", value=f"${s_high}", inline=False)
              embed.add_field(name="**Day Low**", value=f"${s_low}", inline=False)
              embed.add_field(name = "**Previous Close**", value = f"${prev_close}", inline = False)


              await message.channel.send(embed = embed)
          except (ImportError, KeyError):

            embedError=discord.Embed(color=discord.Color.purple())
            embedError.add_field(name="Error", value="Invalid Ticker, try again")
            
            await message.channel.send(embed = embedError)

          

          try:
              
            if message.content.startswith('$split'):
              await message.channel.trigger_typing()
              stock = message.content.split(' ')[1].upper()
              ticker = yf.Ticker(stock)
              s_url = ticker.info.get("website")
              s_name = ticker.info.get("longName")
              s_logo = ticker.info.get("logo_url")
              splits = ticker.splits
              embed = discord.Embed(
              title = stock,
                url = s_url,
                description = f"Splits for {s_name}",
                color = discord.Color.purple())
              embed.set_author(name = f"{s_name}", url = f"{s_url}", icon_url = f"{s_logo}")
              embed.add_field(name = "**Splits**", value = f"{splits}")

              await message.channel.send(embed = embed)

          except (ImportError, KeyError):

            embedError=discord.Embed(color=discord.Color.purple())
            embedError.add_field(name="Error", value="Invalid Ticker, try again")
            
            await message.channel.send(embed = embedError)
          
          # dividends not working right now (api's fault)


          # if message.content.startswith('$div'):
          #   stock = message.content.split(' ')[1].upper()
          #   ticker = yf.Ticker(stock)
          #   s_url = ticker.info.get("website")
          #   s_name = ticker.info.get("longName")
          #   s_logo = ticker.info.get("logo_url")
          #   div = ticker.dividends
          #   print("div started")
          #   embed = discord.Embed(
          #   title = stock,
          #     url = s_url,
          #     description = f"Dividends for {s_name}",
          #     color = discord.Color.purple())
          #   embed.set_author(name = f"{s_name}", url = f"{s_url}", icon_url = f"{s_logo}")
          #   embed.add_field(name = "**Dividends**", value = f"{div}")

          try:

            if message.content.startswith('$trend'):
              await message.channel.trigger_typing()
              url="https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-trending-tickers"


              querystring = {"region":"US"}
              
            
              headers = {
                'x-rapidapi-key': rKey,
                'x-rapidapi-host': rHost
        }
              response = requests.request("GET", url, headers=headers, params=querystring)

              r2 = response.json()

              # stonk 1
              
              q1 = r2["finance"]['result'][0]['quotes'][0]
              stonk1 = q1['symbol']
              stock1_market_price = q1['regularMarketPrice']
              s1MCP = q1['regularMarketChangePercent']
              stock1_market_change_per = (float(np.round(s1MCP, 2)))
            


              # stonk 2
              q2 = r2["finance"]['result'][0]['quotes'][1]
              stonk2 = q2['symbol']
              stock2_market_price = q2['regularMarketPrice']
              s2MCP = q2['regularMarketChangePercent']
              stock2_market_change_per = (float(np.round(s2MCP, 2)))
              


              # stonk 3
              q3 = r2["finance"]['result'][0]['quotes'][2]
              stonk3 = q3['symbol']
              stock3_market_price = q3['regularMarketPrice']
              s3MCP = q3['regularMarketChangePercent']
              stock3_market_change_per = (float(np.round(s3MCP, 2)))
              

              # stonk 4
              q4 = r2["finance"]['result'][0]['quotes'][3]
              stonk4 = q4['symbol']
              stock4_market_price = q4['regularMarketPrice']
              s4MCP = q4['regularMarketChangePercent']
              stock4_market_change_per = (float(np.round(s4MCP, 2)))
              


              # stonk 5
              q5 = r2["finance"]['result'][0]['quotes'][4]
              stonk5 = q5['symbol']
              stock5_market_price = q5['regularMarketPrice']
              s5MCP = q5['regularMarketChangePercent']
              stock5_market_change_per = (float(np.round(s5MCP, 2)))
              
              

              embed = discord.Embed(
              title = "Trending Tickers",
              description = "This is a list of the current top 5 trending tickers in the stock market. (Information from Yahoo Finance)" ,
                color = discord.Color.purple())


              embed.add_field(name = "Stock", value=f"{stonk1} \n {stonk2} \n {stonk3} \n {stonk4} \n {stonk5}", inline = True)

              embed.add_field(name = "Price", value = f"${stock1_market_price} \n ${stock2_market_price} \n ${stock3_market_price} \n ${stock4_market_price} \n ${stock5_market_price}", inline = True)

              embed.add_field(name = "Change", value = f"{stock1_market_change_per}% \n {stock2_market_change_per}% \n {stock3_market_change_per}% \n {stock4_market_change_per}% \n {stock5_market_change_per}%", inline = True)

              await message.channel.send(embed = embed)

          except (ImportError, KeyError):

            embedError=discord.Embed(color=discord.Color.purple())
            embedError.add_field(name="Error", value="Invalid Ticker, try again")
            
            await message.channel.send(embed = embedError)


          #if the message starts with something from the list command_list aka starts with $help or $command then execute code

          #.startswith is not a discord function its a python built in funciton
          command_list = ['$help', '$commands'] #this list

          if message.content.startswith(tuple(command_list)):
            await message.channel.trigger_typing()
            embed = discord.Embed(#embed is a discord made command that embeds a format into text params are title, desc, color
              title = "Command List",
              description = "$s (ticker) - gives the Day high and Day low for a stock**" + "\n \n" + "**$help or $commands - gives list of commands",
              color = discord.Color.purple())
            await message.channel.send (embed = embed)

          

          try:

            if message.content.startswith('$chart'):
              await message.channel.trigger_typing()
              stock = message.content.split(' ')[1].upper()
              ticker = yf.Ticker(stock)
              s_url = ticker.info.get("website")
              s_name = ticker.info.get("longName")
              s_logo = ticker.info.get("logo_url")
              s_high = ticker.info.get("dayHigh")
              chart =  'https://stockcharts.com/c-sc/sc?s=' + stock + '&p=D&b=5&g=0&i=0&r=1615008274751'
            
              embed=discord.Embed(
                color=discord.Color.purple())
              embed.set_author(name=f"{s_name}", url=f"{s_url}", icon_url=f"{s_logo}")     
              embed.set_image(url = chart)
              await message.channel.send(embed = embed)
          except (ImportError, KeyError):

            embedError=discord.Embed(color=discord.Color.purple())
            embedError.add_field(name="Error", value="Invalid Ticker, try again")
            
            await message.channel.send(embed = embedError)




client = MyClient()
client.run(token)

