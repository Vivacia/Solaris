"""
Quote

created by Meghavarnika Budati
Version 1.0.1, November 21, 2018

Class for Solaris to manage quotes.
"""

class Quote:
    id = 0

    def __init__(quote, author, date, channel, server, storedBy):
        self.quote = quote
        self.author = author
        self.date = date
        self.channel = channel
        self.storedBy = storedBy

        fileName = server + ".txt" 
        if content is None:
            id = 0
        else:
            last = ""
            with open(fileName, "rb") as f:
                first = f.readline()        # Read the first line.
                f.seek(-2, os.SEEK_END)     # Jump to the second last byte.
                while f.read(1) != b"\n":   # Until EOL is found...
                    f.seek(-2, os.SEEK_CUR) # ...jump back the read byte plus one more.
                last = f.readline()         # Read last line.
            last = last[:find(". <")]
            id = int(last) + 1

    def store():
        fileName = server + ".txt" 
        file = open(fileName, "a")
        textStored = ("%d. <%s> %s -- added by %s in #%s, %s.", id, author, quote, storedBy, channel, date)
        file = open(fileName, "w")
        file.write(textStored)
        file.close()