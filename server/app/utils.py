from app import db
from app.models import User
from random import choice, randint
from config import WALLETS

names = [
    "James",
    "David",
    "Nic",
    "Edward",
    "William",
    "Ali",
    "Evie",
    "Kate",
    "John",
    "Barry",
    "Bob",
    "Winifred",
    "Earline",
    "Pansy",
    "Veronika",
    "Michelina",
    "Tammara",
    "Takisha",
    "Annie",
    "Christal",
    "Francisca",
    "Mindy",
    "Ivy",
    "Dalila",
    "Mariano",
    "My",
    "Alexandria",
    "Jeanelle",
    "Freddie",
    "Rosenda",
    "Laurinda",
    "Tynisha",
    "Ty",
    "Melonie",
    "Sterling",
    "Alma",
    "Reuben",
    "Belva",
    "Kristen",
    "Emeline",
    "Malissa",
    "Sherman",
    "Vivien",
    "Eloise",
    "Keila",
    "Boyce",
    "Reanna",
    "Chandra",
    "Shanae",
    "Daine",
    "Yer",
    "Beatris",
    "Selena",
    "Tia",
    "Fernande",
    "Kera",
    "Brooks",
    "Pinkie",
    "Antonia",
    "Shannan",
    "Willette"
]

def create_fake_users(amount):
    global names
    for i in range(amount):
        first_name, last_name = None, None
        while first_name == last_name:
            first_name = choice(names)
            last_name = choice(names)
        email = "{}.{}@gmail.com".format(first_name.lower(), last_name.lower())
        phone_number = ''.join([str(randint(0, 9)) for i in range(11)])
        wallet = choice(wallets)

        User.create(first_name, last_name, email, phone_number,
                    wallet['guid'], wallet['password'])
        print "Created: " + first_name, last_name

def restart_db():
    db.drop_all()
    db.create_all()

def init_db():
    global names
    db.create_all()

    for wallet in WALLETS:
        first_name, last_name = None, None
        while first_name == last_name:
            first_name = choice(names)
            last_name = choice(names)
        email = "{}.{}@gmail.com".format(first_name.lower(), last_name.lower())
        phone_number = ''.join([str(randint(0, 9)) for i in range(11)])

        User.create(first_name, last_name, email, phone_number,
                    wallet['guid'], wallet['password'])