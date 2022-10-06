import os
import shutil
source = "C:/Users/Lenovo/Downloads"
to = "C:/Users/Lenovo/Desktop/python/c102"

listoffiles = os.listdir(source)
print(listoffiles)
for filename in listoffiles:
    name,extension = os.path.splitext(filename)
    if extension == "":
        continue
    if extension in [".gif",".png",".jpg",".jpeg",".jfif"]:
        path1 = source + "/" + filename
        path2 = to + "/" + "image_files"
        path3 = to + "/" + "image_files" + "/" + filename

        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)