# -*- coding : utf-8 -*-

import os
import glob
import ast
import codecs
import re
import sys


print sys.getdefaultencoding()
reload(sys)
sys.setdefaultencoding('utf-8')

outPutFile = open("outPut.txt",'w')


#Project Dicretory
path = '/Users/jiangbanghui/Desktop/iPhone_HWVideo/VideoGo'

#search file name
pathSting = 'valuestringKey.strings'

keys = []
for line in codecs.open(pathSting,'r','utf-8'):
    if ('=' in line) and (';' in line) and ('"' in line) and ('//' not in line):
        index = line.find('=')
        key   = line[0:index]
        key = key.strip()
        keys.append(key)

print 'Please wait..'

unused_strings = []
for   string in keys:
    command = 'ag --cpp %s %s'%(string,path)
    result = os.popen(command).read();
    if len(result) < 1:
        outPutFile.write(string + '\n')
        print 'key is :' + string +'unused'

print 'Done!'


