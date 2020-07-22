import winapps
# Сделать запись установленых приложений в файл
# Передать установленые браузеры в возврате для обработки
app_list=[]
def get_apps():

    for app in winapps.list_installed():
        app_list.append(str(app)) #все приложения записуются в апп лист
    #     print(app)

#def scan_apps():




