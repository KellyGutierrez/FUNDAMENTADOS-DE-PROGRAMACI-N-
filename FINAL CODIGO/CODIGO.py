import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import pyplot


archivoexcel =pd.read_excel("Futbol_Partidos.xlsx")
archivoexcel.head()
df=pd.DataFrame(archivoexcel)
print(archivoexcel) 

sumalocales=df["local"]
visitante=df["visitante"]
goles_local=df["goles_local"]
goles_visita=df["goles_visita"]
local=df["local"]
visitante=df["visitante"]
ciudad=df["ciudad"]
gana_local=df["gana_local"]
gana_visita=df["gana_visita"]
torneo=df["torneo"]
sumalocales=df["local"]
pais_x=df["pais_x"]

#SUMA GOLES LOCAL

def suma_locales():
    sumalocales=archivoexcel['goles_local'].sum()
    print()
    print("El total de goles de los equipos locales son:",sumalocales,"\n")
    
suma_locales()

#SUMA GOLES VISITANTE
def suma_visitantes():
    sumavisitantes=archivoexcel['goles_visita'].sum()
    print("El total de goles de los equipos visitantes son:",sumavisitantes,"\n")
    
suma_visitantes()

#GRAFICA LOCALES Y VISITANTES

# total de goles
def goles_totales():
    suma=0
    locales2=df["goles_local"]
    visita2=df["goles_visita"]
    for x in range(914):
        suma+=locales2[x]
        suma+=visita2[x]
    print("Los goles totales fueron:",suma,"\n")
goles_totales()


#Grafica total goles



#GOLES LOCAL
print("***** lISTA DE TORNEOS *****","\n")
print("FIFA World Cup qualification\n Friendly\n Copa América\n Confederations Cup\n Copa Paz del Chaco\n Kirin Cup\n FIFA World Cup\n Gold Cup\n AFC Asian Cup\n Copa del Pacífico")
campeonato=str(input("Ingrese un torneo para calcular el total de goles locales: "))
def goles_local_campeonato(campeonato):
    campeonato = df[df['torneo']== campeonato]['goles_local'].sum()
    print("El total de goles locales en el torneo",campeonato,"son: ",campeonato,"\n")
    return campeonato
goles_local_campeonato(campeonato) 
  
#GOLES  VISITANTE
print("***** lISTA DE TORNEOS *****","\n")
print("FIFA World Cup qualification\n Friendly\n Copa América\n Confederations Cup\n Copa Paz del Chaco\n Kirin Cup\n FIFA World Cup\n Gold Cup\n AFC Asian Cup\n Copa del Pacífico")
campeonato=str(input("Ingrese un torneo para calcular el total de goles visitantes: "))
def goles_visitantes_campeonato(campeonato):
    campeonato = df[df['torneo']== campeonato]['goles_visita'].sum()
    print("El total de goles visitantes en el torneo",campeonato,"son: ",campeonato,"\n")
    return campeonato
goles_visitantes_campeonato(campeonato)


#GOLES EN TOTAL 
def goles_totales(fila):
    resultado=fila['goles_local']+fila['goles_visita']
    return resultado 
df['goles_totales']= df.apply(goles_totales,axis=1)
print(df['goles_totales'].sum())

#GOLES TOTALES TORNEO
def goles_totales_torneo(campeonato):
    campeonato= df[df['torneo']== campeonato]['goles_totales'].sum()
    return campeonato
print("Ingrese un campeonato: ")
print("Sus opciones son: ")
print("FIFA World Cup qualification\n Friendly\n Copa América\n Confederations Cup\n Copa Paz del Chaco\n Kirin Cup\n FIFA World Cup\n Gold Cup\n AFC Asian Cup\n Copa del Pacífico\n")
campeonato= input()
sumatoria_torneo= goles_totales_torneo(campeonato)

#DATOS SELECCIONES
def partidos_seleccion():  
    df= pd.DataFrame(archivoexcel,columns = ['local','visitante'])    
    print (pd.Series(df.values.ravel()).value_counts()) 
print("La cantidad de partidos por seleccion son: ","\n")
partidos_seleccion()



#DATOS ACERCA DEL EQUIPO VISITANTE
def partidos_locales_visitantes():
    df = pd.DataFrame(archivoexcel,columns = ['local'])
    print("Partidos de seleccion de local: ")
    print(pd.Series(df.values.ravel()).value_counts())
    
    df = pd.DataFrame(archivoexcel,columns = ['visitante'])
    print("Partidos de seleccion de visitantes: ","\n")
    print(pd.Series(df.values.ravel()).value_counts())
    
partidos_locales_visitantes()

