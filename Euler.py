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
        t = await message.channel.send('Available commands : ```$Help, $Generate, $Info```')
        await message.delete()
        await asyncio.sleep(20)
        await t.delete()

    if any(word in m for word in Commands.Info):
        p1 = await message.channel.send('Created by Gusbell for POSN discord channel,')
        await message.delete()
        await asyncio.sleep(1)
        p2 = await message.channel.send('further information please visit https://github.com/Gusb3ll/Euler-bot')
        await asyncio.sleep(20)
        await p1.delete()
        await p2.delete()

### Real miracle begin here ###

    if m.startswith('$Generate alg 1'): #!
        t = await message.channel.send(file=discord.File(random.choice(Problems.Alg_Easy)))
        await asyncio.sleep(1)
        await message.delete()
        await asyncio.sleep(30)
        await t.delete()
    elif m.startswith('$Generate alg 2'):
        t = await message.channel.send(file=discord.File(random.choice(Problems.Alg_Normal)))
        await asyncio.sleep(1)
        await message.delete()
        await asyncio.sleep(30)
        await t.delete()
    elif m.startswith('$Generate alg 3'):
        t = await message.channel.send(file=discord.File(random.choice(Problems.Alg_Hard)))
        await asyncio.sleep(1)
        await message.delete()
        await asyncio.sleep(30)
        await t.delete()
    elif m.startswith('$Generate geo 1'): #!
        t = await message.channel.send(file=discord.File(random.choice(Problems.Geo_Easy)))
        await asyncio.sleep(1)
        await message.delete()
        await asyncio.sleep(30)
        await t.delete()
    elif m.startswith('$Generate geo 2'):
        t = await message.channel.send(file=discord.File(random.choice(Problems.Geo_Normal)))
        await asyncio.sleep(1)
        await message.delete()
        await asyncio.sleep(30)
        await t.delete()
    elif m.startswith('$Generate geo 3'):
        t = await message.channel.send(file=discord.File(random.choice(Problems.Geo_Hard)))
        await asyncio.sleep(1)
        await message.delete()
        await asyncio.sleep(30)
        await t.delete()
    elif m.startswith('$Generate com 1'): #!
        t = await message.channel.send(file=discord.File(random.choice(Problems.Com_Easy)))
        await asyncio.sleep(1)
        await message.delete()
        await asyncio.sleep(30)
        await t.delete()
    elif m.startswith('$Generate com 2'):
        t = await message.channel.send(file=discord.File(random.choice(Problems.Com_Normal)))
        await asyncio.sleep(1)
        await message.delete()
        await asyncio.sleep(30)
        await t.delete()
    elif m.startswith('$Generate com 3'):
        t = await message.channel.send(file=discord.File(random.choice(Problems.Com_Hard)))
        await asyncio.sleep(1)
        await message.delete()
        await asyncio.sleep(30)
        await t.delete()
    elif m.startswith('$Generate iq 1'): #!
        t = await message.channel.send(file=discord.File(random.choice(Problems.iq_Easy)))
        await asyncio.sleep(1)
        await message.delete()
        await asyncio.sleep(30)
        await t.delete()
    elif m.startswith('$Generate iq 2'):
        t = await message.channel.send(file=discord.File(random.choice(Problems.iq_Normal)))
        await asyncio.sleep(1)
        await message.delete()
        await asyncio.sleep(30)
        await t.delete()
    elif m.startswith('$Generate iq 3'):
        t = await message.channel.send(file=discord.File(random.choice(Problems.iq_Hard)))
        await asyncio.sleep(1)
        await message.delete()
        await asyncio.sleep(30)
        await t.delete()
    elif m.startswith('$Generate num 1'): #!
        t = await message.channel.send(file=discord.File(random.choice(Problems.num_Easy)))
        await asyncio.sleep(1)
        await message.delete()
        await asyncio.sleep(30)
        await t.delete()
    elif m.startswith('$Generate num 2'):
        t = await message.channel.send(file=discord.File(random.choice(Problems.num_Normal)))
        await asyncio.sleep(1)
        await message.delete()
        await asyncio.sleep(30)
        await t.delete()
    elif m.startswith('$Generate num 3'):
        t = await message.channel.send(file=discord.File(random.choice(Problems.num_Hard)))
        await asyncio.sleep(1)
        await message.delete()
        await asyncio.sleep(30)
        await t.delete()
    elif m.startswith('$Generate func 1'): #!
        t = await message.channel.send(file=discord.File(random.choice(Problems.func_Easy)))
        await asyncio.sleep(1)
        await message.delete()
        await asyncio.sleep(30)
        await t.delete()
    elif m.startswith('$Generate func 2'):
        t = await message.channel.send(file=discord.File(random.choice(Problems.func_Normal)))
        await asyncio.sleep(1)
        await message.delete()
        await asyncio.sleep(30)
        await t.delete()
    elif m.startswith('$Generate func 3'):
        t = await message.channel.send(file=discord.File(random.choice(Problems.func_Hard)))
        await asyncio.sleep(1)
        await message.delete()
        await asyncio.sleep(30)
        await t.delete()
    elif m.startswith('$Generate') or m.startswith('$generate'):
        p1 = await message.channel.send('Usage : ```$Generate [topic] [difficulty]```')
        await asyncio.sleep(1)
        p2 = await message.channel.send('List of topic : ```alg : Algebra, geo : Geometry, com : Combinatoric, iq : Inequality, num : Number theory, func : Functional Equation```')
        await asyncio.sleep(1)
        p3 = await message.channel.send('List of difficulty : ```1 Easy, 2 Normal , 3 Hard```')
        await asyncio.sleep(20)
        await p1.delete()
        await p2.delete()
        await p3.delete()

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

