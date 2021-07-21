import discord
import requests
import random
from discord_slash import SlashCommand

client_id = '866752200206319656'

craybot = discord.Client(activity=discord.Game(name='with Aliens'), intents=discord.Intents.default())
slash = SlashCommand(craybot, sync_commands=True)

@craybot.event
async def on_ready():
    print(f"We have logged in as {craybot.user}")

