from twilio.rest import TwilioRestClient
from config import ACCOUNT_SID, AUTH_TOKEN, TWILIO_PHONE_NUMBER

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

def send_message(message, user):
    client.messages.create(
        body=message,
        to=user.phone_number,
        from_=TWILIO_PHONE_NUMBER
    )