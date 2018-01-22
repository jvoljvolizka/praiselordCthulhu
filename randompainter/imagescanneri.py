import hashcreate
from PIL import Image
from PIL import ImageColor
import random


filename = "alive_parrot.png"
im = Image.open(filename) #Can be many different formats.
pix = im.load()
if im.size[1] <= im.size[0]:
    yuk = im.size[1]
    gen = im.size[0]
else:
    yuk = im.size[0]
    gen = im.size[1]

#yuk = im.size[1]
#gen = im.size[0]


print(im.size) #Get the width and hight of the image for iterating over
print(pix)
pixellist = []
a = 0
b = 0
while a < yuk: #yuk
    #print(pix[b,a])
    pixellist.append(pix[b,a])
    #print(b)
    #print(a)
    b += 1
    if b == gen:#gen
        a += 1
        b = 0

#for i in range(len(pixellist)) :
f#    print(pixellist[i][1])
colorchoser = 0

randnum = random.randint(yuk,gen)
newlist = sorted(pixellist, key=lambda red: red[colorchoser])
print(pixellist)
newimg = Image.new('RGB', (yuk, gen))
newimg.putdata(newlist)
newimg.save("test42v.1.0.1-" + str(randnum) + ".png")



