import discord
from discord.ext import commands

import json
import requests
import random
from bs4 import BeautifulSoup
from random import randint

class Stats(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Stats comments cog online!")

    @commands.Cog.listener()
    async def on_message(self, msg):
        if 'https://scratch.mit.edu/projects/' in msg.content:
            start = msg.content.index("https://scratch.mit.edu/projects/") + 33
            if(start >= len(msg.content) or not msg.content[start].isnumeric()):
                return
            end = start
            while msg.content[end].isnumeric():
                end += 1
                if end == len(msg.content):
                    break
            embed=discord.Embed(color=0x007ffc)
            embed.set_author(name="TurboWarp link", url=f"https://turbowarp.org/{msg.content[start:end]}/embed", icon_url=f"https://cdn2.scratch.mit.edu/get_image/project/{msg.content[start:end]}_480x360.png")
            await msg.channel.send(embed = embed)

    @commands.command()
    async def comment(self, ctx):
        response = requests.get("https://api.scratch.mit.edu/proxy/featured")
        resJson = response.json()
        random_index = randint(0, len(resJson["community_featured_projects"])-1)
        projectID = resJson['community_featured_projects'][random_index]['id']
        user = resJson['community_featured_projects'][random_index]['creator']
        title = resJson['community_featured_projects'][random_index]['title']
        url = f"https://scratch.mit.edu/projects/{projectID}/"
        comments = requests.get(f"https://api.scratch.mit.edu/users/{user}/projects/{projectID}/comments?offset=0&limit=20")
        resJson = comments.json()
        random_index = randint(0, len(resJson)-1)

        MBList = ["How nice!","But I disagree with that","Which sums it up pretty well", f"thanks {user}, very cool!", "constructive criticism at it's finest", "I think he has a point"]
        if(resJson[random_index]['content'].find("https://scratch.mit.edu/projects/")>-1):
            MBList = ["oi, no advertising","advertising is against the tos!","StOp WiTh ThE AdVeRtiZiNG, GuYs"]
        embed=discord.Embed(color=0x0080ff)
        embed.set_thumbnail(url=resJson[random_index]['author']['image'])
        embed.add_field(name=f"{user} commented:\n{resJson[random_index]['content']}", value=f"on the project: {title}", inline=True)
        embed.set_footer(text=random.choice(MBList))
        await ctx.send(embed=embed)
        return

def setup(client):
    client.add_cog(Stats(client))