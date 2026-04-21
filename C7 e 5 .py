i = 0 
pos = 0
neg = 0
cer = 0
while i < 5:
    j =  int(input("ihbgsdkj"))
    if (j<0):
        print (j,"negativo")
        neg = neg + 1
    if (j == 0):
        print (j,"es cero aweonao")
        cer = cer + 1
    if(j>0):
        print (j," es positivo")
        pos = pos + 1
    i = i+1
print ("pusiste ",pos," positivos ",neg," negativos y ",cer," ceros")

