import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


login = 'pythonsendbot9@gmail.com'
address_list = ['address1@gmail.com', 'address2@gmail.com']
password = 'xxxxxxxx'
msg = MIMEMultipart()
msg['Subject'] = 'Topic'
msg['From'] = 'myaddress@gmail.com'
body = 'Test message!'
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(login, password)
server.sendmail(login, address_list, msg.as_string())
server.quit()