suma_locales()
suma_visitantes()
print("La cantidad de partidos por seleccion son: ")
partidos_seleccion()
partidos_locales_visitantes()
print("Deslice hacia arriba para ver los datos generados ↑")

def grafica_l_v():
    partidos = ["Locales","Visitantes"]
    datos = [1493,901]
    colores = ["aquamarine","pink"]
    pyplot.title(" goles de los locales y visitantes")
    pyplot.bar(partidos, height=datos, color=colores, width=0.8)
    pyplot.show()
    
grafica_l_v()

def grafica_total_goles():
    total=[' Total de goles de todos los partidos']
    dato=[2394]
    color=['palegreen']
    plt.title('Goles totales.')
    plt.bar(total,height=dato,color=color,width=0.5)
    plt.show

grafica_total_goles()

def graf_locales_visitantes_campeonato():
    x=['Locales', 'Visitantes']
    y=[goles_visitantes_campeonato(campeonato),goles_local_campeonato(campeonato)]
    colors=['yellow','mediumpurple']
    plt.bar(x,y,color=colors)
    plt.title('Goles totales y goles de visitantes y locales por torneo.')
    plt.ylabel('Goles')
    plt.show

graf_locales_visitantes_campeonato()

def partido_seleccion_calculo_grafica():
    local=[]
    visitante=[]
    columna_local=df.iloc[:,1]
    col_visitante=df.iloc[:,2]
    sel=set(columna_local);sel=list(sel)
    s1=list(columna_local);s2=list(col_visitante)
    for i in range(len(sel)):
            contador_locales=0
            contador_visitantes=0
            for j in range(len(s1)):
                comp=sel[i]
                sedf=s1[j]
                if sedf==comp:
                   contador_locales=contador_locales+1
            for h in range(len(s2)):
                    comp1=sel[i]
                    sedf1=s2[h]
                    if sedf1==comp1:
                        contador_visitantes=contador_visitantes+1
            visitante.append(contador_visitantes)
            local.append(contador_locales)
            
            print(comp,'jugó',contador_locales,'veces como local, y',contador_visitantes,'como visitante.')
    
    fig,ax=plt.subplots()
    ax.barh(sel,local,color='magenta',label='Partidos locales.')
    ax.barh(sel,visitante,color='skyblue',left=local,label='Partidos visitantes.')
    ax.invert_yaxis()
    ax.legend(loc=(1.1,0.8))
    plt.show()
    
partido_seleccion_calculo_grafica()




#PARTIDOS EN LOS QUE HA JUGADO LA SELECCION 
def once():
    suma=0
    
    n=str(input("ingrese nombre del equipo:"))
    print()
    print("***************Partidos jugados***************","\n")
    for x in range(len(local)):
        if local[x]==n or visitante[x]==n:
            suma+=1
            print(local[x],"vs",visitante[x],"marcador:",goles_local[x],"-",goles_visita[x],"\n")
    
    print("Partidos en total:",suma)
once()

#CIUDADES EN LOS PAISES JUGADOS
equipo=str(input("ingrese equipo:"))
def doce(equipo):
    suma=0
    suma2=0
    for x in range(len(local)):
        if local[x]==equipo:
            suma+=1
        else:
            if visitante[x]==equipo:
                suma2+=1
    print("****** Partidos",equipo,"******")
    print("Partidos locales:",suma,"-","Partidos como Visitante:",suma2)
doce(equipo)

n=str(input("ingrese equipo:"))

def trece(n):
    print()
    print("******** Lista de las ciudades de los partidos de",n,"********","\n")
    for x in range(len(local)):
        if local[x]==n or visitante[x]==n:
            print(local[x],"vs",visitante[x],"- Ciuad:",ciudad[x])
trece(n)

equipo2=str(input("ingrese equipo:"))

#PARTIDOS GANADOS PERDIDOS EMPATADOS
def quince(equipo):
    gano=0
    perdio=0
    empate=0
    for x in range(len(local)):
        if local[x]==equipo2 and gana_local[x]==1:
            gano+=1
        else:
            if visitante[x]==equipo2 and gana_visita[x]==1:
                gano+=1
            else:
                if visitante[x]==equipo2 and gana_visita[x]==0 and gana_local[x]==1:
                    perdio+=1
                else:
                    if local[x]==equipo2 and gana_local[x]==0 and gana_visita[x]==1:
                        perdio+=1
                    else: 
                        if local[x]==equipo2 and gana_local[x]==0 and gana_visita[x]==0:
                            empate+=1
                        else: 
                            if visitante[x]==equipo2 and gana_local[x]==0 and gana_visita[x]==0:
                                empate+=1
    print("partidos ganados:",gano,"partidos perdidos:",perdio,"partidos empatados:",empate)
    
