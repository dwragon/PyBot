import os
from ctypes import windll

print()


def file_search():
    ch_sys = open('sys.txt', 'w')
    ch_sys.write(str(os.environ) + '\n')  # запись всей информации о пк
    ch_sys.write(os.name + '\n')
    ch_sys.close()
    ################################
    # мне этот кусок не нравится(я не люблю цикл вайл), но по другому я не могу сделать
    ################################
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    letter = ord('A')
    while bitmask > 0:
        if bitmask & 1:
            drives.append(chr(letter))
        bitmask >>= 1
        letter += 1
    ################################
    for i in drives:
        ch_files = open('file' + i + '.txt', mode='w', encoding='utf-8')
        for root, directories, files in os.walk(r"" + i + ":"):
            # print(root)
            ch_files.write(root + '\n')

            for directory in directories:
                # print(directory)
                ch_files.write(directory + '\n')

            for file in files:
                # print(file)
                ch_files.write(file + '\n')
    ch_files.close()

# def file_dowload():
