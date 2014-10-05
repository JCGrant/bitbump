import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'app.db')

BLOCKCHAIN_GUID = "68d7ab7e-41d4-483a-89b0-faf21c678e17"
BLOCKCHAIN_PASSWORD = "comehackmebro"
BLOCKCHAIN_ADDRESS = "1NcARzKFBPUvs8MTs49dUdueEtYVyivyP2"