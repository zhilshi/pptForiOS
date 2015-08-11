# -*- coding : utf-8 -*-

import os
import glob


#Search Image Used Dicretory
path1 = '/Users/jiangbanghui/Desktop/VideoGo_1224/VideoGo'
#Project Image Dicretory
path2 = '/Users/jiangbanghui/Desktop/VideoGo_1224/VideoGo/SupportingFiles/images'

pics = []
paths = []

for root,dirs,files, in os.walk(path2):
    for file in files:
        if '.png' in file:
             pics.append(file)
             paths.append(root)

pics = [pic[:-4].replace('@2x', '') for pic in pics]

unused_pics = []
unused_paths = []

for inx ,pic in enumerate(pics):
    command = 'ag "%s" %s'%(pic,path1)
    result = os.popen(command).read()
    if len(result) < 1:
        unused_pics.append(pic)
        unused_paths.append(paths[inx])

txt_path = 'DeleteImageName.txt'
txt = '\n'.join(sorted(unused_pics))
os.system('echo "%s" > %s'%(txt,txt_path))

for index, unpic in enumerate(unused_pics):
    unpic = unpic.strip('\n')
    unpath = unused_paths[index] + '/'
    sd_pic = unpath + unpic + '.png'
    hd_pic = unpath + unpic + '@2x.png'
        
    os.system('rm "%s"'%sd_pic)
    os.system('rm "%s"'%hd_pic)

print 'delete Done!'



