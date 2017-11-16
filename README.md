# Create_VOC
=============
A simple tool for creating VOC dataset,implemented with Python cv2.

# Data Organization
-------------
|
|--createVOC.py      ##source code for creating  VOC dataset
|
|--createTest.py     ##source code for creating  test.txt and trainval.txt
|
|--createXml.py      ##source code for creating Annotations/**.xml 
|
|--Labels/           ##directory containing the  labels
|
|--Images/           ##directory containing the images

# Environment
-------------
-python3 
-python cv2  shutil  itertools

# Run
-------------
python createVOC.py

# Usage
-------------
0. The current tool requires that images in the directory Images/  and labels in the directory Labels/  .You will need to modify the createVOC.py in rows 26 and 27, if you want to create VOC dataset from the images and labels elsewhere.

1. The test.txt and trainval.txt will be saved in the directory ImageSets/Main/ ,if you want to create your test.txt and trainval.txt ,you need to modify the createVOC.py in rows 30. The 1st parameter is the start id, 2nd parameter is the total images ,3rd parameter is the total test images.

2.After runing createVOC.py,we will get the VOC dataset.

# VOC 
------------
|
|--Annotations/        ##directory containing xml
|
|--ImageSets/Main      ##directory containing trainval.txt and test.txt
|
|--JPEGImages          ##directory containing images
|
|--label               ##directory contain labels