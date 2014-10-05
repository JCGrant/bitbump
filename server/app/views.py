# -*- coding: utf-8 -*-
import os
from app import app
from flask import request
from models import User
from twilio_ import send_message
import sendgrid
sg = sendgrid.SendGridClient(os.environ['SGUSER'], os.environ['SGPW'])

def send_email(text, receiver):
    message = sendgrid.Mail()
    message.add_to('%s %s <%s>' % (receiver.first_name, receiver.last_name, receiver.email))
    message.set_subject('Payment Confirmation!')
    message.set_text(text)
    message.set_from('BitBump <info@bit-bump.me>')
    status, msg = sg.send(message)

@app.route('/transaction', methods=['POST'])
def do_transaction():
    sender_id = request.form['sender']
    receiver_id = request.form['receiver']
    amount = int(request.form['amount'])

    sender = User.get(sender_id)
    receiver = User.get(receiver_id)

    response = sender.pay(receiver, amount)
    if 'error' in response:
        return response.get('error'), 400

    amount_in_pounds = amount * 209.5 / 100000000

    send_message("You successfully paid £{:.2f} to {}!".format(
        amount_in_pounds, receiver.first_name
    ), sender)
    
    #send_email("You successfully paid £{:.2f} to {}!".format(
    #    amount_in_pounds, receiver.first_name
    #), sender)

    send_message("You successfully received £{:.2f} from {}!".format(
        amount_in_pounds, sender.first_name
    ), receiver)

    #send_email("You successfully received £{:.2f} from {}!".format(
    #    amount_in_pounds, sender.first_name
    #), receiver)

    return 'OK!', 200

@app.route('/users', methods=["POST"])
def create_new_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    phone_number = request.form['phone_number']

    User.create(first_name, last_name, email, phone_number)
    return 'OK!', 200

@app.route('/balance')
def get_balance():
    user_id = request.args['user_id']
    user = User.get(user_id)
    return str(user.get_balance()), 200
