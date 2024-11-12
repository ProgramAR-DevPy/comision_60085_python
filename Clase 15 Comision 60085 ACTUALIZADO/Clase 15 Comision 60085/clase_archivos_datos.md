# Persistencia de Datos: ¡Que tus Datos No se Esfumen! 💾
- Imagina que estás jugando un videojuego 🎮 y llegas al nivel final. Apagas la consola, pero al día siguiente, ¡vuelves a empezar desde cero! 😱  Frustrante, ¿verdad? La persistencia de datos evita que eso ocurra en tus programas.

### ¿Qué es la Persistencia de Datos? 🤔
- Es la capacidad de guardar la información de tu programa de forma permanente, para que puedas recuperarla más tarde. Es como guardar tu progreso en el videojuego para no tener que empezar de nuevo cada vez.

### ¿Por qué es Importante? 💾
1. **Evita la pérdida de datos:** Asegura que la información generada por tu programa no desaparezca cuando lo cierras.
2. **Permite continuar donde lo dejaste:** Puedes retomar tu trabajo o análisis desde el último punto guardado.
3. **Facilita el intercambio de datos:** Puedes compartir la información generada por tu programa con otros usuarios o sistemas.

### Tipos de Persistencia: ¡Elige tu Arsenal! ⚔️
- **Bases de Datos:** Son como grandes almacenes donde puedes guardar y organizar grandes cantidades de datos de forma estructurada. Son ideales para aplicaciones complejas y escalables.
- **Archivos:** Son la forma más simple y directa de guardar datos. Son como pequeñas cajas donde puedes almacenar información en diferentes formatos.

### Archivos: ¡Tus Cajas de Datos! 📦
- Un archivo es un conjunto de datos almacenados en un dispositivo (disco duro, memoria USB, etc.). Puedes pensar en ellos como documentos de texto, imágenes, música o cualquier otro tipo de información digital.

### **Tipos de Archivos:**

1. **Archivos Binarios:** Almacenan datos en un formato que solo la computadora puede entender (por ejemplo, imágenes, música, programas ejecutables).
2. **Archivos de Texto:** Almacenan texto legible por humanos, como código fuente, documentos de texto o archivos CSV.

### Trabajando con Archivos de Texto en Python: ¡Abre, Lee, Escribe y Cierra! 📖

Python te ofrece funciones simples para trabajar con archivos de texto:

- open`(nombre_archivo, modo):` Abre un archivo en el modo especificado `("r" para lectura, "w" para escritura, "a" para agregar)`.
- `archivo.read():` Lee todo el contenido del archivo como una cadena de texto.
- `archivo.readline():` Lee una línea del archivo.
- `archivo.readlines():` Lee todas las líneas del archivo y las devuelve como una lista.
- `archivo.write(texto):` Escribe el texto en el archivo.
- `archivo.close():` Cierra el archivo.

### Ejemplo:

```python
# Escribir en un archivo
with open("mi_archivo.txt", "w") as archivo:
    archivo.write("¡Hola, mundo!\n")

# Leer desde un archivo
with open("mi_archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)  # Output: ¡Hola, mundo!
```

# Escritura de Archivos en Python: ¡Plasma tus Datos en el Disco Duro! 💾
- Imagina que tienes una idea brillante 💡 y quieres anotarla para no olvidarla. Puedes escribirla en un papel o, mejor aún, ¡guardarla en un archivo en tu computadora!

En Python, escribir en un archivo es como usar un bolígrafo digital para plasmar tus datos en el disco duro. 🖊️💻

### Paso a Paso:
1. **Elige la Ubicación:** Decide dónde quieres guardar tu archivo. Puede ser en una carpeta específica de tu computadora.
2. **Define la Ruta:** Crea una variable que almacene la ruta completa del archivo, incluyendo el nombre del archivo y su extensión.
- **Ejemplo:** ruta = "C:/Users/TuUsuario/Documentos/mi_archivo.txt"
3. **Abre el Archivo:** Usa la función open() para abrir el archivo en modo escritura ("w"). Esto crea el archivo si no existe, o lo sobrescribe si ya existe.

- **Ejemplo:** `archivo = open(ruta, "w")`

4. Escribe en el Archivo: Usa el método `write()` del objeto archivo para escribir datos en el archivo.
- **Ejemplo:** `archivo.write("¡Hola, mundo!\n")`

