import discord
from time import sleep
from random import randint
from getName import getName

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    # for debugging:
    print("Received message: " + message.content)
    if message.author == client.user:
        return
    response = ""

    # if message.content.startswith('$hello'):
    #     response = 'Hello!'

    containsDadJoke = False
    
    if "test" in message.content:
        response = "LMAO"

    # big block of if/else
    if " im " in message.content or message.content.startswith("im "):
        response = getName(message.content,"im")
        containsDadJoke = True
    elif "i'm" in message.content:
        response = getName(message.content,"i'm")
        containsDadJoke = True
    elif "Im " in message.content:
        response = getName(message.content,"Im")
        containsDadJoke = True
    elif "I'm" in message.content:
        response = getName(message.content,"I'm")
        containsDadJoke = True
    elif "IM" in message.content:
        response = getName(message.content,"IM")
        containsDadJoke = True
    elif "I'M" in message.content:
        response = getName(message.content,"I'M")
        containsDadJoke = True
    elif "i am" in message.content:
        response = getName(message.content,"i am")
        containsDadJoke = True
    elif "I am" in message.content:
        response = getName(message.content,"I am")
        containsDadJoke = True
    
    if containsDadJoke:
        response = "Hi, " + response + ". I'm Dad."

    if response:
        await message.channel.send(response)

    else:
        num = randint(1, 5000)
        print(num)
        if num == 422 or message.content == "special.py":
            await message.channel.send("SPECIAL MODE ENGAGING... (randint(1,5000) == 422)")
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
            for i in range(30):
                await message.channel.send("why")
            await message.channel.send("SPECIAL MODE DISENGAGED")

client.run()