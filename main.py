import requests
import time
import json
import config
import discord
from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook


links = []
skus = []
names = []

#get SKUs, Products name from URL
with open('links.txt','r') as f:
    for line in f:
        try:
            link = line.strip()

            r = requests.get(link)
            bsObj = BeautifulSoup(r.text, 'html.parser')

            name = bsObj.find("h1", {'itemprop':'name'}).text

            sku = bsObj.find("ul", {"class":"product-numbers"}).findAll("li")[1].find("span").text

            links.append(link)
            names.append(name)
            skus.append(sku)
        except:
            continue
    links.append("https://www.dickssportinggoods.com/p/bowflex-selecttech-552-dumbbells-16bfxuslcttchdmbbslc/16bfxuslcttchdmbbslc")
    names.append("Bowflex selecttech 552")
    skus.append("11465449")

def main():
    while True:
        for i in range(len(links)):
            checkOnlineInventory(names[i], skus[i], links[i])

def checkOnlineInventory(name, sku, link):
    url = 'https://availability.dickssportinggoods.com/v1/inventoryapis/searchinventory?location=0&sku={}'.format(sku)
    tempHeaders = config.header
    tempHeaders['referer'] = link

    proxy = {
      "http": "http://108.59.14.203:13010",
      "https": "http://108.59.14.203:13010",
    }

    try:
        r = requests.get(url, timeout=6, proxies=proxy, headers=tempHeaders).json()
    except:
        checkOnlineInventory(name, sku, link)
        return

    ats = r['data']['skus'][0]['atsqty']
    message = time.strftime('%a %H:%M:%S') + " Online\nItem: {}\navailable to ship: {}\n{}".format(name, ats, link)
    print(message)

    if(int(ats) > 0):
        discord.sendDiscord(message, "online", sku, "inventory")


if __name__ == "__main__":
    main()