5 Cierra el Archivo: Usa el método `close()` para cerrar el archivo y liberar los recursos asociados.
- **Ejemplo:** `archivo.close()`

Ejemplo Completo 1:

```python
ruta = "C:/Users/TuUsuario/Documentos/mi_archivo.txt"

with open(ruta, "w") as archivo:
    archivo.write("Esto es una línea de texto.\n")
    archivo.write("Esta es otra línea.\n")
    archivo.write("Y una más.\n")

print("¡El archivo se ha guardado correctamente!")
```

### Explicación:

- Definimos la ruta donde queremos guardar el archivo.
- Usamos `with open(ruta, "w")` as archivo: para abrir el archivo en modo escritura. El bloque `with` se encarga de cerrar el archivo automáticamente al finalizar.
- Escribimos varias líneas de texto en el archivo usando `archivo.write()`.
- El programa imprime un mensaje de confirmación.

### Ejemplo Completo 2:
```python
ruta = "C:/Users/TuUsuario/Documentos/mi_archivo.txt"

# Abrir el archivo en modo escritura
archivo = open(ruta, "w")

# Escribir en el archivo
archivo.write("Esta es una línea de texto.\n")
archivo.write("Esta es otra línea.\n")

# Cerrar el archivo explícitamente
archivo.close()

print("El archivo se ha guardado correctamente.")
```
### Explicación:

- Abrir el archivo: Usamos `open(ruta, "w")` para abrir el archivo en modo escritura `("w")`. Esto crea el archivo si no existe, o lo sobrescribe si ya existe.
- Escribir en el archivo: Usamos `archivo.write()` para escribir líneas de texto en el archivo.
- Cerrar el archivo manualmente: Llamamos a `archivo.close()` para cerrar el archivo explícitamente. Esto es importante para liberar los recursos del sistema asociados al archivo (como el bloqueo del archivo) y asegurarnos de que los datos se escriban correctamente en el disco.

### ¿Por qué es importante cerrar los archivos?

1. **Liberar recursos:** Los archivos abiertos consumen recursos del sistema operativo. Si no los cierras, puedes encontrarte con problemas como límites en el número de archivos abiertos o errores de "archivo en uso".
2. **Garantizar la escritura:** En algunos casos, los datos que escribes en un archivo pueden no guardarse en el disco inmediatamente. Cerrar el archivo asegura que todos los datos pendientes se escriban correctamente.

### Comparación con with:

La sentencia `with` proporciona una forma más segura y conveniente de trabajar con archivos. Se encarga automáticamente de cerrar el archivo al final del bloque, incluso si ocurre una excepción.

```python
with open(ruta, "w") as archivo:
    # ... operaciones con el archivo ...
# El archivo se cierra automáticamente aquí
```

### ¿Cuándo usar `archivo.close()`?

Si bien with es la forma recomendada de trabajar con archivos en Python, puede haber situaciones en las que necesites cerrar un archivo manualmente:

- **Flexibilidad:** Si necesitas abrir y cerrar un archivo varias veces dentro de un bloque de código más grande.
- **Compatibilidad:** Si estás trabajando con código antiguo que no utiliza with.

## 🔴🔴🔴🔴🔴🔴 ¡Atención!🔴🔴🔴🔴🔴🔴🔴

### **Siempre recuerda cerrar los archivos que abres manualmente. Si no lo haces, puedes causar problemas en tu programa y en tu sistema operativo.**

# Lectura de Archivos en Python: ¡Recupera tus Datos del Disco Duro! 💾
- Imagina que has guardado un tesoro en un cofre 🏴‍☠️. Ahora, necesitas abrir el cofre y examinar sus contenidos. En Python, leer un archivo es como abrir ese cofre y descubrir la información que has almacenado.

### Abriendo el Cofre: ¡Modo Lectura! 📖
Para leer un archivo, primero debes abrirlo en modo lectura ("r"). Esto le indica a Python que solo quieres acceder a los datos del archivo, no modificarlos.

```python
ruta = "ruta/a/tu/archivo.txt"  # Reemplaza con la ruta real de tu archivo

with open(ruta, "r") as archivo:
    # ... aquí va el código para leer el archivo ...
```

### Tres Formas de Leer: ¡Elige tu Estilo! 🔍
Python te ofrece tres métodos principales para leer archivos de texto:

1. `read()`: Lee todo el contenido del archivo de una vez y lo devuelve como una sola cadena de texto.

