import threading
from urllib import urlencode
from urllib2 import Request, urlopen





url = 'https://pennapps2k16.herokuapp.com/buy/' # Set destination URL here

# high frequency trading ->
goog_post_fields = {
	"vol":200,
	"price":0.20,
	"ticker":"GOOG",
	"isMarket":"TRUE",
	"userId":4
}


gthb_post_fields = {
	"vol":200,
	"price":0.20,
	"ticker":"GTHB",
	"isMarket":"TRUE",
	"userId":3
}


penn_post_fields = {
	"vol":200,
	"price":0.20,
	"ticker":"PENN",
	"isMarket":"TRUE",
	"userId":0
}

def request1():

  Request(url, urlencode(goog_post_fields).encode())
  urlopen(request1).read().decode()

def request2():
  Request(url, urlencode(penn_post_fields).encode())
  urlopen(request2).read().decode()

def request3():
  Request(url, urlencode(gthb_post_fields).encode())
  urlopen(request3).read().decode()
# request2 = Request(url, urlencode(penn_post_fields).encode())
# request3 = Request(url, urlencode(gthb_post_fields).encode())

json = urlopen(request1).read().decode()
print(json)

threading.Thread(request1).start()
threading.Thread(request2).start()
threading.Thread(request3).start()