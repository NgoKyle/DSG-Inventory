import requests
import time
from discord_webhook import DiscordWebhook


while True:
    r = requests.get("https://www.dickssportinggoods.com/p/bowflex-selecttech-552-dumbbells-16bfxuslcttchdmbbslc/16bfxuslcttchdmbbslc")
    print(r)
    if r.ok:
        webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/697503879457407018/TCpMS4Z-L-yMcQ_xtFF8tEmOdrppm6x8hUFdrrYPC2QR1x4qwsa9cLDS2Qfmnb5PtFau',content='bowflex site is up')
        webhook.execute()
    time.sleep(5)
