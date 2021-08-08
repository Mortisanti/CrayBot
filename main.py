#TODO Make a commands table embed
#TODO Consider adding option for video secrets. Embeds can have videos
#TODO Figure out if there's a better way to deal with long descriptions in embeds

import discord
import os
from lore import lore
from keep_alive import keep_alive
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option

craybot = discord.Client(activity=discord.Game(name='with Aliens'), intents=discord.Intents.default())
slash = SlashCommand(craybot, sync_commands=True)

@craybot.event
async def on_ready():
    print(f"We have logged in as {craybot.user}")

# @slash.slash(name="databank", description="Retrieve a random piece of AREA-51 lore from the databank")
# async def databank(ctx):
#     level, short_desc, img_url, long_desc = lore.get_lore()
#     footer_icon_url = 'https://i.imgur.com/VpMy8Yr.gif'
#     databank_embed = discord.Embed(
#         type='rich',
#         title=short_desc,
#         description=long_desc,
#         color=0x00ffd9,
#         url=img_url
#         )
#     databank_embed.set_image(url=img_url)
#     databank_embed.set_footer(text=f"From the Level: {level}", icon_url=footer_icon_url)
#     await ctx.send(embed=databank_embed)

@slash.slash(name="databanklist", description="Print out a numbered list of each databank entry and the level it corresponds to.")
async def databank_list(ctx):
    trimmed_lore_list = lore.get_lore_list()
    footer_icon_url = 'https://i.imgur.com/VpMy8Yr.gif'
    databank_embed = discord.Embed(
        type='rich',
        title="Databank List",
        description=trimmed_lore_list,
        color=0x00ffd9
        )
    # databank_embed.set_image(url=img_url)
    databank_embed.set_footer(text=f"Databank List", icon_url=footer_icon_url)
    await ctx.send(embed=databank_embed)

@slash.slash(name="databankrandom", description="Retrieve a random entry from the databank.")
async def databank_random(ctx):
    level, short_desc, img_url, long_desc = lore.get_lore()
    footer_icon_url = 'https://i.imgur.com/VpMy8Yr.gif'
    databank_embed = discord.Embed(
        type='rich',
        title=short_desc,
        description=long_desc,
        color=0x00ffd9,
        url=img_url
        )
    databank_embed.set_image(url=img_url)
    databank_embed.set_footer(text=f"From the Level: {level}", icon_url=footer_icon_url)
    await ctx.send(embed=databank_embed)

@slash.slash(name="databankentry", description="Enter a number between 1-90 to retrieve a specific entry from the databank.")
async def databank_entry(ctx, entry: int):
    level, short_desc, img_url, long_desc = lore.get_lore(entry)
    footer_icon_url = 'https://i.imgur.com/VpMy8Yr.gif'
    databank_embed = discord.Embed(
        type='rich',
        title=short_desc,
        description=long_desc,
        color=0x00ffd9,
        url=img_url
        )
    databank_embed.set_image(url=img_url)
    databank_embed.set_footer(text=f"From the Level: {level}", icon_url=footer_icon_url)
    await ctx.send(embed=databank_embed)
keep_alive()
craybot.run(os.environ['DISCORD_TOKEN'])