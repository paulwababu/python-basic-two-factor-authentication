#generate a random 4 digit number
#initialize and use the SMS api from africa's talking
#connect to gcloud remote mysql database
#send 2fa code generated to the database named verify on table called fa and column named address 

import africastalking
import os
import secrets
import mysql.connector

#variable for connecting to remote database
mydb = mysql.connector.connect(
    host = "35.232.88.217",
    user = "test_remote",
    password = "test_remote",
    database = "verify"
)

mycursor = mydb.cursor()


#initialize the sdk
username = "#"
api_key = "#"
africastalking.initialize(username,api_key)

#recipients
recipients = ['+254796919703']

#generate random 4 digit PIN
secret_key = secrets.randbelow(10000)
message = ("%04d") %secret_key
code = message

sql=("INSERT INTO fa (address) VALUES ({})".format(code))

mycursor.execute(sql, code)

mydb.commit()

#initialize the service, in our case, SMS
sms = africastalking.SMS

#USE THE SERVICE
def on_finish(error, response):
    if error is not None:
        raise error
    print(response)

sms.send(message, recipients, callback=on_finish)
