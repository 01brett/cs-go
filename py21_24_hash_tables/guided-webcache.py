import urllib.request
from datetime import datetime


class CacheEntry:
    def __init__(self, data):
        self.data = data
        self.timestamp = datetime.now().timestamp()


cache = {}

CACHE_TIMEOUT = 10

while True:
    url = input("Enter a URL: ")

    if url == "q":
        break
    elif url == "":
        continue

    cur_time = datetime.now().timestamp()
    print("\ncur_time:", cur_time)

    if url not in cache or cur_time - cache[url].timestamp > CACHE_TIMEOUT:
        res = urllib.request.urlopen("https://" + url)
        data = res.read()
        cache[url] = CacheEntry(data)
        res.close()
        print("\nCache Miss\n")
    else:
        print("\nCache Hit\n")

    doc = cache[url].data[:80]
    print(doc)
