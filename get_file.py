import os
import string

print(os.name)
def file_search():
    # for i in range(ord('a'), ord('z') + 1):
    #     print(i)
    # Хочу сделать автоматический перебор дисков включая флешки там и всякое такие

    ch_files = open('file.txt', 'w')
    for root, directories, files in os.walk(r"E:"):
        #print(root)
        ch_files.write(root+'\n')

        for directory in directories:
           # print(directory)
            ch_files.write(directory+'\n')

        for file in files:
            #print(file)
            ch_files.write(file+'\n')
    ch_files.close()
def file_dowload():
