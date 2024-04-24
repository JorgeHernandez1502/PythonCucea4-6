descuento=0
total=0
cantidadManzana=1
cantidadManzana=float(input('Dime la cantidad de manzanas vendidas: '))
while cantidadManzana!=0:
    precioManzana=float(input('Dime el precio de la manzana: '))
    print("hola buenas tardes")
    total=precioManzana*cantidadManzana
    
    if cantidadManzana==30:
        print("descuento espceial")
        descuento=(cantidadManzana*precioManzana)*.2
        print(f"el descuento es de {descuento}")
        total=total-descuento
    elif cantidadManzana>=10:
        print("descuento normal")
        descuento=(cantidadManzana*precioManzana)*.1
        print(f"el descuento es de {descuento}")
        total=total-descuento
    else :
        print("Gracias por comprar")


    print(f"total: {total}")  
