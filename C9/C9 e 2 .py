
precio1 = float(input("dime el total porque no me pagan como para sumar os productos y tengo fe de que sabes sumar"))
def calcular (precio):
    print ("el total pero sin descuento es ",precio, "pero... ")
    if (precio > 30000):
        preciodetreinta = (precio - precio * 0.2)
        print ("tenes un 20 en off")
        print("TOTAL = ",preciodetreinta)
    if (precio <= 30000 and precio >= 10000):
        preciodediez = (precio - precio* 0.1)
        print ("tenes un 10 en off")
        print ("TOTAL = ",preciodediez)
    if (precio < 10000):
        print ("no tenes descuento jajajaj")
        print ("TOTAL = ",precio)

calcular (precio1)