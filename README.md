# Url_Shortener


import pyshorteners

link=input("enter your link:")

shortener=pyshorteners.Shortener()

y = shortener.tinyurl.short(link)

print(y) 
