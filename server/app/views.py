from app import app
from flask import request
from models import User
from twilio_ import send_message

@app.route('/transaction', methods=['POST'])
def do_transaction():
    sender_id = request.form['sender']
    receiver_id = request.form['receiver']
    amount = int(request.form['amount'])

    sender = User.get(sender_id)
    receiver = User.get(receiver_id)

    sender.pay(receiver_id, amount)

    send_message("You successfully paid {} to {}!".format(
        amount, receiver.first_name
    ), sender)
    send_message("You successfully received {} from {}!".format(
        amount, sender.first_name
    ), receiver)
    return 'OK!'

@app.route('/users', methods=["POST"])
def create_new_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    phone_number = request.form['phone_number']

    User.create(first_name, last_name, email, phone_number)
    return 'OK!'

@app.route('/balance')
def get_balance():
    user_id = request.args['user_id']
    user = User.get(user_id)
    return str(user.get_balance())
