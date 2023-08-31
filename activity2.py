import os
import shutil

from_dir = 'C102_assets-main'
to_dir = 'output'
files = os.listdir(from_dir)

for i in files:
    name,extention = os.path.splitext(i)
    if extention == "":
        continue
    if extention in ['.txt','.pdf','.docs','.exel']:
        path1 = from_dir + '/' + i
        path2 = to_dir +'/'+ 'documents'
        path3 = to_dir +'/'+ 'documents'+ '/'+ i
        if os.path.exists(path2):
            shutil.move(path1, path3)
            print("code is running")
        else:
            print("error, documents isn't a folder")
            print("Making documents a folder")
            os.mkdir(path2)
            print("moving files")
            shutil.move(path1, path3)
