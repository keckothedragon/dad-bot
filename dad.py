import discord
import os
from getName import getName

# def getName(s: str, target: str):
#     if target == "im":
#         if s.startswith("im "):
#             s = s.split(target)[1]
#             print(s)
#             s = s.split()
#             print(s)
#     else:
#         s = s.split(target)[1]
#         s = s.split()
#         return s[0]

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


client.run()