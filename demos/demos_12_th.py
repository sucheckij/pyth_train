import concurrent
import random
import threading
import asyncio
import multiprocessing
import time

import requests


def pierwsza():
    print('funkcja pierwsza')
    time.sleep(random.randint(3,10))
    print('funkcja pierwsza - koniec')

def druga():
    print('funkcja druga')
    time.sleep(random.randint(3,10))
    print('funkcja druga - koniec')

def trzecia():
    print('funkcja trzecia')
    time.sleep(random.randint(3,10))
    print('funkcja trzecia - koniec')

class UserThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.info = "Klasa z wątków"

    def showInfo(self):
        return self.info

    def run(self):
        print("start wątku w klasie")
        x = 0
        while (x<8):
            print(self.showInfo())
            time.sleep(random.randint(3,10))
            print(x)
            x += 1
        print('koniec watku Klasa')


strony = ['https://helion.pl/ksiazki/adobe-after-effects-oficjalny-podrecznik-edycja-2023-lisa-fridsma,aeop23.htm#format/d'] * 50
thread_local = threading.local()

def getSession():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session

def getPage(url):
    sesja = getSession()
    with sesja.get(url) as odp:
        print(f'dane z strony {len(odp.content)}')

def getWebPages(pages):
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        executor.map(getPage, pages)




def demo_th():
    print('\nodpalamy glowny watek')
    t1 = threading.Thread(target=pierwsza)
    t2 = threading.Thread(target=druga)
    t3 = threading.Thread(target=trzecia)
    print('zakonczenie watku glownego\n')
    t1.start()
    t2.start()
    t3.start()


    # print('klasa')
    # d = UserThread()
    # d.start()
    # print('koniec')


    start = time.time()
    getWebPages(strony)
    print(f'czas wykonania {time.time() - start} dla {len(strony)}')