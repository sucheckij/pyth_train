import asyncio
import time

import requests


def demo_async():
    # tryb asynchroniczny
    start = time.time()
    for _ in range(3):
        requests.get("http://127.0.0.1:1234/")
    print(f"Czas wykonania tradycyjnego {time.time() - start:.2f}")

    # tryb asynchroniczny
    async def getData():
        loop = asyncio.get_running_loop()
        await asyncio.gather(*[loop.run_in_executor(None, requests.get,"http://127.0.0.1:1234/") \
                               for _ in range(3)])

    start = time.time()
    asyncio.run(getData())
    print(f"Czas wykonania asynchronicznego {time.time() - start:.2f}")