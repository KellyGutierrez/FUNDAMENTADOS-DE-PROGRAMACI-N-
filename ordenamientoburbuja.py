# ordenamiento burbuja

# definicion de vectores

#listaEnteros=[24,54,32,5,47,89,52,4,62,39]

listaEnteros=[]

def cargardatos (listaEnteros):
    print("cargar datos")
    for i in range (10):
        dato=int(input("Ingrese valor :"))
        listaEnteros.append(dato)
        print(listaEnteros)
    
#funcion que realiza el ordenamiento burbuja 

def ordburbuja(listaDesordenada):
    print("ordenar datos")
    for i in range(1,len(listaDesordenada)-1):
                for j in range (0,len(listaDesordenada)-1):
                    if listaDesordenada[j]>listaDesordenada[j+1]:
                        aux=listaDesordenada[j]
                        listaDesordenada[j]=listaDesordenada[j+1]
                        listaDesordenada[j+1]=aux
    print(listaDesordenada)                         
#fin del ordenamiento
#llamar la funcion que carga los datos
cargardatos(listaEnteros)
#llamar la funcion ordenar burbuja

ordburbuja(listaEnteros)
       