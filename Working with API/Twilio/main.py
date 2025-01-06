from twilio.rest import Client

account_sid = '[AccSID]'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='[NewPhoneNo]',
  body='This is my first message thru twilio',
  to='[ToPhoneNumber]'
)

print(message.sid)