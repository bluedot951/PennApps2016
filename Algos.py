import requests
import json
# nessie API key: b5f9af5da4a243e5e82982193e355b7f
url = 'something'
response = requests.get(url)
print(response)

# User

class user():
    def __init__(self, balance, inventory):
        self.b = balance
        self.inv = inventory

    def changeinv(self, sym, vol):
        self.inventory[sym] += vol
u = user(10.00, {})
u.changeinv('GTHB', 10)
print(u.inventory['GTHB'])

# Order
class order:
    def __init__(self, ticker, side, vol, price, ordertype):
        self.t = ticker
        self.s = side
        self.v = vol
        self.p = price
        self.ot = ordertype

# Central Inventory/Pool
class cinv:
    inv = []
    def changecinv(self, x):
        self.inv.append(x)

# General ledger
class GL:
    def __init__(self, oid, tstamp):
        self.oid = oid
        self.t = tstamp

    def addGLentry(self, id, stamp):
        self.oid.append(id)
        self.t.append(stamp)

# Priority Queue
class PQ:
    def __init__(self, poid, tstamp, gl):
        self.poid = poid
        self.tstamp = tstamp
        self.gl = gl
    def addPQentry(self, x, y):
        self.poid.insert(0, x)
        self.tstamp.insert(0, y)
    def removePQentry(self):
        gl.addGLentry(self.id[0], self.tstamp[0])
        self.id = self.id[1:]
        self.tstamp = self.tstamp[1:]

gl = GL()
pq = PQ(gl)


def execution(orderID, pool):
    #conditions for execution to be true
    if centralinv(orderID.t) != NULL:
        # do something
    else:
        return False
    return True

def addtoGL(aGL):
    if execution(orderID) == True:
        # blah blah blah
    elif execution(orderID) == False:
        #return order to PQ


#The price of any stock at any moment is determined by finding the price at which  the maximum number of shares will be transacted.


retval = #call functions, will be in the same data type/format as DB
request.post('url', retval)