#programa que calcula la hipotenusa y el area de un triangulo rectangulo

#declaracion y llamado a las librerias y paquetes
import math

# dclaracion e inicializacion de variables

def f_titulo():
    print("CALCULAR LA HIPOTENUSA DE UN TRIANGULO RECTANGULO")
    
def f_calcularhipotenusa(p_catetoUno,p_catetoDos):  # prototipo de la funcion

    vp_radicando=0.0
    vps_hipotenusa= 0.0
    #vps_perimetro=0.0 
    
    #procesos
    vp_radicando=math.pow(p_catetoUno,2) + math.pow(p_catetoDos,2)
    vps_hipotenusa= math.sqrt(vp_radicando)
    
    #retornar la respuesta
    return vps_hipotenusa

    
#fin del desarrollo de la funcion

def f_despedida():
    print("ADIOS")

#CONTROL  DEL PROGRAMA - PRINCIPAL
f_titulo()
ve_catetoUno=int(input("digite cateto uno :"))
ve_catetoDos=int(input("digite cateto dos :"))
vps_rf_hip=f_calcularhipotenusa(ve_catetoUno,ve_catetoDos)
print("la hipotenusa es ", vps_rf_hip)
f_despedida()

#realizo el llamado a la funcion por segunda vez
ve_catetoUno=int(input("digite cateto uno :"))
ve_catetoDos=int(input("digite cateto dos :"))
vps_rf_hip=f_calcularhipotenusa(ve_catetoUno,ve_catetoDos)
print("la hipotenusa es ", vps_rf_hip)
