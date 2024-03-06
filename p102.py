import os,shutil
print(os.getcwd())
from_dir="/Users/nityam/Downloads/C102_assets-main"
to_dir="/Users/nityam/Documents/Chikku/Python Projects"
files=os.listdir(from_dir)
print(files)
exten=[".txt",".doc",".docx",".pdf"]
for file in files:
    name,ext=os.path.splitext(file)
    if(ext in exten):
        path1=from_dir+"/"+file
        path2=to_dir+"/documents"
        path3=path2+"/"+file
        if(os.path.exists(path2)!=True):
            os.makedirs(path2)
        shutil.move(path1,path3)