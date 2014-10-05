import requests

class Wallet:

    base_url = "https://blockchain.info/merchant"

    def __init__(self, guid, password, second_password=None):
        self.guid = guid
        self.main_password = password
        self.second_password = second_password

    def get_json_reponse(self, method, data={}):
        data['password'] = self.main_password
        if self.second_password:
            data['second_password'] = self.second_password
        r = requests.get(Wallet.base_url + '/' + self.guid + '/' + method, params=data)
        json = r.json()
        return json

    def get_balance(self):
        json = self.get_json_reponse('balance')
        return json['balance']

    def make_transaction(self, to_address, amount, from_address=None, fee=None, note=None):
        data = {
            "address": to_address,
            "amount": amount
        }

        if from_address:
            data['from'] = from_address
        if fee:
            data['fee'] = fee
        if note:
            data['note'] = note

        json = self.get_json_reponse('payment', data)
        return json