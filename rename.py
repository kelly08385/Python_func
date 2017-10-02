import os,sys

#path = '../../Downloads/picture/bottle/'
dir = 'YCH'
path = '../../Documents/data_face/'+ dir + '/'

i = 1

for files in os.listdir(path):
    print path + files
    os.rename(path+files ,path + dir +'-' + str(i) + '.png')
    i = i+1