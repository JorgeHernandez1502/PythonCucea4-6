print("muestra del menu:")
print(" 1.manzanas")
print(" 2.peras")
print(" 3.uvas")

opcion=int(input("ingresa tu opcion"))
if opcion==1:
    nombreFruta="manzana"
elif opcion==2:
    nombreFruta="pera"
elif opcion==3:
    nombreFruta="uva"
else:
    nombreFruta=""
    print("valor no valido")
