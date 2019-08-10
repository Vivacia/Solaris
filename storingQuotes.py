"""
storingQuotes

created by Meghavarnika Budati
Version 1.0.1, November 21, 2018

Module for Solaris to store the quote of a user.
"""

import datetime
import string
import Quote

#stores Author: lastMessage
last = {}

addTriggerWords = ["add last pin", "add last quote", "solaris add last pin", "solaris add last quote", "solaris, add last pin", "solaris, add last quote"]
manualTriggerWords = ["add quote", "add pin", "solaris add quote", "solaris add pin", "solaris, add quote", "solaris, add pin"]

def tempStoreLastQuote(lastMessage, auth):
    last[auth] = lastMessage

def storeLastQuote(mess, channel, server, storedBy):
    for x in addTriggerWords:
        if mess.startswith(x):
            if "@" not in mess and "#" not in mess:
                return("Error -- please specify the person.")

            print("initial message: " + mess)
            mess = mess[mess.find(x) + x.len() + 1:]
            author = mess[mess.find("@") + 1:]
            d = datetime.datetime.now()
            date = d.strftime('%H:%M:%S, %m/%d/%Y')
            print("message after shit: " + mess)
            print("author:" + author)

            if (last[author] != None and last[author] != ""):
                quote = Quote(quote, author, date, channel, server, storedBy)
                quote.store()
                return("Added quote/pin!")

            else:
                return("Error -- please manually enter the quote. I was not here.")

def storeQuote(mess, channel, server, storedBy):
    for x in manualTriggerWords:
        if mess.startswith(x):
            x = x + " "
            quote = mess[mess.find(x):]
            author = quote[mess.find("@") + 1 : quote.find(" ")]
            quote = quote[quote.find(author) + author.length() + 1:]

            d = datetime.datetime.now()
            date = d.strftime('%H:%M:%S, %m/%d/%Y')
            newQuote = Quote(quote, author, date, channel, server, storedBy)
            newQuote.store