import winapps


def get_apps():
    for app in winapps.list_installed():
        print(app)