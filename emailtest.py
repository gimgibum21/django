import smtplib

gmail_user = 'gimgibum21@gmail.com'
gmail_password = 'rbfpykfwlfenlmre'
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
except:
    print('hello world')