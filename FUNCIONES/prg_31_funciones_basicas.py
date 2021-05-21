#programa que calcula la hipotenusa y el area de un triangulo rectangulo

#declaracion y llamado a las librerias y paquetes
import math

def f_titulo():
    print("CALCULAR LA HIPOTENUSA DE UN TRIANGULO RECTANGULO")

def f_calcularhipotenusa():  # prototipo de la funcion 
    #variables
    ve_catetouno= 0.0
    ve_catetodos= 0.0

    vp_radicando=0.0

    vps_hipotenusa= 0.0
    #vps_perimetro=0.0

    #entradas
    ve_catetouno=int(input("digite cateto uno :"))
    ve_catetodos=int(input("digite cateto dos :"))

    #procesos

    vp_radicando =math.pow(ve_catetouno,2) + math.pow(ve_catetodos,2)
    vps_hipotenusa= math.sqrt(vp_radicando)
    #salidas
    print("hipotenusa", vps_hipotenusa)
#fin del desarrollo de la funcion

#llamado de la funcion

f_titulo()
f_calcularhipotenusa()

