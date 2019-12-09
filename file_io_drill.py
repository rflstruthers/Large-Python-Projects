##Python: 3.7.4
##Author: Reilly Struthers
##Purpose: Python course file I/O drill.

import os
import time

path = 'C:\\Users\\User0\\Desktop\\The Tech Academy\\Python\\DrillStep100'
files = os.listdir(path) # list of files in 'DrillStep100 directory'

def get_txt():
    txtFiles = {} 
    for names in files:
        if names.endswith(".txt"):
            txtPath = os.path.join(path,names) # get absolute path of each txt file
            t = os.path.getmtime(txtPath) # get time-stamp
            tStamp = modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t)) # change time-stamp format
            txtFiles.update({names : tStamp}) # add file name and corresponding time-stamp to dictionary

    print('The following are all the text files and their \ncorresponding time-stamps in the DrillStep100 \ndirectory: \n')
    
    for i in txtFiles.items(): # print txtFiles dictionary with each key-value pair on a new line
        print (i[0],':',i[1])
    
    
            

if __name__ == '__main__':
    get_txt()

