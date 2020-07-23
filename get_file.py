import os
print(os.name)
def file_search():
    for root, directories, files in os.walk(r"E:"):
        print(root)
        for directory in directories:
            print(directory)
        for file in files:
            print(file)