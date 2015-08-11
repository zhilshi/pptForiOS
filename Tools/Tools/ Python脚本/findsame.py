# findsame.py
# Desription: Find same image files in the current directory 
# Usage: findsame.py [targetpath] [file]
#             targetpath: the directory to find same image files
#             file: find target file which will have the same content of this file

########################################
# CONFIG
########################################
exts = ['.png', '.bmp','gif']

gDictFile={}
gMd5File={}
gcisize=-1
gcimd5=""

########################################
# GLOBLAL
########################################
import os
import hashlib
import string
import sys

def getmd5(filePath):
    fh = open(filePath, 'rb')
    m = hashlib.md5()
    m.update(fh.read())
    md5value=m.hexdigest()
    fh.close()
    return md5value

def fileProc(filePath):
    gDictFile[filePath]=getmd5(filePath)
    return

def cmpareProc(filePath,cifile):
    filesize=os.path.getsize(filePath)
    if filesize==gcisize and gcimd5==getmd5(filePath):
        #print "add "+filePath
        gDictFile[filePath]=gcimd5
    return

def findsame():
    for key, value in gDictFile.iteritems():
        if value in gMd5File.keys():
            #print 'find exist:'+value+', '+gMd5File[value]+','+key
            gMd5File[value]=gMd5File[value]+"\n"+key
        else:
            #print "add "+key+","+value+" to gMd5File"
            gMd5File[value]=key

    print 'Find same files as below:'
    print '----------------------------------'
    for key,value in gMd5File.iteritems():
        if string.find(value,"\n")>0: 
            print key+"\n"+value+"\n"
    return


########################################
# SEARCH
########################################
from os.path import basename, isdir, join
from os import listdir
def walkIn(path,cifile):
    if(isdir(path)):
        #print prefix, basename(path)
        for item in listdir(path):
            walkIn(os.path.join(path, item),cifile)
    else:
        #print prefix, basename(path)
        if os.path.splitext(path)[1] in exts:
            if cifile=="":
                fileProc(path)
            else:
                cmpareProc(path,cifile)

########################################
# MAIN
########################################
if __name__ == '__main__':
    from os.path import isdir
    root="."
    cifile=""
    if len(sys.argv)==2: 
        root=sys.argv[1]
    if len(sys.argv)==3:
        cifile=sys.argv[2] 

    if not os.path.isdir(root):
        raise 'What you entered is not a path.'
    print 'Searching...'
    if cifile=="":
        walkIn(root,cifile)
    else:
        if os.path.isfile(cifile):
            gcisize=os.path.getsize(cifile)
            gcimd5=getmd5(cifile)
            gDictFile[cifile]=gcimd5
            walkIn(root,cifile)
    findsame();
