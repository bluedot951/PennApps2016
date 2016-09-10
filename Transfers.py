# This is written for PYTHON 3
# Don't forget to install requests package

import requests
import json

# customerId = 'your customerId here'
apiKey = '3a0f0fa4ae6f43cc9f70854d69e0f78f'
HTSECustomerID = '57d410abe63c5995587e8655'
HTSECheckingAccount = '57d410d8e63c5995587e8657'

def transfer(fromOrTo, checkingAccount, amount):
	if(fromOrTo == "FROM"):
		url = "http://api.reimaginebanking.com/accounts/{}/transfers?key=3a0f0fa4ae6f43cc9f70854d69e0f78f".format(HTSECheckingAccount)
		payload = {
			  "medium": "balance",
			  "payee_id": checkingAccount,
			  "amount": amount,
			  "transaction_date": "2016-09-10",
			  "description": "test"
			}
		response = requests.post(url,data=json.dumps(payload),headers={'content-type': 'application/json'})
		return response.status_code == 201
	if(fromOrTo == "TO"):
		url = "http://api.reimaginebanking.com/accounts/{}/transfers?key=3a0f0fa4ae6f43cc9f70854d69e0f78f".format(checkingAccount)
		payload = {
			  "medium": "balance",
			  "payee_id": HTSECheckingAccount,
			  "amount": amount,
			  "transaction_date": "2016-09-10",
			  "description": "test"
			}
		response = requests.post(url,data=json.dumps(payload),headers={'content-type': 'application/json'})
		return response.status_code == 201
	else:
		return False

print transfer("TO", "57d40d4ee63c5995587e8651", 15)

# url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customerId,apiKey)
# payload = {
#   "type": "Savings",
#   "nickname": "test",
#   "rewards": 10000,
#   "balance": 10000,	
# }
# # Create a Savings Account
# response = requests.post( 
# 	url, 
# 	data=json.dumps(payload),
# 	headers={'content-type':'application/json'},
# 	)

# if response.status_code == 201:
# 	print('account created')
