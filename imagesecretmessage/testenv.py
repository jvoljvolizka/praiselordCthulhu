a = [(1,2,3),(4,3,7),(2,9,5)]
b = a[1]
print(b)
c = []
for i in range(len(b)):
    c.append(b[i])
print(c)
c[2] = 42
c = tuple(c)
print(c)
a[1] = c
print(a)



    for i in range(len(list)):
        if list[i] != 255:
            maxsw = False
        else:
            maxsw = True
            print("oh, fuck! you nasty motherfucker ! i found a 255! ")
            print("max switch activated")
        if list[i] != 0:
            minsw = False
        else:
            maxsw = True
            print("max switch activated")
        if maxsw == False:
            newlist.append(list[i] + 1)
        elif minsw == False:
            newlist.append(list[i] - 1)
        else:
            print("error i am a penguin")
            c = input()
            exit()
    return newlist
print(listcorp(flist))