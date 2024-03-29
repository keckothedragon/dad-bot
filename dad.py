import discord
from time import sleep
from random import randint
from getName import getName
from dotenv import load_dotenv
import os
import constants
from kill import isDed, kill, unkill

load_dotenv()

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    unkill()
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if isDed():
        print("im ded lol")
        return

    if message.author == client.user:
        return
    
    print(f"Received message: {message.content}")

    if message.content.startswith(".say") and message.author.id in constants.authorizedUsers:
        cmd = message.content.split()[1:]
        channelId, msg = cmd[0], " ".join(cmd[1:])
        channel = await client.fetch_channel(channelId)
        print(f"Sending {msg} to #{channel.name} in {channel.guild.name}")
        await channel.send(msg)
        await message.channel.send(f"Sending {msg} to #{channel.name} in {channel.guild.name}")
        return

    if message.content.startswith(".kill") and message.author.id in constants.authorizedUsers:
        kill()
        await message.channel.send("bye")

    response = ""

    containsDadJoke = False

    if f"<@{constants.selfID}>" in message.content:
        # dad-bot is @mentioned
        response = f"<@{message.author.id}>"

    elif "test" in message.content:
        response = "LMAO"

    elif " im " in message.content.lower() or message.content.lower().startswith("im "):
        response = getName(message.content, "im")
        containsDadJoke = True
    elif " i am " in message.content.lower() or message.content.lower().startswith("i am "):
        response = getName(message.content, "i am")
        containsDadJoke = True
    elif " i'm " in message.content.lower() or message.content.lower().startswith("i'm "):
        response = getName(message.content, "i'm")
        containsDadJoke = True
    elif " i’m " in message.content.lower() or message.content.lower().startswith("i’m "):
        response = getName(message.content, "i’m")
        containsDadJoke = True
    
    if containsDadJoke:
        response = "Hi, " + response.strip() + ". I'm Dad."

    if response:
        print("Sending message: " + response)
        await message.channel.send(response)

    else:
        num = randint(1, 5000)
        if num == 422 or constants.secret in message.content:
            await message.reply("SPECIAL MODE ENGAGING... (randint(1,5000) == 422)")
            await message.channel.send("5")
            sleep(1)
            await message.channel.send("4")
            sleep(1)
            await message.channel.send("3")
            sleep(1)
            await message.channel.send("2")
            sleep(1)
            await message.channel.send("1")
            sleep(1)
            for _ in range(30):
                if isDed():
                    break
                await message.channel.send("why")
                sleep(0.5)
            await message.channel.send("SPECIAL MODE DISENGAGED")

client.run(os.getenv("TOKEN"))