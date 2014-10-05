import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#Flask

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'app.db')


# Blockchain

WALLETS = {
    'James': {
        "guid": "XXX",
        "password": "XXX",
        "address": "XXX"
    },
    'Nic': {
        "guid": "XXX",
        "password": "XXX",
        "address": "XXX"
    },
}


# Twilio
ACCOUNT_SID = "XXX"
AUTH_TOKEN = "XXX"
TWILIO_PHONE_NUMBER = "+XXX"
