a = input("sayı gir")
a = int(a)
perlist =[]
i = 1
while i < a:
    if a % i == 0:
        perlist.append(i)
    i += 1
    #print(i)
z = 0
for x in perlist:
    #print(x)
    z = z + x
if z == a:
    print(a,"is perfect!")
else:
    print("nobody likes", a)
#print(perlist)
#print(z)