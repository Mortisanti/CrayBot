#TODO Make a commands table embed
#TODO Consider adding option for video secrets. Embeds can have videos
#TODO Figure out if there's a better way to deal with long descriptions in embeds

import discord
import os
import re
import requests
from lore import lore
from keep_alive import keep_alive
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option


craybot = discord.Client(activity=discord.Game(name='with Aliens'), intents=discord.Intents.default())
slash = SlashCommand(craybot, sync_commands=True)

@craybot.event
async def on_ready():
    print(f"We have logged in as {craybot.user}")


embed_footer_icon = 'https://i.imgur.com/VpMy8Yr.gif'

# Petition Status
@slash.slash(name="petition", description="Check the current signature-count on the Remaster Area 51 petition.")
async def get_petition_status(ctx):
    signatures_regex = r'\"signatureCount\":{\"displayed\":[0-9]+,\"total\":([0-9]+),\"goal\":([0-9]+)}'
    cookies = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0'}
    petition_url = 'https://www.change.org/p/warner-brothers-remaster-area-51-2005-fps-game'
    youtube_url = 'https://www.youtube.com/watch?v=fm0tdZa2MRw'
    r = requests.get(petition_url, cookies=cookies)
    match = re.search(signatures_regex, r.text)
    signatures_count = match.group(1)
    signatures_goal = match.group(2)
    petition_embed = discord.Embed(
        type='rich',
        title="REMASTER AREA 51 - SIGN THE PETITION",
        description=f"**Sign the Petition! - {petition_url}\n\nPetition Promo Video - {youtube_url}**",
        color=0x00ffd9,
        url=petition_url
        )
    petition_embed.set_image(url='https://i.imgur.com/pQ6xByj.png')
    petition_embed.add_field(
        name="Current Signatures",
        value=signatures_count,
        inline=True
        )
    petition_embed.add_field(
        name="Signature Goal",
        value=signatures_goal,
        inline=True
        )
    petition_embed.set_footer(icon_url=embed_footer_icon,
                              text="Remaster Area 51"
                              )
    await ctx.send(embed=petition_embed)


# Databank List
@slash.subcommand(base="databank",
                  name="list",
                  description="Print out a numbered list of all entries in the databank."
                  )
async def get_databank_list(ctx):
    trimmed_lore_list = lore.get_lore_list()
    databank_embed = discord.Embed(
        type='rich',
        title="Databank List",
        description=trimmed_lore_list,
        color=0x00ffd9
        )
    databank_embed.set_footer(icon_url=embed_footer_icon,
                              text="Databank List"
                              )
    await ctx.send(embed=databank_embed)


# Databank Entry
@slash.subcommand(base="databank",
                  name="entry",
                  description="Retrieve a specific entry from the databank.",
                  options=[
                      create_option(
                          name="entry",
                          description="Enter a number between 1-90.",
                          option_type=4,
                          required=True)
                  ])
async def get_databank_entry(ctx, entry: int):
    level, short_desc, img_url, long_desc = lore.get_lore(entry)
    databank_embed = discord.Embed(
        type='rich',
        title=short_desc,
        description=long_desc,
        color=0x00ffd9,
        url=img_url
        )
    databank_embed.set_image(url=img_url)
    databank_embed.set_footer(icon_url=embed_footer_icon,
                              text=f"From the Level: {level}"
                              )
    await ctx.send(embed=databank_embed)


# Databank Random
@slash.subcommand(base="databank",
                  name="random",
                  description="Retrieve a random entry from the databank."
                  )
async def get_databank_random(ctx):
    level, short_desc, img_url, long_desc = lore.get_lore()
    databank_embed = discord.Embed(
        type='rich',
        title=short_desc,
        description=long_desc,
        color=0x00ffd9,
        url=img_url
        )
    databank_embed.set_image(url=img_url)
    databank_embed.set_footer(icon_url=embed_footer_icon,
                              text=f"From the Level: {level}"
                              )
    await ctx.send(embed=databank_embed)


keep_alive()
craybot.run(os.environ['DISCORD_TOKEN'])