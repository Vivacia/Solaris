"""
Solaris

created by Meghavarnika Budati
Version 1.0.1, November 21, 2018

To store and manage quotes.
"""

import discord
import asyncio

#user-defined
import retrievingQuotes
import Quote
import storingQuotes
import greetings

client = discord.Client()

@client.event
async def on_message(message):
      await client.change_presence(game=discord.Game(name='with Mommy.'))
      mess = message.content.lower()
      chan = message.channel
      auth = str(message.author)
      server = message.server

      storeModules = [
            storingQuotes.storeLastQuote,
            storingQuotes.storeQuote
      ]

      retrieveModules = [
            retrievingQuotes.getLastQuote,
            retrievingQuotes.getQuoteAtLine,
            retrievingQuotes.getRandomQuote
      ]

      if message.author == client.user:
        return
      
      else:
        response = greetings.greet(mess)
        if response != None and response != "":
            await client.send_typing(chan)
            await client.send_message(chan, response)
       
        response = greetings.gbye(mess)
        if response != None and response != "":
            await client.send_typing(chan)
            await client.send_message(chan, response)

        storingQuotes.tempStoreLastQuote(mess, auth)

        for function in storeModules:
            response = function(mess, chan, server, auth)
            if response != None and response != "":
                await client.send_typing(chan)
                await client.send_message(chan, response)
            break

        for function in retrieveModules:
            response = function(mess, server)
            if response != None and response != "":
                await client.send_typing(chan)
                await client.send_message(chan, response)
            break

@client.event
async def on_ready():
  print('Logged in as')
  print(client.user.name)
  print("ID: ")
  #514972065246478352
  print(client.user.id)
  print('------')

token = "you're a sneaky one :)"
client.run(token)
