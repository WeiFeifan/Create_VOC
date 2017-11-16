import os
import shutil
from createXml import create
from createTest import create_test
def listallfile():
    fileDir = "VOC2007/label/2"
    for root , dirs,files in os.walk(fileDir):
        print(root)
        print(dirs)
        print(files)

def copy_file(origpath,distpath):
    for root,dirs,files in os.walk(origpath):
        for file in files:
            if  os.path.exists(root+'/'+file):
                shutil.copy(root+'/'+file,distpath)
    
if __name__ == "__main__":
   # listallfile()
    #FOA ,create VOC folder
    if not os.path.exists('VOC'):
        os.makedirs('VOC/Annotations')
        os.makedirs('VOC/ImageSets/Main')
        os.makedirs('VOC/JPEGImages')
        os.makedirs('VOC/label')
    copy_file('Labels','VOC/label')
    copy_file('Images','VOC/JPEGImages')
    create()
#fllow the instructions of createTest.py 
    create_test(1,32,6)
    