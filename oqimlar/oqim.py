import json
import time
from threading import Thread
import httpx

url = httpx.get('https://jsonplaceholder.typicode.com/photos')
photo = url.json()


def oqim1():
    start1 = time.time()
    url = httpx.get('https://jsonplaceholder.typicode.com/photos')
    photo = url.json()
    with open('ymallikki.json', 'w') as f:
        json.dump(photo, f, indent=2)
    end = time.time()
    return int(end - start1)


def oqim2():
    start2 = time.time()
    url = httpx.get('https://leetcode.com/problems/3sum-closest')
    end1 = time.time()
    return int(end1 - start2)


def oqim3():
    start3 = time.time()
    url = httpx.get('https://hub.docker.com/r/tolibjon/imtihon_4_image')
    end1 = time.time()
    return int(end1 - start3)


def oqim4():
    start4 = time.time()
    url = httpx.get('https://github.com/baxodirmuroduv/baxodirmuroduv')
    end1 = time.time()
    return int(end1 - start4)


def oqim5():
    start5 = time.time()
    url = httpx.get('https://my-json-server.typicode.com/')
    end1 = time.time()
    return int(end1 - start5)


oq1 = Thread(target=oqim1)
oq2 = Thread(target=oqim2)
oq3 = Thread(target=oqim3)
oq4 = Thread(target=oqim4)
oq5 = Thread(target=oqim5)
oq1.start()
oq2.start()
oq3.start()
oq4.start()
oq5.start()

oq1.join()
oq2.join()
oq3.join()
oq4.join()
oq5.join()


a = oqim1()
print(f"{a} second")
b = oqim2()
print(f"{b} second")
u = oqim3()
print(f"{u} second")
t = oqim4()
print(f"{t} second")
o = oqim5()
print(f"{o} second")
