import discord
from discord.ext import commands

import os

# -- invite --
#https://discord.com/api/oauth2/authorize?client_id=713774249235710002&permissions=51264&scope=bot
# --        --

client = commands.Bot(command_prefix = ";")

@client.event
async def on_ready():
    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.listening, name="; commands"))
    print("MBHelper is online!")

for filename in os.listdir("./cogs"):   #load all cogs in the cogs folder
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

load_dotenv()
client.run(os.environ.get("DISCORD_TOKEN"))
