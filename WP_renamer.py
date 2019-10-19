import os
path = '/Users/amlan/Desktop/NewFolder'
files = os.listdir(path)


for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join(["wp"+str(index), '.jpg'])))
