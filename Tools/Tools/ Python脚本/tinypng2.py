#!/usr/bin/env python3
# coding=utf-8

# from os.path import dirname
import os,sys, getopt
from urllib.request import Request, urlopen
from base64 import b64encode
from multiprocessing import Pool

poolLimite = 10
key = "fg4M4iggxPEQYI3EMj6Owe0NiXq35Wpu"
# input = "large-input.png"
# output = "tiny-output.png"
opts, args = getopt.getopt(sys.argv[1:], "hi:o:")
input_doc_path=""
output_doc_path = ''

for op, value in opts:
    if op == "-i":
        input_doc_path = value
    elif op == "-o":
        output_doc_path = value
    elif op == "-h":
        print('''
        使用方法 python3 tinypng.py -i picDocPath -o outputDocPath
        -o 参数可以为空，默认存在picDocPath/tinypng 内
        去 https://tinypng.com/developers 申请自己的key 每key每月免费压缩500个图
        默认并发数为10 可以自己调整''')



pics  = []
absFileNames = []

def absFilesPath(dirPath):
    for root,dirs,files, in os.walk(dirPath):
        for file in files:
            if '.png' in file:
                pics.append(file)
                absFileNames.append(root+'/'+file)


#def absFilePath(fileName):
#    return os.path.join(input_doc_path,fileName)


def getTinyPng(filePath):
    print('开始'+filePath)
    request = Request("https://api.tinify.com/shrink", open(filePath, "rb").read())

    cafile = None
    # Uncomment below if you have trouble validating our SSL certificate.
    # Download cacert.pem from: http://curl.haxx.se/ca/cacert.pem
    # cafile = dirname(__file__) + "/cacert.pem"

    auth = b64encode(bytes("api:" + key, "ascii")).decode("ascii")
    request.add_header("Authorization", "Basic %s" % auth)

    response = urlopen(request, cafile = cafile)
    if response.status == 201:
      # Compression was successful, retrieve output from Location header.
      result = urlopen(response.getheader("Location"), cafile = cafile).read()

#      output = os.path.join(output_doc_path, os.path.split(filePath)[1])
      open(filePath, "wb").write(result)
      print('完成'+output)
    else:
      print('失败'+filePath)
      # Something went wrong! You can parse the JSON body for details.
      print("Compression failed")

def main():
#    fileNames = [x for x in os.listdir(input_doc_path) if os.path.splitext(x)[1]=='.png']
#    absFileNames = list(map(absFilePath, fileNames))

    os.system('input doc path "%s"'%input_doc_path)

    absFilesPath(input_doc_path)
    
#    print('****** %s ' % absFileNames)
    global output_doc_path
    if output_doc_path == '':
        output_doc_path = os.path.join(input_doc_path, 'tinypng')
#    if not os.path.exists(output_doc_path):
#        os.mkdir(output_doc_path)

    # print(input_doc_path)
    # print(absFileNames)
    

    
    
    print('Parent process %s.' % os.getpid())
    p = Pool(poolLimite)
    for fileName in absFileNames:
        p.apply_async(getTinyPng, args=(fileName,))

    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

if __name__=='__main__':
    if os.path.isdir(input_doc_path):
        main()
