#!/usr/bin/env python
import os
import random
def create_test(start,end,test):
    allNum = end-start+1
    b_list = range(start,end)
    blist_webId = random.sample(b_list, test)
    blist_webId = sorted(blist_webId) 
    allFile = []
    testFile = open('VOC/ImageSets/Main/test.txt', 'w')
    trainFile = open('VOC/ImageSets/Main/trainval.txt', 'w')
    for i in range(allNum):
        allFile.append(i+1)
    for test in blist_webId:
        allFile.remove(test)
        testFile.write(str(test) + '\n')   
    for train in allFile:
        trainFile.write(str(train) + '\n')
    testFile.close()
    trainFile.close()

if __name__ == "__main__":
    pass
