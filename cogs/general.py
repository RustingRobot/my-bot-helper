import discord
from discord.ext import commands

class General(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("General cog online!")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"pong ( {round(self.client.latency * 1000)} ms )")

    @commands.command()
    async def off(self, ctx):
        if str(ctx.author) == "Rusting Robot#7758":
            await ctx.message.add_reaction("☑️")
            await self.client.logout()

def setup(client):
    client.add_cog(General(client))