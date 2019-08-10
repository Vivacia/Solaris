"""
retrievingQuotes

created by Meghavarnika Budati
Version 1.0.1, November 21, 2018

Module for Solaris to get quotes.
"""

import random
import string

getLastTriggerWords = ["get last pin", "get last quote", " solaris get last pin", " solaris get last quote", " solaris, get last pin", " solaris, get last quote"]
lineTriggerWords = ["get pin", "get quote", "solaris get pin", "solaris get quote", "solaris, get pin", "solaris, get quote"]
getRandomTriggerWords = ["get random pin", "get random quote", "solaris get random pin", "solaris get random quote", "solaris, get random pin", "solaris, get random quote"]


def getLastQuote(mess, server):
    fileName = str(server) + ".txt"
    last = ""
    
    for x in getLastTriggerWords:
        if mess.startswith(x):
            with open(fileName, "rb") as f:
                first = f.readline()        # Read the first line.
                f.seek(-2, os.SEEK_END)     # Jump to the second last byte.
                while f.read(1) != b"\n":   # Until EOL is found...
                    f.seek(-2, os.SEEK_CUR) # ...jump back the read byte plus one more.
            last = f.readline()
            return(last)
            
def getQuoteAtLine(mess, server):
    fileName = server + ".txt"
    for x in lineTriggerWords:
        if mess.startswith(x):
            mess = mess[mess.find(x) + 1:]
            if " " in mess:
                mess = mess[:mess.find(" ")]

            reqLine = int(mess)

            with open(fileName) as fp:
                for i, line in enumerate(fp):
                    if i == reqLine:
                        quote = fp.readline()
                        return(quote)

def getRandomQuote(mess, server):
    fileName = server + ".txt"
    for x in randomTriggerWords:
        if mess.startswith(x):
            last = ""
            with open(fileName, "rb") as f:
                first = f.readline()
                f.seek(-2, os.SEEK_END)
                while f.read(1) != b"\n":
                    f.seek(-2, os.SEEK_CUR)
                last = f.readline()
            last = last[0 : find(". <")]
            id = int(last)
            x = random.choice(id)

            reqLine = int(mess)

            with open(fileName) as fp:
                for i, line in enumerate(fp):
                    if i == reqLine:
                        quote = fp.readline()
                        return(quote)