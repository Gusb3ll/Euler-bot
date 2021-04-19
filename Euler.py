### CREATED BY GUSBELL ###

import discord, os, asyncio, random

from pathlib import Path
from dotenv import load_dotenv

from objects import Commands, Problems

env_path = Path('.', '.env')

load_dotenv(dotenv_path=env_path)
TOKEN = os.getenv('DISCORD_TOKEN')
SECRET_KEY = os.getenv('SECRET_KEY')

client = discord.Client()

##### --- Bot Static & Function --- #####

###### --- End of Bot Function --- ######

@client.event
async def on_ready():
    print('Euler has logged in as {0.user}!'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    m = message.content

    if any(word in m for word in Commands.Help):
        await message.channel.send('Available commands : ```$Help, $Generate, $Info```')

    if any(word in m for word in Commands.Info):
        await message.channel.send('Created by Gusbell for POSN discord channel,')
        asyncio.sleep(1)
        await message.channel.send('further information please visit https://github.com/Gusb3ll/Euler-bot')

### Real miracle begin here ###

    if m.startswith('$Generate 1'): 
        t = await message.channel.send(file=discord.File(random.choice(Problems.Beginner)))
        await asyncio.sleep(1)
        await message.delete()
        await asyncio.sleep(30)
        await t.delete()
    elif m.startswith('$Generate 2'):
        t = await message.channel.send(file=discord.File(random.choice(Problems.Intermediate)))
        await asyncio.sleep(1)
        await message.delete()
        await asyncio.sleep(30)
        await t.delete()
    elif m.startswith('$Generate 3'):
        t = await message.channel.send(file=discord.File(random.choice(Problems.Expert)))
        await asyncio.sleep(1)
        await message.delete()
        await asyncio.sleep(30)
        await t.delete()
    elif m.startswith('$Generate 4'):
        t = await message.channel.send(file=discord.File(random.choice(Problems.Master)))
        await asyncio.sleep(1)
        await message.delete()
        await asyncio.sleep(30)
        await t.delete()
    elif m.startswith('$Generate'):
        p1 = await message.channel.send('Usage : ```$Generate [difficulty]```')
        await asyncio.sleep(1)
        p2 = await message.channel.send('List of difficulty : ```1 Beginner, 2 Intermeiate , 3 Expert , 4 Master```')
        await asyncio.sleep(10)
        await p1.delete()
        await p2.delete()

########## Test stuff #########

    if m.startswith('$test'):
        p = await message.channel.send('Rendering...')
        await asyncio.sleep(5)
        #!#INSERT LATEX FUNCTION#!#
        await asyncio.sleep(1)
        await p.delete()

    if m.startswith('$meme'):
        t = await message.channel.send(file=discord.File(random.choice(Problems.Meme)))
        await asyncio.sleep(1)
        await message.delete()
        await asyncio.sleep(60)
        await t.delete()

###############################

    if any(word in m for word in Commands.Shutdown):
        if message.author.id == 297306376542224385:
            await message.channel.send('Shutting down...')
            await client.logout()
        else:
            await message.channel.send("You don't have permission to perform this action.")

client.run(TOKEN)
