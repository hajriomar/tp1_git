def matrice(l):
    for i in range(5):
        l.append(int(input()))
    return(l)
l1=list()
l1=matrice(l1)
l2=list()
l2=matrice(l2)
l3=list()
l3=matrice(l3)
l4=list()
l4=matrice(l4)
l5=list()
l5=matrice(l5)
print(l1)
print(l2)
print(l3)
print(l4)
print(l5)
a=0
s=0
if 1 in l1:
    a=l1.index(l1)+1
    s=2+abs(3-a)
if 1 in l2:
    a=l2.index(1)+1
    s=1+abs(3-a)
if 1 in l3:
    a=l3.index(1)+1
    s=abs(3-a)
if 1 in l4:
    a=l4.index(1)+1
    s=1+abs(3-a)
if 1 in l5:
    a=l5.index(1)+1
    s=2+abs(3-a)
print(s)