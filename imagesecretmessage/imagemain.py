from PIL import Image
import qrcode

qr = qrcode.QRCode( #qr kod oluştur
    version=10,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
     box_size=1,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image()
img.save("qr.png")

filename = "firstimage.jpg"
im = Image.open(filename) #Can be many different formats.
pix = im.load()
imx = im.convert("RGB")
x = imx.getpixel((0,0))
print(x)
print(pix)
def imglistcreate(img): #pixel listesi
    rgb_im = img.convert('RGB')
    #r, g, b = rgb_im.getpixel((1, 999))
    #print(r, g, b)
    #r += 1
    #print(r)
    #tullist = []

    #tul = (r,g,b)
    #tullist.append(tul)
    #print(tul)
    #print(tullist)
    print(img.size)
    switch = True
    bluelist = []
    gen = 0
    yuk = 0
    while switch == True:
        if gen == img.size[0]-1 and yuk == img.size[1]-1:
            switch = False
        elif gen == img.size[0]:
            gen = 0
            yuk += 1


        x = rgb_im.getpixel((gen,yuk))
        bluelist.append(x)
        gen += 1
    return bluelist

mainlist = imglistcreate(im)

def qrlist(list):#yer değiştirecek pixel listesi -mavi-
    qrlis = []
    doblist =[]
    a = 0
    b = 1
    mul = 3
    for i in range(65*65):
        qrlis.append(list[a][2])
        a += mul
        doblist.append(list[b][2])
        b += mul
    return qrlis , doblist

flist,seclist = qrlist(mainlist)
print(flist)
print(seclist)

def listcorp(list):#listeyi -1 or +1
    maxsw = False
    minsw = False
    newlist = []
    for i in range(len(list)):
        if list[i] == 255:
            maxsw = True
            print("maxsw true")
            break
        else:
            maxsw = False
        if list[i] == 0:
            minsw = True
            print("minsw true")
            break
        else:
            minsw = False

    for i in range(len(list)):

        if maxsw == False:
            newlist.append(list[i] + 1)
        elif minsw == False:
            newlist.append(list[i] - 1)
        else:
            print("error i am a penguin")# bunu nasıl düzelteceğime dair hiçbir fikrim yok. ivit.
            c = input()
            exit()
    if maxsw == True or (maxsw == False and maxsw == False):
        masterswitch = True
    return newlist , masterswitch

newchangelist , changeswitch = listcorp(seclist)
print(newchangelist)
def listadd(list,blist):
    newlist = list
    a = 0
    debpointt = False
    for i in range(0,len(newlist),3):

        b = []
        debpoint = newlist[i]
        if debpointt == True:
            return newlist
            break
        debpointtt = blist[a]
        #if i == 0:
        #    pointer = 0
        #else:
        #    pointer = i+3
        b.append(newlist[i][0])
        b.append(newlist[i][1])
        if a == (65*65)-1:
            debpointt = True
        b.append(blist[a])
        b = tuple(b)
        newlist[i] = b

        a += 1
    return newlist
newblanklist = listadd(mainlist,newchangelist)
debugstop = True
qrim = Image.open("qr.png")
qrpixlist = imglistcreate(qrim)
print(len(qrpixlist))
print(qrpixlist)
def qrlistcreator(list):
    newqrlis = []
    for i in range(len(list)):
        if list[i][0] == 255:
            newqrlis.append(1)
        else:
            newqrlis.append(0)
    return newqrlis

print(qrlistcreator(qrpixlist))
def qrint(switch,blankpixlist,qrlastpixlist):
    lastblanklist = []
    if switch == True:
        for i in range(len(blankpixlist)):
            lastblanklist.append(blankpixlist[i] - qrlastpixlist[i])
    else:
        for i in range(len(blankpixlist)):
            lastblanklist.append(blankpixlist[i] - qrlastpixlist[i])
    return lastblanklist







#print(newblanklist)