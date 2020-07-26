# -*- coding: utf-8 -*-
import os
import smtplib
import sys
from configparser import ConfigParser
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate

# smtpObj = smtplib.SMTP('smtp.gmail.com',587)
# smtpObj.starttls()
# smtpObj.login('kurwapawa@gmail.com','bereg_srednii')
# smtpObj.sendmail("kurwapawa@gmail.com","kurwapawa@gmail.com","theme","fileB.txt"

def send_files(subject,body_text,to_emails,cc_emails,bbc_ebails,file_to_attach):
    #Отправка информации с помощью почты
    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path,"email.ini")
    header = 'Content-Disposion','attchment; filename="%s"'%file_to_attach

    #get the config
    if os.path.exists(config_path):
        cfg = ConfigParser()
        cfg.read(config_path)
    else:
        print("Config not found Exiting!")
        sys.exit(1)
    #extract server and from_addr from config
    host = cfg.get("smtp","server")
    from_addr = cfg.get("smtp","from_addr")

    #create the message
    msg = MIMEMultipart()
    msg["from"] = from_addr
    msg["Subject"] = subject
    msg["Date"] = formatdate(localtime=True)

    if body_text:
        msg.attach(MIMEText(body_text))
    msg["To"] = ','.join(to_emails)
    msg["cc"] = ','.join(cc_emails)

    attachment = MIMEBase('application',"octet-stream")

    try:
        with open(file_to_attach,"rb") as fh:
            data = fh.read()

        attachment.set_payload(data)
        encoders.encode_base64(attachment)
        attachment.add_header(*header)
        msg.attach(attachment)
    except IOError:
        msg= "error opening attachment file %s"%file_to_attach
        print(msg)
        sys.exit(1)

    emails = to_emails + cc_emails
    server = smtplib.SMTP(host)
    server.sendmail(from_addr,emails,msg.as_string())
    server.quit()

if __name__ == "__main__":
    emails = ["kurwapawa@gmail.com","kurwapawa@gmail.com"]
    cc_emails = ["kurwapawa@gmail.com"]
    bbc_emails = ["kurwapawa@gmail.com"]

    subject = "Test email with attachment from Python"
    body_text = "this email contains an attachment"
    path = "fileC.txt"
send_files(subject, body_text, emails, cc_emails, bbc_emails, path)
