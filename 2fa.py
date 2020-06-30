import africastalking
import os
import secrets


#initialize the sdk
username = "TruthWifiPlatform"
api_key = "#"
africastalking.initialize(username,api_key)

#recipients
recipients = ['#']


#generate random 4 digit PIN
secret_key = secrets.randbelow(10000)
message = "Your PIN is %04d" %secret_key

#initialize the service, in our case, SMS
sms = africastalking.SMS

#USE THE SERVICE
def on_finish(error, response):
    if error is not None:
        raise error
    print(response)

sms.send(message, recipients, callback=on_finish)
