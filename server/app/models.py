from app import db
from block_chain import Wallet


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True)
    phone_number = db.Column(db.String(16), unique=True)
    blockchain_guid = db.Column(db.String(36), nullable=False)
    blockchain_password = db.Column(db.String(64), nullable=False)
    blockchain_address = db.Column(db.String(100), nullable=False)

    def __init__(self, first_name, last_name, email, phone_number,
                 blockchain_guid, blockchain_password, blockchain_address):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.blockchain_guid = blockchain_guid
        self.blockchain_password = blockchain_password
        self.blockchain_address = blockchain_address

    @staticmethod
    def create(first_name, last_name, email, phone_number,
               blockchain_guid=None, blockchain_password=None, blockchain_address):
        u = User(first_name, last_name, email, phone_number,
                 blockchain_guid, blockchain_password, blockchain_address)
        db.session.add(u)
        db.session.commit()

    @staticmethod
    def delete(user):
        db.session.delete(user)
        db.session.commit()

    @staticmethod
    def get(id):
        return User.query.get(id)

    def update(self, first_name=None, last_name=None, email=None, phone_number=None):
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if email:
            self.email = email
        if phone_number:
            self.phone_number = phone_number
        db.session.commit()

    @property
    def wallet(self):
        return Wallet(self.blockchain_guid, self.blockchain_password)

    def pay(self, receiver, amount):
        return self.wallet.make_transaction(receiver.blockchain_address, amount)


    def get_balance(self):
        return self.wallet.get_balance()

    def __repr__(self):
        return "User: {} {}".format(self.first_name, self.last_name)
