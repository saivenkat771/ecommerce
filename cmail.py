import smtplib
from smtplib import SMTP
from email.message import EmailMessage


def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('saivenkat2783@gmail.com',"pyrm fjzh ilzl quir")
    msg=EmailMessage()
    msg['From']='saivenkat2783@gmail.com'
    msg['subject']=subject
    msg['To']=to
    msg.set_content(body)
    server.send_message(msg)
    server.quit()
