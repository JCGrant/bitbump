import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'app.db')

WALLET_1 = {
    "guid": "68d7ab7e-41d4-483a-89b0-faf21c678e17",
    "password": "comehackmebro",
    "address": "1NcARzKFBPUvs8MTs49dUdueEtYVyivyP2"
}
WALLET_2 = {
    "guid": "4bf05872-b2a2-42d3-bd60-2675dc1b997f",
    "password": "comehackmebro",
    "address": "1CapJyo8wxiK5A5TAVyYx7wtYMVJFhpDdG",
}

WALLETS = [WALLET_1, WALLET_2]