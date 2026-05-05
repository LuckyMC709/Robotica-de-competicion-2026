import math
def bascara (a,b,c):
    preraiz = (b*b-4*a*c)
    if (preraiz < 0):
        preraiz = preraiz*-1
        raiz = math.sqrt(preraiz)
        xuno = ((-b+raiz)/2*a)
        xdos = ((-b-raiz)/2*a)
        print (xuno,"i",xdos,"i")

    else:
        raiz = math.sqrt(preraiz)
        xuno = ((-b+raiz)/2*a)
        xdos = ((-b-raiz)/2*a)
        print (xuno,xdos)
    
a = int(input("numa "))
b = int(input("numb "))
c = int(input("numc "))

bascara(a,b,c)