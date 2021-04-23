### CREATED BY GUSBELL ###

import discord, os, asyncio

import numpy as np

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
    activity = discord.Game(name="$Help | In Development", type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print('Euler has logged in as {0.user}!'.format(client))
    print('Discord.py version : ' + discord.__version__)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    m = message.content

    if any(word in m for word in Commands.Help):
        t = await message.channel.send('Available commands : ```$Help, $Generate, $Info```')
        await asyncio.sleep(30)
        await message.delete()
        await t.delete()

    if any(word in m for word in Commands.Info):
        t = await message.channel.send('Created by Gusbell for POSN discord channel, further more information please visit https://github.com/Gusb3ll/Euler-bot')
        await asyncio.sleep(30)
        await message.delete()
        await t.delete()

### Real miracle begin here ###

    if m.startswith('$Generate alg 1'): #!
        t = await message.channel.send(file=discord.File(np.random.choice(Problems.Alg_Easy)))
        await asyncio.sleep(30)
        await message.delete()
        await t.delete()
    elif m.startswith('$Generate alg 2'):
        t = await message.channel.send(file=discord.File(np.random.choice(Problems.Alg_Normal)))
        await asyncio.sleep(30)
        await message.delete()
        await t.delete()
    elif m.startswith('$Generate alg 3'):
        t = await message.channel.send(file=discord.File(np.random.choice(Problems.Alg_Hard)))
        await asyncio.sleep(30)
        await message.delete()
        await t.delete()
    elif m.startswith('$Generate geo 1'): #!
        t = await message.channel.send(file=discord.File(np.random.choice(Problems.Geo_Easy)))
        await asyncio.sleep(30)
        await message.delete()
        await t.delete()
    elif m.startswith('$Generate geo 2'):
        t = await message.channel.send(file=discord.File(np.random.choice(Problems.Geo_Normal)))
        await asyncio.sleep(30)
        await message.delete()
        await t.delete()
    elif m.startswith('$Generate geo 3'):
        t = await message.channel.send(file=discord.File(np.random.choice(Problems.Geo_Hard)))
        await asyncio.sleep(30)
        await message.delete()
        await t.delete()
    elif m.startswith('$Generate com 1'): #!
        t = await message.channel.send(file=discord.File(np.random.choice(Problems.Com_Easy)))
        await asyncio.sleep(30)
        await message.delete()
        await t.delete()
    elif m.startswith('$Generate com 2'):
        t = await message.channel.send(file=discord.File(np.random.choice(Problems.Com_Normal)))
        await asyncio.sleep(30)
        await message.delete()
        await t.delete()
    elif m.startswith('$Generate com 3'):
        t = await message.channel.send(file=discord.File(np.random.choice(Problems.Com_Hard)))
        await asyncio.sleep(30)
        await message.delete()
        await t.delete()
    elif m.startswith('$Generate iq 1'): #!
        t = await message.channel.send(file=discord.File(np.random.choice(Problems.iq_Easy)))
        await asyncio.sleep(30)
        await message.delete()
        await t.delete()
    elif m.startswith('$Generate iq 2'):
        t = await message.channel.send(file=discord.File(np.random.choice(Problems.iq_Normal)))
        await asyncio.sleep(30)
        await message.delete()
        await t.delete()
    elif m.startswith('$Generate iq 3'):
        t = await message.channel.send(file=discord.File(np.random.choice(Problems.iq_Hard)))
        await asyncio.sleep(30)
        await message.delete()
        await t.delete()
    elif m.startswith('$Generate num 1'): #!
        t = await message.channel.send(file=discord.File(np.random.choice(Problems.num_Easy)))
        await asyncio.sleep(30)
        await message.delete()
        await t.delete()
    elif m.startswith('$Generate num 2'):
        t = await message.channel.send(file=discord.File(np.random.choice(Problems.num_Normal)))
        await asyncio.sleep(30)
        await message.delete()
        await t.delete()
    elif m.startswith('$Generate num 3'):
        t = await message.channel.send(file=discord.File(np.random.choice(Problems.num_Hard)))
        await asyncio.sleep(30)
        await message.delete()
        await t.delete()
    elif m.startswith('$Generate func 1'): #!
        t = await message.channel.send(file=discord.File(np.random.choice(Problems.func_Easy)))
        await asyncio.sleep(30)
        await message.delete()
        await t.delete()
    elif m.startswith('$Generate func 2'):
        t = await message.channel.send(file=discord.File(np.random.choice(Problems.func_Normal)))
        await asyncio.sleep(30)
        await message.delete()
        await t.delete()
    elif m.startswith('$Generate func 3'):
        t = await message.channel.send(file=discord.File(np.random.choice(Problems.func_Hard)))
        await asyncio.sleep(30)
        await message.delete()
        await t.delete()
    elif m.startswith('$Generate'):
        p1 = await message.channel.send('Usage : ```$Generate [topic] [difficulty]```')
        p2 = await message.channel.send('List of topic : ```alg - Algebra, geo - Geometry, com - Combinatoric, iq - Inequality, num - Number theory, func - Functional Equation```')
        p3 = await message.channel.send('List of difficulty : ```1 Easy, 2 Normal , 3 Hard```')
        await asyncio.sleep(30)
        await message.delete()
        await p3.delete()
        await p2.delete()
        await p1.delete()

########## Test stuff #########

    if m.startswith('$test'):
        t = await message.channel.send('Rendering...')
        await asyncio.sleep(5)
        #!#INSERT LATEX FUNCTION#!#
        await message.delete()
        await t.delete()

###############################

    if any(word in m for word in Commands.Shutdown):
        if message.author.id == 297306376542224385:
            t = await message.channel.send('Shutting down...')
            await asyncio.sleep(5)
            await message.delete()
            await t.delete()
            await asyncio.sleep(.1)
            await client.logout()
        else:
            t = await message.channel.send("You don't have permission to perform this action.")
            await asyncio.sleep(5)
            await message.delete()
            await t.delete()

client.run(TOKEN)
