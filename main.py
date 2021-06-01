import discord
from discord.ext import commands

import os

client = commands.Bot(command_prefix = ";")

@client.event
async def on_ready():
    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.listening, name="; commands"))
    print("MBHelper is online!")

for filename in os.listdir("./cogs"):   #load all cogs in the cogs folder
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(os.environ.get("DISCORD_TOKEN"))
