# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

#######################################COPIED_FROM_TWILIO_API#############################

# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ.get('twilio_account_sid')
auth_token = os.environ.get('twilio_auth_token')
# messaging_sid = os.environ.get('messaging_service_sid') ????
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                    body="This is your audition reminder from followSpot.",
                    from_='(+16505501808',
                    to='+16507735818'
                )

print(message.sid)
