# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 10:29:58 2021

@author: Kmilo
"""

# programa que calcula el cuadro de los primeros 100 numeros

#Area de declaracion de variables
cuadradoNumero=0
acumuladorSuma= 0
num= 1

#Entrada
cantidadNumeros=int(input("cantidad de numeros :"))
#proceso
#ciclo para 1 hasta 100
for num in range(cantidadNumeros+1):
    cuadradoNumero = num*num
    acumuladorSuma=acumuladorSuma+cuadradoNumero
    print("el cuadrado de : ", num, "es :", cuadradoNumero)
    print("la suma acumulada es :",acumuladorSuma)
#fin del ciclo

print("la suma de los cuadrados es :", acumuladorSuma)