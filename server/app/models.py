from app import db
from block_chain import Wallet


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    email = db.Column(db.String(120), unique=True)
    phone_number = db.Column(db.String(16), unique=True)
    blockchain_guid = db.Column(db.String(36))
    blockchain_password = db.Column(db.String(64))

    def __init__(self, first_name, last_name, email, phone_number,
                 blockchain_guid, blockchain_password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.blockchain_guid = blockchain_guid
        self.blockchain_password = blockchain_password

    @staticmethod
    def create(first_name, last_name, email, phone_number,
               blockchain_guid=None, blockchain_password=None):
        u = User(first_name, last_name, email, phone_number,
                 blockchain_guid, blockchain_password)
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

    def pay(self, to_address, amount):
        return self.wallet.make_transaction(to_address, amount)


    def get_balance(self):
        return self.wallet.get_balance()

    def __repr__(self):
        return "User: {} {}".format(self.first_name, self.last_name)