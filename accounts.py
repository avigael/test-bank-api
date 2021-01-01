# -*- coding: utf-8 -*-
import json
from random import randint

with open('accounts.json') as acc_data:
    data = json.load(acc_data)
SIZE = len(data)

def get_accounts(amount):
    accounts = []
    for i in range(0, amount):
        acc = randint(1, SIZE)
        accounts.append(data[acc])
    return accounts