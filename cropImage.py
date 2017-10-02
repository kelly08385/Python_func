import os,sys
from PIL import Image

def crop(x,y):
    img2 = img.crop((x,y,x+800,y+400))
    return img2

if __name__ == "__main__":
    path = 'wineScene/'
    dis_path = "wineScene_crop/"
    for files in os.listdir(path):
        img = Image.open(path + files)
        width,height = img.size
        index = 0
        print "width,height = [{},{}]".format(width,height)
        for x in range(width/800):
            for y in range(height/400):
                index = index + 1
                print "[x,y] = [{},{}]".format(x*800,y*400)
                temp_x,temp_y = x*800,y*400
                cropImg = crop(temp_x,temp_y)
                cropImg.save(dis_path + files[:-4] + "-" + str(index) +".jpg")
