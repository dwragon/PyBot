import  smtplib


smtpObj = smtplib.SMTP('smtp.yandex.ru',587)
smtpObj.starttls()
smtpObj.login('beliy.ian@yandex.ru','bereg_levii')
smtpObj.sendmail("beliy.ian@yandex.ru","kurwapawa@gmail.com","mao")
