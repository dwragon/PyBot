import winapps

# Сделать запись установленых приложений в файл
# Передать установленые браузеры в возврате для обработки
app_list = []


def get_apps():
    f = open('text.txt', 'w')

    for app in winapps.list_installed():
        app_list.append(app)  # все приложения записуются в апп лист
        f.write((str(app) + '\n'))#запись результата в текстовик

    f.close()


def scan_apps():
    for i in app_list:
        print(app_list)
