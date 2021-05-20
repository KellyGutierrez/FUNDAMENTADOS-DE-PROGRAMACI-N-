# Lectura de archivos tipo excel
# Importar librerias
import pandas as pd

# Leer archivo excel

archivoExcel = pd.read_excel('ventas_productos.xlsx')

# Imprimir los datos
print(archivoExcel)
archivoExcel.head()
