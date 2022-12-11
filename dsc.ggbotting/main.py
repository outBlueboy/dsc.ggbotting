import os
import random
import requests
import threading


class stats:
    hits = 0
    failed = 0





os.system("cls")
threads = int(input("Threads --> "))
code = input("Code to bot --> ")
proxyless = input("Proxyless (Y/n) --> ")


def click():
    try:
        os.system(f"title blueboy#0999 ^| Hits: {stats.hits} ^| Failed {stats.failed}")

        proxies = None
        if proxyless.lower() == "n":
            proxys = open('proxies.txt', 'r').read().splitlines()
            proxy = random.choice(proxys)
            proxies = {'http': f'http://{proxy}', 'https':f'http://{proxy}'}


        headers = {
            'authority': 'r.dsc.gg',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.7',
            'cookie': '__cf_bm=GW6cDGxzfbUJpfHmk5MeDcAjDM04DTwCNtmzrZMsuGg-1670781184-0-AZ6CtOQENZ7IYo/jnnvIz5tdqsoRcARH+AUPFalZa85fOP3tTTwmho3PNbhMbD3y2ls50VPoEXjW1uXUJrUFT/j7ZWB1ZIMSY/uJWm8YvvUeFszP01BZbiZXe1v+eSMyARUL41i/FDj6FSG6a9senxY=; clicked_tags=dsc.gg; clicked_tags=dsc.gg',
            'dnt': '1',
            'sec-ch-ua': '^\\^Not?A_Brand^\\^;v=^\\^8^\\^, ^\\^Chromium^\\^;v=^\\^108^\\^, ^\\^Brave^\\^;v=^\\^108^\\^',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '^\\^Windows^\\^',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'sec-gpc': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        }

        r = requests.get(f"https://r.dsc.gg/{code}", headers=headers, proxies=proxies)
        if r.status_code in (200, 302):
            stats.hits += 1
        else:
            stats.failed += 1
    except:
        stats.failed += 1

os.system('cls')

print("  ______   __                 ")
print(" |   __ \ |  |.--.--.-----.   ")
print(" |   __ < |  ||  |  |  -__|   ")
print(" |______/ |__||_____|_____|   ")



print("            creds       ")
print("         blueboy#0999    ")
print("        fake vast#9163   ")



while True:
    if threading.active_count() < threads:
        for x in range(threads):
            threading.Thread(target=click).start()



            #creds#
            # fake vast#9163
            # blueboy#0999