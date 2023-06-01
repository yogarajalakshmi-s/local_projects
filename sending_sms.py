from twilio.rest import Client
import os

# https://www.twilio.com/docs/sms/send-messages
client = Client(os.environ.get('ACCOUNT_SID'), os.environ.get('AUTH_TOKEN'))
message = client.messages \
    .create(
        body="Hello!",
        from_=os.environ.get('FROM_NUMBER'),
        to=os.environ.get('TO_NUMBER')
    )

print(message.sid)
