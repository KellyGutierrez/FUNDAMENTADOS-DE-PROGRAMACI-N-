# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 10:22:36 2021

@author: TORREX
"""
#Declarar lista de notas vacia
lista=[]

#AlMACENAR DATOS EN LA LISTA 
nota1=0
nota2=0
nota3=0
nota4=0
nota5=0
reprobo=0
aprobo=0

for x in range(10):
    #Nota por estudiante
    notas=float(input("ingrese nota:"))
    #Adicionamos la nota a la lista 
    lista.append(notas)
    #Contadores
    if notas<=1.0:
        nota1+=1
        reprobo+=1
    else:
        if notas<=2.0:
            nota2+=1
            reprobo+=1
        else:
            if notas<=2.9:
                nota3+=1
                reprobo+=1
            else:
                if notas<=4.0:
                    nota4+=1
                    aprobo+=1
                else:
                    if notas<=5.0:
                        nota5+=1
                        aprobo+=1

#Declaracion del menor valor                        
menor=lista[0]
posicion=0
for x in range(1,10):
    if lista[x]<menor:
        menor=lista[x]
        posicion=x

#Declaracion del mayor valor        
mayor=lista[0]
posicion2=0
for x in range(1,10):
    if lista[x]>mayor:
        mayor=lista[x]
        posicion2=x
        
#Suma de las notas
sumanotas=0.0
for i in range(len(lista)):
    sumanotas+=lista[i]
print("suma notas:",sumanotas)

#Promedio
promedio=sumanotas/10
        
#imprimir lista 
print("**********LISTA DE NOTAS**********")
print(lista)
print("**********DATOS DE RESULTADOS**********")

print("promedio de notas:",promedio)
#Personas reprobadas
print("personas que reprobaron:",reprobo)
#Personas aprobadas 
print("personas que aprobaron:",aprobo)
#Posicion del menor valor
print("nota menor:",menor,"con posicion",posicion)
#Posicion del mayor valor
print("nota mayor:",mayor,"con posicion",posicion2)

#Cantidad de estudiantes ubicados en cada seccion 
print("personas con nota 0.0 a 1.0:",nota1)
print("personas con nota 1.1 a 2.0:",nota2)
print("personas con nota 2.1 a 2.9:",nota3)
print("personas con nota 3.0 a 4.0:",nota4)
print("personas con nota 4.1 a 5.0:",nota5)







    
