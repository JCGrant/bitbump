from app import app
from flask import request
from models import User

@app.route('/transaction/', methods=['POST'])
def do_transaction():
    sender_id = request.form['sender']
    receiver_id = request.form['receiver']
    amount = int(request.form['amount'])
    password = request.form['password']

    user = User.get(sender_id)
    user.pay(receiver_id, amount)
    return 'success'


@app.route('/users/', methods=["POST"])
def create_new_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    phone_number = request.form['phone_number']

    User.create(first_name, last_name, email, phone_number)
    return 'success'

@app.route('/balance/')
def get_balance():
    user_id = request.form['user_id']
    user = User.get(user_id)
    return user.get_balance()