quince(equipo2)


def partidos_general():
    nomb=df.iloc[:,1]
    nomb2=df.iloc[:,2]
    torneo=df.iloc[:,5]
    gano_loc=df.iloc[:,10]
    gano_vis=df.iloc[:,11]
    s1=list(nomb)
    s2=list(nomb2)
    tor=list(torneo)
    gano_l=list(gano_loc)
    gano_v=list(gano_vis)
    seleccion=input('Ingrese el nombre de la selección: ')
    while seleccion not in s1 or seleccion not in s2:
        seleccion=input('Seleccion incorrecta, intente nuevamente: ')
    print("**********   Marcadores",seleccion,"  **********")
    torneo=set(tor)
    cont_w=0
    cont_l=0
    for j in torneo: 
        for i in range(len(s1)):
            comp1=s1[i]
            comp2=s2[i]
            comp_wl=gano_l[i]
            comp_wv=gano_v[i]
            torneo=tor[i]
            if torneo==j:
                if comp1==seleccion and comp_wl==1:
                    cont_w=cont_w+1
                elif comp2==seleccion and comp_wv==1:
                    cont_w=cont_w+1
                elif comp1==seleccion and comp_wv==1:
                    cont_l=cont_l+1
                elif comp2==seleccion and comp_wl==1:
                    cont_l=cont_l+1
        print('Torneo:',j,"Partidos ganados:",cont_w,'Partidos Perdidos',cont_l,)
    print('Partidos totales ganados:',cont_w,'Partidos totales perdidos',cont_l,)


partidos_general()

#MARCADORES DE LA SELECCION 
def GOLES():
    nomb=df.iloc[:,1]
    nomb2=df.iloc[:,2]
    gol=df.iloc[:,3]
    gol2=df.iloc[:,4]
    s1=list(nomb)
    s2=list(nomb2)
    goles=list(gol)
    goles2=list(gol2)
    seleccion=input('Ingrese el nombre de la selección que desea buscar: ')
    while seleccion not in s1 or seleccion not in s2:
        seleccion=input('Esa selección no está registrada en este programa, intente con otra: ')
    cont_p=0
    cont_w=0
    cont_l=0
    cont_d=0
    gol=0
    gol_rival=0
    for i in range(len(s1)):
        comp1=s1[i]
        comp2=s2[i]
        gol_l=goles[i]
        gol_v=goles2[i]
        if comp1==seleccion or comp2==seleccion:
            cont_p=cont_p+1
            if comp1==seleccion:
                gol=gol+gol_l
                gol_rival=gol_rival+gol_v
            elif comp2==seleccion:
                gol=gol+gol_v
                gol_rival=gol_rival+gol_l
            if comp1==seleccion and gol_l>gol_v:
                cont_w=cont_w+1
            elif comp2==seleccion and gol_v>gol_l:
                cont_w=cont_w+1
            elif gol_l==gol_v:
                cont_d=cont_d+1
            else:
                cont_l=cont_l+1
    print('La selección de',seleccion,'ganó',cont_w,'empató',cont_d,'y perdió',cont_l,'partidos con',gol,'goles a favor, y',gol_rival,'goles en contra.')
#Mejor selección por ranking. 17  
GOLES()
      
#MEJOR EQUIPO 
def mejor_seleccion():
    nomb=df.iloc[:,1]
    nomb2=df.iloc[:,2]
    clasi_loc=df.iloc[:,12]
    clasi_vis=df.iloc[:,14]
    tor=df.iloc[:,5]
    s1=list(nomb)
    s2=list(nomb2)
    clasi_lo=list(clasi_loc)
    clasi_vi=list(clasi_vis)
    torneo=list(tor)
    camp=set(torneo)
    mejor_l=None
    mejor_v=None
    
    for j in camp:
        clasi_local=999
        clasi_visit=999
        for i in range(len(s1)):
            comp1=s1[i]
            comp2=s2[i]
            clasi1=clasi_lo[i]
            clasi2=clasi_vi[i]
            champ=torneo[i]
            if champ==j:
                if clasi1<clasi_local:
                    mejor_l=comp1
                    clasi_local=clasi1
                if clasi1<clasi_visit:
                    mejor_v=comp2
                    clasi_visit=clasi2
        print('*Según el torneo:',j,'- Mejor seleccion local:',mejor_l,'con clasificacion:',clasi_local,',- Mejor seleccion visitante:',mejor_v,'con clasificacion:',clasi_visit,'\n')
    
mejor_seleccion()   

print("GRACIAS POR USAR EL PROGRAMA, FELIZ DIA ")
    
    
    
    
    
    

    

