import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


archivoexcel =pd.read_excel("Tabla excel.xlsx")
archivoexcel.head()
df=pd.DataFrame(archivoexcel)
print(archivoexcel) 
departamento=df["Departamento"]
poblacion=df["Poblacion"]
superficie=["Superficie"]
def areatotal():
    suma=0
    Superficie2=df["Superficie"]
    for x in range(33):
        suma+=Superficie2[x]
    print("La superficie total es:",suma,"Km2")

areatotal()
def promedio_axd():
    suma=0
    Superficie2=df["Superficie"]
    for x in range(33):
        suma+=Superficie2[x]
    departamento=df["Departamento"]
    promedio=suma/len(departamento)
    print("El promedio de area por departamento es:","{:.2f}".format(promedio))
promedio_axd()
def promedio_pxd():
    suma2=0
    poblacion=df["Poblacion"]
    for x in range(33):
        suma2+=poblacion[x]
    promedio=suma2/33
    print("El promedio de poblacion por departamento es:","{:.2f}".format(promedio))
promedio_pxd()
def departamentomenor():
    poblacion=df["Poblacion"]
    departamento=df["Departamento"]
    menor=poblacion[0]
    
    for x in range(33):
        if poblacion[x]<menor:
            menor=poblacion[x]
            posicion=departamento[x]
           
    print("El departamento con menor poblacion es:",posicion,"con:",menor,"habitantes")
departamentomenor()
def departamentomayor():
    poblacion=df["Poblacion"]
    departamento=df["Departamento"]
    mayor=poblacion[0]
    
    for x in range(33):
        if poblacion[x]>mayor:
            mayor=poblacion[x]
            posicion=departamento[x]
    print("El departamento con mayor pobalcion es",posicion,"con:",mayor,"habitantes")
departamentomayor()
def relacion():
    suma=0
    suma2=0
    poblacion=df["Poblacion"]
    Superficie2=df["Superficie"]
    for x in range(33):
        suma+=Superficie2[x]
    for x in range(33):
        suma2+=poblacion[x]
    resultado=suma2/suma
    print("En Colombia hay","{:.1f}".format(resultado),"habitantes por Km2")
relacion()
def grafico_dxp():
    departamento=df["Departamento"]
    poblacion=df["Poblacion"]
    #GENERAR GRAFICO
    fig,ax=plt.subplots()
    ax.set_title("Departamento y Poblacion ")
    ax.set_ylabel("Departamento")
    ax.set_xlabel("Poblacion")
    plt.bar(departamento,poblacion)
    plt.show()
grafico_dxp()
def grafico_dxa():
     departamento=df["Departamento"]
     superficie=df["Superficie"]
     fig,ax=plt.subplots()
     ax.set_title("Departamento y Area ")
     ax.set_ylabel("Area")
     ax.set_xlabel("Superficie")
     plt.bar(departamento,superficie)
     plt.show()
grafico_dxa()
def horizontal_dxa():
    fig,ax=plt.subplots()
    ax.set_title("Departamento y Poblacion ")
    ax.set_ylabel("Departamento")
    ax.set_xlabel("Poblacion")
    plt.barh(departamento,poblacion)
    plt.show()
horizontal_dxa()
def hori_dxa():
    area=df["Superficie"]
    fig,ax=plt.subplots()
    ax.set_title("Departamento y Superficie ")
    ax.set_ylabel("Departamento")
    ax.set_xlabel("Area")
    plt.barh(departamento,area)
    plt.show()
hori_dxa()
def pie_dxp():
    fig,ax=plt.subplots()
    ax.set_title("Poblacion por Departamento ")
    plt.pie(poblacion, labels=departamento)
    plt.show()
pie_dxp()
def pie_dxa():
    area=df["Superficie"]
    fig,ax=plt.subplots()
    ax.set_title("Area por departamento ")
    plt.pie(area, labels=departamento)
    plt.show()
pie_dxa()


    
    
     