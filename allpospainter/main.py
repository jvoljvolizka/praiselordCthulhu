import math
from PIL import Image


class maint():




    def binconvert(list):
        a = []
        for i in list:
            #print(i)
            if int(i) == 1:
                a.append((255,255,255))
            else:
                a.append((0,0,0))
        return a

    def bincount(num):
        counter = int(num)
        for i in range(0,counter):
            a = '{0:b}'.format(i)
            b = a.zfill(int(math.sqrt(counter)))
            b = list(b)
            n = maint
            c = n.binconvert(b)
            print(c)
            img = Image.new('RGB', (2, 2))
            img.putdata(c)
            img.save("test" + str(i) + ".bmp")



maint.bincount(2 ** 4)