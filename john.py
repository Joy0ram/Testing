import requests as r
from bs4 import BeautifulSoup 

a="https://arena-breakout-infinite.fandom.com/wiki/Backpacks"
b=r.get(a)
c=BeautifulSoup(b.text,"lxml")

print(c.prettify())
#print(c.find_all(text="9"))