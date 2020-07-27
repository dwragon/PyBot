import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "An email with attachment from Python"
body = "This is an email with attachment sent from Python"
sender_email = "xaeh80064@gmail.com"
receiver_email = "xaeh80064@gmail.com"
password = ("bereg_srednii")

# Это для составного сообщения
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  # без этого не работает

# Тело мыла
message.attach(MIMEText(body, "plain"))

filename = "fileb.txt"  # Указание названия файла и дериктории

# Открытие файла
with open(filename, "rb") as attachment:

    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())


encoders.encode_base64(part)


part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Добавлнение вложения и конвертация в строку
message.attach(part)
text = message.as_string()

# Всё для конекта (указание порта там )
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)