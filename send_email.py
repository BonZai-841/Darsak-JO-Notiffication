#
# sender = os.environ.get("BK_EMAIL")
# password = os.environ.get("BK_EMAIL_PASSWORD")
# reciever = os.environ.get("BK_EMAIL2")
# from utils import Darsak

import smtplib, ssl
import os

class SendEmail():
    def __init__(self, email, password, reciever, message):
        self.email = email
        self.password = password
        self.reciever = reciever
        self.message = message


    def send_email(self, email, password, message, reciever):

        print("Sending Email...")

        with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ssl.create_default_context()) as server:
            # port = 465
            # context = ssl.create_default_context()
            server.login(email, password)
            server.sendmail(email, reciever, message)

        print("Email Sent Succesfully !")

#
# port = 465
#
# message = f"""\
# Subject: Python test hello user
#
# Your today lessons are
#
# your archived lessons are
#
# """
#
#
# print("Sending Email...")
# with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#     server.login("bakerjalaghef@gmail.com", "ealxzaibuzzzmtlh")
#     server.sendmail("bakerjalaghef@gmail.com", "jalaghefbaker@gmail.com", message)
# print("Email Sent Succesfully !")
