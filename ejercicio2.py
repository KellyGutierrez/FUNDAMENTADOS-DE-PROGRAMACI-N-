#librerias usadas en los ejercicios
import random

# ejercicio 2

# area declaracion de variables

cantidadNumeros=0
contadorRepeticiones=0
numero=0
acumuladorSumaTodosNumeros=0
acumuladorSumaNumerosPositivos=0
acumuladorSumaNumerosNegativos=0

#entradas
cantidadNumeros=int(input("cantidad de numeros: "))

#Procesos
while contadorRepeticiones<cantidadNumeros:
    numero=random.randint(-100,100)  #generamos numero aleatorio
    print("numero :", numero)
    acumuladorSumaTodosNumeros=acumuladorSumaTodosNumeros+numero #acumulo +
    if numero>0:
        acumuladorSumaNumerosPositivos=acumuladorSumaNumerosPositivos+numero
    else:
        acumuladorSumaNumerosNegativos=acumuladorSumaNumerosNegativos+numero
    contadorRepeticiones=contadorRepeticiones+1
#Fin del ciclo

#salida de
print("suma todo :", acumuladorSumaTodosNumeros)
print("suma positivos :", acumuladorSumaNumerosPositivos)
print("suma negativo :", acumuladorSumaNumerosNegativos)
    

