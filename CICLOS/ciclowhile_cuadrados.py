#   ciclo while
#declaracion de variables
contadorRepeticiones=1
cuadradoNumero=0
acumuladorSuma=0

#entrada
canidadNumeros=int(input("cantidad de numeros: "))
#proceso
while contadorRepeticiones<=5:
    cuadradoNumero=pow(contadorRepeticiones,2)
    acumuladorSuma=acumuladorSuma+cuadradoNumero
    print("el cuadrado de :", contadorRepeticiones, "es :", cuadradoNumero)
    print("la suma acumulada es :", acumuladorSuma)
    contadorRepeticiones=contadorRepeticiones+1

#fin While

#salida
print("la suma de los cuadrados es :", acumuladorSuma)
