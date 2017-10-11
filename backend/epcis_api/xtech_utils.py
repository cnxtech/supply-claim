import requests
import json

base_endpoint = 'https://wallet.staging.payxapi.com/apiv2/wallet/'
transfer_url = base_endpoint + 'transfer'
default_wallet = '51287e29-5601-454f-a0c5-0b542e868af1'


def add_wallet(public_key):
    add_wallet_url = base_endpoint + 'addwallet'
    payload = {'user_id': public_key}
    r = requests.post(add_wallet_url, payload)
    response = r.json()
    #in case there is an error
    print('Error Adding wallet: ' + str(response['error']))
    resp_data = ''
    try:
        resp_data = response['data'][0]
    except IndexError:
        print('Error: Wallet not created. Possible wallet id duplicated.')
        return 'null'
        
    print('Wallet UUID: ' + resp_data['uuid'])
    return resp_data['uuid']


def transfer(wallet_uuid, amount, reference):
    return call_transfer(wallet_uuid, default_wallet, amount, reference)


def top_up(wallet_uuid, amount):
    return call_transfer(default_wallet, wallet_uuid, amount, 'top-up wallet')


def call_transfer(wallet_uuid_from, wallet_uuid_to, amount, reference):
    payload = {'order_id': '4ap9623', 
               'from_wallet': wallet_uuid_from, 
	       'to_wallet': wallet_uuid_to,
	       'amount': amount,
	       'reference': reference}
    r = requests.post(transfer_url, payload)
    response = r.json()
    #in case there is an error
    print('Error Transfer: ' + str(response['error']))
    resp_data = response['data']
    print('TRX UUID: ' + resp_data['uuid'])
    return resp_data['uuid']
