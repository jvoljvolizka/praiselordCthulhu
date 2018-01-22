import PIL
from PIL import Image

f = open("harry.txt" , "r+" , encoding="utf-8")

filetext = f.read()
print(len(filetext))

#print(c)
def createlist(file):
    list = []
    for i in range(len(file)):
        list.append(file[i])
    return list
textlist = createlist(filetext)

asciilist = []
for i in range(len(textlist)):
    asciilist.append(ord(textlist[i]))
print(len(textlist))
#print(asciilist)

pixellist = []

for i in range(0,len(asciilist),3):
    if i == len(textlist)-2:
        break
    pixellist.append((asciilist[i],asciilist[i+1],asciilist[i+2]))

print(len(pixellist))

newimg = Image.new('RGB', (400, 400))
newimg.putdata(pixellist)
newimg.save("harry.bmp")




print()
