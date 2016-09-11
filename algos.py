import requests
import json
import datetime
from transfers import transfer, HTSECheckingAccount
from time import time
import urllib2

nessie_key = 'b5f9af5da4a243e5e82982193e355b7f'
response = requests.get('http://api.reimaginebanking.com/accounts/57d40aeee63c5995587e864f/customer?key={api}'.format(api =nessie_key ))
print(response)

# # user = user ID
# self.u = user
# # ID = order ID
# self.id = ID
# self.t = ticker
# self.s = side
# self.v = vol
# self.p = price
# self.ot = ordertype
# self.ts = tstamp
# order ~ [id, price, volume, userId, ticker, isBuy, isMarket]



# User

class User:
    def __init__(self, balance, inventory):
        self.b = balance
        self.inv = inventory

    def changeinv(self, sym, vol):
        if self.inv[sym]:
            self.inv[sym] += vol
        else:
            self.inv[sym] = vol

# Order
class Order:
    def __init__(self):
        pass
    #
    #
    # def __init__(self, user, ID, ticker, side, vol, price, ismarket, tstamp):
    #     # user = user ID
    #     self.u = user
    #     # ID = order ID
    #     self.id = ID
    #     self.t = ticker
    #     self.s = side
    #     self.v = vol
    #     self.p = price
    #     self.im = ismarket
    #     self.ts = tstamp

#retval is python dictionary
def getData(pq, all_orders, ledger, new_order):
    
    BPQ = []
    SPQ = []

    o = Order()
    print pq
    print all_orders
    print ledger
    print new_order
    o.u = new_order[6]
    o.id = new_order[0]
    o.t = new_order[3]
    o.v = new_order[2]
    o.p = new_order[1]

    o.im = new_order[5]
    o.ts = time()

    if new_order[4]:
        o.s = "buy"
        BPQ.append(o)
    else:
        o.s = "sell"
        SPQ.append(o)


    for p in pq:
        print p
        orderID = p[2] # reverse lookup for side
        myOrder = None

        isBuy = False

        for order in all_orders:
            print order
            if order[0] == orderID:
                isBuy = order[5]

        if isBuy:
            BPQ.append(p)
        else:
            SPQ.append(p)


    BPQ.sort(key=lambda entry: (-entry.p, entry.ts))
    SPQ.sort(key=lambda entry: (entry.p, entry.ts))
    BPQ, SPQ, ledger = execution(BPQ, SPQ, ledger)

    pqToRet = BPQ
    pqToRet.extend(SPQ)

    return(pqToRet, ledger)

    # This takes pq, order, and ledger queries from rest.py to calculate market data
    # pq ~ [ [id, timestamp, orderId], ..., ... ]
    # order ~ [id, price, volume, userId, ticker, isBuy, isMarket]
    # order ~ [id, price, volume, ticker, isBuy, isMarket, userId]
    # all_orders = listof (orders)
    # ledger ~ [ [id, timestamp, orderId] ...]
    # inventory: list of ( sticker, number)

    # take and parse the input data

    # aggregrate memory of pending orders


    # calculate points of interest -> Market Price

    #
    # Dequeue PG to Ledger

    # Update Price History





# def addglentry(o):
#     requests.post('heroku url', data = o, json = o)

def removepqentry(myPQ, o):
    # addglentry(o)
    myPQ.remove(o)

# o is of class order
# also need to add change to general inventory & change to user account info
def execution(buyPQ, sellPQ, ledger):

    # for i in buyPQ[:]:
    #     ticker = i.t
    #     url = "https://pennapps2k16.herokuapp.com/price_history/" + ticker
    #
    #     response = urllib2.urlopen(url)
    #     data = json.load(response)
    #
    #     marketPrice = float(data[len(data)-1][2])
    #
    #     if i.price >= marketPrice or i.im:
    #         transfer('to', '57d40d4ee63c5995587e8651', i.vol * marketPrice)
    #         transfer('from', HTSECheckingAccount, i.vol * marketPrice)
    #
    #         ledger.append(i)
    #         removepqentry(buyPQ, i)
    #
    # for i in sellPQ[:]:
    #     url = "https://pennapps2k16.herokuapp.com/price_history/" + ticker
    #
    #     response = urllib2.urlopen(url)
    #     data = json.load(response)
    #
    #     marketPrice = float(data[len(data)-1][2])
    #
    #
    #     if i.price <= marketPrice or i.im:
    #         transfer('to', HTSECheckingAccount, i.vol * marketPrice)
    #         transfer('from' '57d40d4ee63c5995587e8651', i.vol * marketPrice)
    #
    #         ledger.append(i)
    #         removepqentry(sellPQ, i)
    #
    for i in buyPQ[:]:
        for j in sellPQ[:]:
            if i.price >= j.price:
                if i.vol > j.vol:
                    transfer('to', '57d40d4ee63c5995587e8651', j.vol * j.price )
                    transfer('from', HTSECheckingAccount, j.vol*j.price)
                    i.vol -= j.vol
                    ledger.append(j)
                    removepqentry(sellPQ, j)
                else:
                    transfer('to', HTSECheckingAccount, i.vol * j.price)
                    transfer('from', '57d40d4ee63c5995587e8651', i.vol * j.price)
                    j.vol -= i.vol
                    i.vol = 0
                    ledger.append(i)
                    removepqentry(buyPQ, i)
    return buyPQ, sellPQ, ledger

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