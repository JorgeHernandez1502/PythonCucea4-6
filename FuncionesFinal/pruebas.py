def calcularDescuento(cantidad,precio):
    if cantidad==30:
        print("descuento espceial")
        descuento=(cantidad*precio)*.2
        print(f"el descuento es de {descuento}")
       
    elif cantidad>=10:
        print("descuento normal")
        descuento=(cantidad*precio)*.1
        print(f"el descuento es de {descuento}")
        
    else :
        descuento=0
        print("Gracias por comprar")
    return descuento

descuento=calcularDescuento(30,10)
print(descuento)
descuento=calcularDescuento(15,10)
print(descuento)
descuento=calcularDescuento(5,10)
print(descuento)
