import random
def numfind(numlist, magnum, hilolist, stop):
    newlist = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(hilolist)):
        numlist[i] = a
        if hilolist[i] == "h":
            newlist[i] = random.randint(a, stop)
        if hilolist[i] == "l":

            newlist[i] = random.randint(0, a)
    return newlist
a = [1,43,7,36,98,54,87,42,667,9]
b = 645
c = ["h","h","h","h","h","h","h","l","h"]
d = 100000

print(numfind(a,b,c,d))