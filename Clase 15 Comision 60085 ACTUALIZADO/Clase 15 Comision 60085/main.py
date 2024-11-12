# #escribir un archivo
# #Si el archivo no existe, lo crea
# with open("mi_archivo.txt", "w") as archivo:
#     archivo.write("¡HOLA MUNDO !\n")

# with open("mi_archivo.txt", "w", encoding="utf-8") as archivo:
#     archivo.write("¡chauchau")
     

# # Leer desde un archivo
# with open("mi_archivo.txt", "r") as archivo:
#     contenido = archivo.read()
#     print(contenido)

# #!: ¿Como podemos apendear a nuestro archivo?

# with open("mi_archivo.txt", "a", encoding="utf-8") as archivo:
#     archivo.write("¡linea nueva")




# # # #ESCRIBIENDO UN ARCHIVO CON SU RUTA DE ACCESO
# ruta = "C:/Users/Ale Sosa/Desktop/clase15_comision_60085.txt"


# with open(ruta, "a", encoding= "utf-8" ) as archivo:
#     archivo.write("Esto es una línea de texto.\n")
#     archivo.write("Esta es otra línea.\n")
#     archivo.write("Y una más.\n")
#     archivo.write("Esto es otra línea de texto.\n")
#     archivo.write("Esta es una segunda  línea.\n")
#     archivo.write("Y esta es otra más.\n")

# print("¡El archivo se ha guardado correctamente!")

# ruta = "C:/Users/Ale Sosa/Desktop/clase15_comision_60085.txt"
# # Abrir el archivo en modo escritura
# archivo = open(ruta, "a", encoding="utf-8")

# # Escribir en el archivo
# archivo.write("hola\n")
# archivo.write("Lorem\n")

# # Cerrar el archivo explícitamente
# archivo.close()

# print("El archivo se ha guardado correctamente.")




# #! ¿COMO PUEDO AGREGAR ALGO A UN ARCHIVO QUE NO ESTÁ EN MI ENTORNO?



# #! ¿Y SI QUIERO VER UN ARCHIVO DE UNA URL?
# #https://drive.usercontent.google.com/u/0/uc?id=1r3tsdHXRGNsZrWQXBFe7wBwi9HUFHmj4&export=download

# import urllib.request

# def descargar_y_leer_archivo(url, nombre_archivo):
#     """Descarga un archivo desde una URL y lo lee."""  #docstring
#     urllib.request.urlretrieve(url, nombre_archivo)
#     with open(nombre_archivo, "r", encoding="utf-8") as archivo:
#         contenido = archivo.read()
#         return contenido

# # # URL de descarga directa
# url_descarga = "https://drive.usercontent.google.com/u/0/uc?id=1r3tsdHXRGNsZrWQXBFe7wBwi9HUFHmj4&export=download"  

# nombre_archivo = "mi_archivo_descargado.txt"

# contenido = descargar_y_leer_archivo(url_descarga, nombre_archivo)
# print(contenido)



## seek()
# with open("mi_archivo.txt", "r", encoding="utf-8") as archivo:
#     archivo.seek(20)  
#     datos = archivo.read()  
#     print(datos) 

# #JSON
import json

data = {}
data['clients'] = []

data['clients'].append({
    'first_name': 'Sigrid',
    'last_name': 'Mannock',
    'age': 27,
    'amount': 7.17})

data['clients'].append({
    'first_name': 'Joe',
    'last_name': 'Hinners',
    'age': 31,
    'amount': [1.90, 5.50]})

data['clients'].append({
    'first_name': 'Theodoric',
    'last_name': 'Rivers',
    'age': 36,
    'amount': 1.11})


#Creando un JSON
with open('superjason.json', 'w') as file:
    print("Archivo creado")
    json.dump(data, file, indent=4)


# # Leyendo mi archivo JSON
# with open('superjason.json') as file:
#     data = json.load(file)

#     for client in data['clients']:
#         print('First name:', client['first_name'])
#         print('Last name:', client['last_name'])
#         print('Age:', client['age'])
#         print('Amount:', client['amount'])
#         print('')

