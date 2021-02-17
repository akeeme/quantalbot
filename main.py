import discord
from discord.ext import commands
import os
import yfinance as yf
import asyncio
from datetime import date

token = os.getenv('token')


class MyClient(discord.Client):
    async def on_ready(self):
        await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name = "the Stock Market"))
        print('Logged in')
    
    async def on_message(self, message: discord.message.Message):
      # async with message.typing():
      #   await asyncio.sleep(2)
      if message.author.id != client.user.id:
        if message.content.startswith('$s'):

          stock = message.content.split(' ')[1].upper()
          ticker = yf.Ticker(stock)
          s_high = ticker.info.get("dayHigh")
          s_low = ticker.info.get("dayLow")
          s_url = ticker.info.get("website")
          s_name = ticker.info.get("longName")
          s_logo = ticker.info.get("logo_url")


          embed=discord.Embed(
          title= stock,
              url=s_url,
              description=f"Stock info for {s_name}" ,
              color=discord.Color.purple())
          embed.set_author(name=f"{s_name}", url=f"{s_url}", icon_url=f"{s_logo}")
          embed.add_field(name="**Day High**", value=f"${s_high}", inline=False)
          embed.add_field(name="**Day Low**", value=f"${s_low}", inline=False)
          #embed.add_field(name="**Options**", value=f"${opt}", inline=False)
          await message.channel.send(embed = embed)

        if message.content.startswith('$op'):
          # today = date.today()
          # td_day = today.strftime("%Y/%m/%d")
          stock = message.content.split(' ')[1].upper()
          ticker = yf.Ticker(stock)
          s_url = ticker.info.get("website")
          s_name = ticker.info.get("longName")
          s_logo = ticker.info.get("logo_url")
          opt = ticker.options
          embed = discord.Embed(
          title = stock,
            url = s_url,
            description = f"Options info for {s_name}",
            color = discord.Color.purple())
          embed.set_author(name = f"{s_name}", url = f"{s_url}", icon_url = f"{s_logo}")
          embed.add_field(name = "**Option Dates**", value = f"{opt}")

          await message.channel.send(embed = embed)
        
        if message.content.startswith('$chain'):
          stock = message.content.split(' ')[1].upper()
          opDate = message.content.split(' ')[2]
          ticker = yf.Ticker(stock)
          s_url = ticker.info.get("website")
          s_name = ticker.info.get("longName")
          s_logo = ticker.info.get("logo_url")
          opt = ticker.option_chain(opDate)
          embed = discord.Embed(
          title = stock,
            url = s_url,
            description = f"Options Chain for {s_name}",
            color = discord.Color.purple())
          embed.set_author(name = f"{s_name}", url = f"{s_url}", icon_url = f"{s_logo}")
          embed.add_field(name = "**Options**", value = f"{opt}")


          


          # opt = stock.option_chain(td_day)


        
      

        #if the message starts with something from the list command_list aka starts with $help or $command then execute code

        #.startswith is not a discord function its a python built in funciton
        command_list = ['$help', '$commands'] #this list

        if message.content.startswith(tuple(command_list)):
          embed = discord.Embed(#embed is a discord made command that embeds a format into text params are title, desc, color
            title = "Command List",
            description = "$s (ticker) - gives the Day high and Day low for a stock**" + "\n \n" + "**$help or $commands - gives list of commands",
            color = discord.Color.purple())
          await message.channel.send (embed = embed)
        if message.content.startswith('$q'):
          async with message.typing():
            await asyncio.sleep(2)
          await message.channel.send("typing test")

          
          
















    # async def on_message(self, message: discord.message.Message):
    #   if message.author.id != client.user.id:
    #     if message.content.startswith('$stock'):
    #       stock = message.content.split(' ')[1].upper()
    #       ticker = yf.Ticker(stock)
    #       s_high = ticker.info.get("dayHigh")
    #       s_low = ticker.info.get("dayLow")
    #       title=stock,
    #   embed = discord.embed(
    #   url=ticker.info.get("website"),
    #   description="Information for ", stock,
    #   color=discord.Color.blue())
    # embed.set_author(name=ticker.info.get("longName"), 
    # embed.add_field(name="**Day High**", value=f"${s_high}", inline=False),
    # embed.add_field(name = "**Day Low**", value=f"${s_low}", inline=False)
    

          # await message.channel.send(f"The day high for {stock} is ${s_high}, the day low is ${s_low}")
          # print (ticker, "\n", stock)

# @client.event
# async def on_ready():
#   print(f"Logged in as {client.user}")

# async def on_message(message):
#   if message.author == client:
#     return
#   command_list = ['$help', '$commands']
#   if any(command in message.content.lower() for command in command_list):
#     msg = "hello"
#     await client.send_message(message.channel, msg + "the only command available is $stock")
#   elif message.content.startswith('$stock'):
#     stock = message.content.split(' ')[1].upper()
#     ticker = yf.Ticker(stock)
#     s_high = stock.info.get("dayHigh")
#     s_low = stock.info.get("dayLow")
#     await message.channel.send( f"The day high for {ticker} is ${s_high}, the day low is ${s_low}")
  

  


# bot = commands.Bot(command_prefix="$")

# # @bot.commamd()
# # #on ready func when bot is ready
# # async def on_ready(): 
# #     print('Bot is ready')
# @bot.event
# async def on_ready():
#   print('Logged in')


# @bot.command()
# async def hi(ctx):
#     await ctx.channel.send("quantal")

# @bot.command()
# async def stock(ctx, ticker):
#   stock = yf.Ticker(str(ticker.upper()))
#   s_high = stock.info.get("dayHigh")
#   s_low = stock.info.get("dayLow")
#   # s_name = stock.info.get("shortName")
#   # s_ask = stock.info.get("ask")
#   # s_bid = stock.info.get("bid")
#   # s_open = stock.info.get("open")
#   # await ctx.channel.send("no")
#   await bot.send_message(s_high, s_low)
#   # await msg(s_name,"\n", "open price is ", s_open, "\n" "day high is ", s_high, "\n", "day low is ", s_low, "\n", "ask price is ", "\n", s_ask, "\n", "bid price is ", s_bid) 



client = MyClient()
client.run(token)

