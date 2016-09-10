import requests
import json
import datetime

nessie_key = 'b5f9af5da4a243e5e82982193e355b7f'
url = 'something endpoint'
response = requests.get('http://api.reimaginebanking.com/accounts/57d40aeee63c5995587e864f/customer?key={api}'.format(api =nessie_key ))
response2 = requests.get(url)
retval = json.loads(response2.text)
print(response)
print(response2)

#retval is python dictionary

# Central Inventory/Pool is a dict of ticker: amount
centralinv = {}


# GL is a list of listof(class order, tstamp)
GL = []

# PQ is a list of listof(class order, tstamp)
PQ = []

# User

class user:
    def __init__(self, balance, inventory):
        self.b = balance
        self.inv = inventory

    def changeinv(self, sym, vol):
        if self.inv[sym]:
            self.inv[sym] += vol
        else:
            self.inv[sym] = vol


u = user(10.00, {})
u.changeinv('GTHB', 10)
print(u.inv['GTHB'])


# Order
class order:
    def __init__(self, ID, ticker, side, vol, price, ordertype, tstamp):
        self.id = ID
        self.t = ticker
        self.s = side
        self.v = vol
        self.p = price
        self.ot = ordertype
        self.ts = tstamp


def addglentry(o):
    GL.append([o])

def addpqentry(o):
    PQ.append([o])

def removepqentry(o):
    addglentry(o)
    PQ.pop([o])

# o is of class order
def execution(o):
    if o.ot == "market" & o.s == "buy":
        addglentry(o)


PQ.sort(key=lambda entry: entry[1])
#The price of any stock at any moment is determined by finding the price at which  the maximum number of shares will be transacted.


retval = #call functions, will be in the same data type/format as DB
request.post('url', retval)