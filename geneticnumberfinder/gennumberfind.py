import random
class main():

    def end(num,a):
        print("dalyarak: %s " %num)
        print(a)
        exit()
    def createnumber(stop):
        RanNumList = []
        for i in range(9):
            RanNumList.append(random.randint(0,stop))
            i =+ 1
        return RanNumList
    def numbercompare(numlist,magicnum,highlowlist,a):
        for i in range(len(numlist)):
            if numlist[i] < magicnum:
                highlowlist[i] = "l"
            elif numlist[i] == magicnum:
                main.end(magicnum,a)
            else :
                highlowlist[i] = "h"
        return highlowlist
    def numfind(numlist,magnum,hilolist,stop):
        newlist = [0,0,0,0,0,0,0,0,0]
        for i in range(len(hilolist)):
            if hilolist[i] == "l":
                newlist[i] = random.randint(numlist[i],stop)
            if hilolist[i] == "h":
                newlist[i] = random.randint(0,numlist[i])
        return newlist

stop = 10000000
magicnumber = input("write a number (0-%s)"%stop)
magicnumber = int(magicnumber)
hilist = ["","","","","","","","",""]

numlist = main.createnumber(stop)
a = 0
#magicnumber = 89
#print(numlist)
#print(main.numbercompare(numlist,magicnumber,hilist))
while True :
    a += 1
    hilist = main.numbercompare(numlist,magicnumber,hilist,a)
    #print(hilist)
    #break
    numlist = main.numfind(numlist,magicnumber,main.numbercompare(numlist,magicnumber,hilist,a),stop)
    #print(a)








