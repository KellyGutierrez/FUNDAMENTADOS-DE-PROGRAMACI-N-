import math

# Declaracion de variables
A_100202015797_82202113173 = 0
B_100202015797_82202113173 = 0
C_100202015797_82202113173 = 0
S = 0

# Entradas 
A_100202015797_82202113173 = int(input("Digite el lado A: "))
B_100202015797_82202113173 = int(input("Digite el lado B: "))
C_100202015797_82202113173 = int(input("Digite el lado C: "))

# Proceso
def area_triangulo():
    S = (A_100202015797_82202113173 + B_100202015797_82202113173 + C_100202015797_82202113173)/2
    area = math.sqrt(S * (S - A_100202015797_82202113173) * (S - B_100202015797_82202113173) * (S - C_100202015797_82202113173))
    print("El aera del triangulo es: ", area)
    
def perimetro_triangulo():
    perimetro = A_100202015797_82202113173 + B_100202015797_82202113173 + C_100202015797_82202113173
    print("El perimetro del triangulo es: ", perimetro)
    
# Fin del proceso
area_triangulo()
perimetro_triangulo()



