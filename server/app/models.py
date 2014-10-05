from app import db
from block_chain import Wallet
from config import BLOCKCHAIN_GUID, BLOCKCHAIN_PASSWORD

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    email = db.Column(db.String(120), unique=True)
    phone_number = db.Column(db.String(16), unique=True)
    blockchain_guid = db.Column(db.String(36))
    blockchain_password = db.Column(db.String(64))

    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.blockchain_guid = BLOCKCHAIN_GUID
        self.blockchain_password = BLOCKCHAIN_PASSWORD

    @staticmethod
    def create(first_name, last_name, email, phone_number):
        u = User(first_name, last_name, email, phone_number)
        db.session.add(u)
        db.session.commit()

    @staticmethod
    def delete(user):
        db.session.delete(user)
        db.session.commit()

    @staticmethod
    def get(self, id):
        return User.query.get(id)

    @property
    def wallet(self):
        return Wallet(self.blockchain_guid, self.blockchain_password)

    def pay(self, to_address, amount):
        return self.wallet.make_transaction(to_address, amount)


    def get_balance(self):
        return self.wallet.get_balance()

    def __repr__(self):
        return "User: {} {}".format(self.first_name, self.last_name)