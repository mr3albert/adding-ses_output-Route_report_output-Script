#!/bin/bash

#this program adds a log output line, a .ses output line, log dir, sess dir, and a quit command in the .scmd file of each test case.
#it will check if each .scmd file in the each test case has the aforementioned three lines then add them as needed 
#Albert Liao, 6/27/2018 
import os #using os.listdir, os.path.dirname, os.path.abspath, os.chdir...

DirNArray = os.listdir() #turning all of the test case files into an array
subDirArray = os.listdir() #testcase directory name array  
address = os.path.dirname(os.path.abspath(__file__)) #address of the current directory s
subDir = ''
logBools = False
sessBools = False

for i in range(len(DirNArray)):
    logBools = False 
    sessBools = False
    subDir = os.path.join(address,DirNArray[i])#appends the current directory address with a subdirectory name to form the address for the sub directory
    if( os.path.isdir(subDir) != True): 
        continue 
    os.chdir(subDir)#change the current working directory to one of the subdir

    #listing the names of the entries in the directory to find the directory has logFile and sesFile 
    subDirArray = os.listdir()

    for i in range(len(subDirArray)):
        if subDirArray[i] == 'logFile': 
            logBools = True

        if subDirArray[i] == 'sesFile':
            sessBools = True

    if(logBools == False):
        os.makedirs('logFile')

    if(sessBools == False):
        os.makedirs('sesFile')