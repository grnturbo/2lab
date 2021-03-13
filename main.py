from pip._vendor import requests
import time
import random
import json


def getdata():
    return requests.get("https://blockchain.info/ru/ticker").text


d = json.loads(getdata())
user = input()
while True:
    d = json.loads(getdata())
    print("\n", user, ": ", d[user])
    temp = d[user]
    print("Стоимость покупки: ", temp["buy"])
    time.sleep(5)