```python
with open(ruta, "r") as archivo:
    contenido_completo = archivo.read()
    print(contenido_completo)
```

2. `readline():` Lee una línea del archivo a la vez. Cada vez que llamas a readline(), obtienes la siguiente línea del archivo.

```python
with open(ruta, "r") as archivo:
    linea1 = archivo.readline()
    linea2 = archivo.readline()
    print(linea1)
    print(linea2)
```

3. `readlines():` Lee todas las líneas del archivo y las devuelve como una lista de cadenas de texto.

```python
with open(ruta, "r") as archivo:
    todas_las_lineas = archivo.readlines()
    for linea in todas_las_lineas:
        print(linea.strip())  # Eliminamos los saltos de línea (\n)
```

### ¿Cuál método usar? 🤔
1. `read():` Ideal para archivos pequeños que quieres cargar completamente en memoria.
2. `readline():` Útil cuando quieres procesar el archivo línea por línea, especialmente si el archivo es grande y no quieres cargarlo todo en memoria.
3. `readlines():` Conveniente cuando necesitas acceder a todas las líneas del archivo como una lista.

### ¡Un Consejo Extra! 💡
Si no sabes qué método usar, prueba con readlines() y luego itera sobre la lista de líneas. Es una forma flexible de trabajar con archivos de texto.

```python
with open(ruta, "r") as archivo:
    for linea in archivo:  # Itera sobre cada línea del archivo
        print(linea.strip())
```

# `seek()` para Navegar por el Archivo 🧭

- La función `seek()` te permite moverte a una posición específica dentro de un archivo abierto. Es como tener un marcador de libros que puedes colocar en cualquier página para empezar a leer desde allí.

### Como se escribe:

```python
archivo.seek(offset)
```

- `offset:` Indica cuántas posiciones quieres moverte.



### Ejemplo:

```python
with open("datos.txt", "r") as archivo:
    archivo.seek(15)  # Mover el cursor a la posición 15
    datos = archivo.read(10)  # Leer 10 caracteres desde esa posición
    print(datos) 
```

### Explicación:

- 1. Abrimos el archivo datos.txt en modo lectura.
- 2. Usamos seek(15) para mover el cursor a la posición 15 (contando desde el inicio del archivo).
- 3. Usamos read(10) para leer 10 caracteres desde esa posición.
- 4. Imprimimos los caracteres leídos.

# Archivos JSON: ¡Organiza tus Datos como un Profesional! 🗂️
**JSON (JavaScript Object Notation)** es un formato ligero y popular para almacenar y transmitir datos estructurados. Es como una receta escrita en un lenguaje universal que cualquier programa puede entender. 🌍

### ¿Por qué usar JSON? 🤔
- Legibilidad: Los archivos JSON son fáciles de leer y escribir tanto para humanos como para máquinas.
- Interoperabilidad: JSON es compatible con muchos lenguajes de programación, lo que facilita el intercambio de datos entre diferentes sistemas.
- Estructura flexible: Puedes representar datos complejos como objetos, arrays y valores primitivos (números, cadenas, booleanos).

### Trabajando con JSON en Python: ¡El Módulo json al Rescate! 🦸
Python incluye el módulo json que te permite leer y escribir datos en formato JSON de forma sencilla.

### Ejemplo de archivo JSON (datos.json):

```JSON
{
    "clientes": [
        {
            "nombre": "Sigrid",
            "apellido": "Mannock",
            "edad": 27,
            "monto": 7.17
        },
        {
            "nombre": "Joe",
            "apellido": "Hinners",
            "edad": 31,
            "monto": [1.9, 5.5]
        },
        {
            "nombre": "Theodoric",
            "apellido": "Rivers",
            "edad": 36,
            "monto": 1.11
        }
    ]
}
```

### Leer un archivo JSON:

```python
import json

with open("datos.json", "r") as archivo:
    datos = json.load(archivo)  # Cargamos el JSON en un diccionario de Python

print(datos["clientes"][0]["nombre"])  # Output: Sigrid
```

### Escribir un archivo JSON:

```python
import json

nuevos_datos = {
    "clientes": [
        {"nombre": "Eva", "apellido": "Smith", "edad": 22, "monto": 3.55}
    ]
}

with open("nuevos_datos.json", "w") as archivo:
    json.dump(nuevos_datos, archivo, indent=4)  # Guardamos el diccionario como JSON con indentación
```



