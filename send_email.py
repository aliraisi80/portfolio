import smtplib
import ssl

import streamlit as st

host="smtp.gmail.com"
port=465

username="aliraisi.m.80@gmail.com"
password=""

receiver="aliraisi.m.80@gmail.com"
context=ssl.create_default_context()
message = """
Hi How are you
Bye!
"""
with smtplib.SMTP_SSL(host,port,context=context) as server:
    server.login(username,password)
    server.sendmail(username,receiver,message)