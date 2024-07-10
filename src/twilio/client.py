from twilio.rest import Client
from decouple import config


def get_client():
  account_sid = config("TWILIO_ACCOUNT_SID")
  auth_token = config("TWILIO_AUTH_TOKEN")

  return Client(account_sid, auth_token)
