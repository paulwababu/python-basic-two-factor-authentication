
import africastalking
import os
import secrets

#initialize the sdk
username = "TruthWifiPlatform"
api_key = "8a05856fb144470a0a303c65cc48906561548daf81e1bc9310b8ff4846c2cbf9"
africastalking.initialize(username,api_key)

#recipients
recipients = ['254797584194']

#generate random 4 digit PIN
secret_key = secrets.randbelow(10000)
message = ("%04d") %secret_key
code = message

#initialize the service, in our case, SMS
sms = africastalking.SMS

#USE THE SERVICE
def on_finish(error, response):
    if error is not None:
        raise error
    print(response)

sms.send(message, recipients, callback=on_finish)
