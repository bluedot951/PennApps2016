import requests
import json
import datetime
import Transfers

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

# BPQ is a list of listof(class order, tstamp) - BUY orders only
BPQ = []

# SPQ is a list of listof(class, order, tstamp) - SELL orders only
SPQ = []

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
    def __init__(self, user, ID, ticker, side, vol, price, ordertype, tstamp):
        # user = user ID
        self.u = user
        # ID = order ID
        self.id = ID
        self.t = ticker
        self.s = side
        self.v = vol
        self.p = price
        self.ot = ordertype
        self.ts = tstamp


def addglentry(o):
    requests.post('heroku url', data = o, json = o)

def removepqentry(myPQ, o):
    addglentry(o)
    myPQ.remove(o)

# o is of class order
def execution(buyPQ, sellPQ):
    for i in buyPQ[:]:
        for j in sellPQ[:]:
            if i.price >= j.price:
                if i.vol > j.vol:
                    transfer('to', '57d40d4ee63c5995587e8651', j.vol * j.price )
                    transfer('from', HTSECheckingAccount, j.vol*j.price)
                    i.vol -= j.vol
                    removepqentry(sellPQ, j)
                else:
                    transfer('to', HTSECheckingAccount, i.vol * j.price)
                    transfer('from' '57d40d4ee63c5995587e8651', i.vol * j.price)
                    j.vol -= i.vol
                    i.vol = 0
                    removepqentry(buyPQ, i)

def addBuyOrder(o, buyPQ):
    price = o.p
    ind  = 0
    while (ind < len(buyPQ) and price >= buyPQ[ind]):
        ind += 1
    buyPQ[ind:ind] = [o]

def addSellOrder(o, buyPQ):
    price = o.p
    ind = 0
    while (ind < len(buyPQ) and price <= buyPQ[ind]):
        ind += 1
    buyPQ[ind:ind] = [o]

BPQ.sort(key=lambda entry: (-entry.p, entry.ts))
SPQ.sort(key=lambda entry: (entry.p, entry.ts))

retval = #call functions, will be in the same data type/format as DB
request.post('url', retval)