# Interactuar con datos
# Fuentes de datos
# 1. Asignar los datos desde la definicion de la estructura

# Importar la libreria
import pandas as pd

# Crear la estructura de datos tipo dataframe y se le asignan los datos
datosEstudiantes = pd.DataFrame({'Estudiante':['Juan','Ana','Marta'],
                                 'Apellido':['Gomez','Diaz','Arango'],
                                 'Edad':[18,25,16]})

# Agregar una columna y le asignamos el mismo dato

datosEstudiantes['Vivo']='TRUE'
datosEstudiantes['Genero']='Masculino'

# Insertar una columna y se asignan los datos

datosEstudiantes.insert(3,'Genero correcto',['Masculino','Femenino','Femenino'])
datosEstudiantes.insert(4,'Semestre',['Primero','Quinto','Noveno'])

# Segunda forma de agregar una columna sobreescribiendo
datosEstudiantes=datosEstudiantes.assign(Colegio=['Nuestra Señora','Filipense','San Luis'])



# Consultar la estructura
print(datosEstudiantes)



