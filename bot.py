import discord
import os
from config import bot
import config
import asyncio

from src.functions.ows import process_ows

@bot.event
async def on_message(msg):
    await process_ows(msg)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="/help"))
    print(f"Connected to Discord API | Logged in as {bot.user}")

async def main():
  await load_cogs()

  if config.testing == "true":
    await bot.start(config.testing_token)

  else:
    if os.environ["PROD_TOKEN"] == None:
      print("Unable to connect (No token variable set)")
    else:
      await bot.start(os.environ["PROD_TOKEN"])
      

async def load_cogs():
  for file in os.listdir('./src/cogs'):
    if file.endswith('.py'):
      config.bot.load_extension(f'src.cogs.{file[:-3]}')

asyncio.run(main())