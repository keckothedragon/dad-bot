import discord
from time import sleep
from random import randint
from getName import getName

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    print(f"Received message: {message.content}")

    response = ""

    # if message.content.startswith('$hello'):
    #     response = 'Hello!'

    containsDadJoke = False
    if "<@1077724856436654130>" in message.content:
        response = f"<@{message.author.id}>"

    elif "test" in message.content:
        response = "LMAO"

    elif " im " in message.content or message.content.startswith("im "):
        response = getName(message.content,"im")
        containsDadJoke = True
    elif "i'm" in message.content:
        response = getName(message.content,"i'm")
        containsDadJoke = True
    elif "i am" in message.content:
        response = getName(message.content,"i am")
        containsDadJoke = True
    
    
    if containsDadJoke:
        response = "Hi, " + response
        response = response.rstrip(' ') + ". I'm Dad."

    if response:
        print("Sending message: " + response)
        await message.channel.send(response)

    else:
        num = randint(1, 500)
        print(num)
        if num == 422:
            await message.channel.send("@everyone SPECIAL MODE ENGAGING... (randint(1,500) == 422)")
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
                sleep(0.5)
            await message.channel.send("SPECIAL MODE DISENGAGED")

client.run('')
# token goes here