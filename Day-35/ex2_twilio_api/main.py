from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)

message = client.messages.create(
  body="It's goin to rain today. Remember to bring an umbrela",
  from_=os.environ.get("FROM_PHONE"),
  to=os.environ.get("TO_PHONE")
)

print(message.sid)
