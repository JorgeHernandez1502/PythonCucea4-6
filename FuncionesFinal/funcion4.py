def calcularIva(cantidadSinIva,porcentajedeiva=21):
    iva=cantidadSinIva*(porcentajedeiva*.01)
    return iva
impuesto=calcularIva(100,16) 
print(impuesto)       
    