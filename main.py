#Crea un código que imprima en pantalla la expresión “Mi Primer Código En Python.”

print("Mi primer código en Python")
#Crea un código que imprima en pantalla la siguiente expresión.

print("1\tA\tB\tC\n2\tD\tE\tF\n3\tG\tH\tI")
#Crea un código que le permita ingresar una respuesta al usuario, haciéndole la siguiente pregunta:¿Qué estás estudiando?
#El código debe poder imprimir en pantalla lo ingresado por el usuario (utilizando print).

respuesta = input(" Qué estas estudiando? :")

print(respuesta)
# Crea un código que le permita ingresar una respuesta al usuario, haciéndole la siguiente pregunta:¿En qué país vives?
#El código debe poder imprimir en pantalla lo ingresado por el usuario (utilizando print).

pais = input("En qué país vives?")
print(pais)
# Declara dos variables, llamadas nombre y edad. Asigna a la variable nombre el valor "David Bowman", y a la edad, el valor 51.
nombre = "David Bowman"
edad = 51
#Crea tres variables: nombre, apellido y nombrecompleto. A nombre, asígnale el valor "Julia", y en apellido, asigna el valor "Roberts". Finalmente, construye la variable nombrecompleto concatenando las variables (recuerda sumar un espacio intermedio).
nombre= "Julia"
apellido = "Roberts"
nombrecompleto = nombre  + " " + apellido

#        2.7. Declara la variable materia, asígnale el valor "Ingeniería del conocimiento", y muestra en pantalla la frase:
#        Estás estudiando “materia”

materia =  "Ingeniería del conocimiento"

print( "Estoy estudiando " + materia)

#Convierte el valor de num1 (num1=35) en un int e imprime el tipo de dato que resulta

num= int(35)
print(type(num))

#Necesitamos imprimir el nombre y número de asociado dentro de la siguiente frase:“Estimado/a (nombre_asociado), su número de asociado es: (numero_asociado)”
nombre_asociado = input("Ingrese su nombre: ")
numero_asociado = input("Ingrese su número de asociado: ")

print("Estimado/a " + nombre_asociado+ ", su número de asociado es: " + numero_asociado)
#Muestra en pantalla el cociente (división al piso) de los siguientes dos números: 874 dividido entre 27.

resultado = 874 / 27
print(resultado)
#Redondea el número 10.676767 al entero más próximo, y muestra en pantalla el resultado.

numero = 10.676767
resultado = round(numero)

print(resultado)
#Gestión de inventario con tuplas:
#Consigna: Una tienda tiene un inventario de productos, cada producto tiene un nombre, precio y cantidad disponible.
# Representa cada producto como una tupla (nombre, precio, cantidad).
# Escribe una función que reciba una lista de productos (tuplas) y devuelva el producto más caro.

productos = [ ("laptop", 1200, 5), ("mouse", 25, 50), ("teclado", 100, 30) ]

def mas_caro(productos):
    producto_mas_caro = productos[0]

    for producto in productos:
        if producto[1] > producto_mas_caro[1]:
            producto_mas_caro = producto

    return producto_mas_caro
resultado = mas_caro(productos)

print("El producto más caro es:", resultado)


#Consigna: Una escuela lleva un registro de estudiantes donde la clave es el número de matrícula y el valor es un diccionario con nombre,
# edad y calificaciones en distintas materias.
# Escribe una función que reciba el registro de estudiantes y devuelva el promedio de calificaciones de un estudiante dado su número de matrícula.

estudiantes = {
    101: {"nombre": "Ana", "edad": 16, "calificaciones": {"matemáticas": 85, "ciencias": 90}},
    102: {"nombre": "Luis", "edad": 17, "calificaciones": {"matemáticas": 78, "ciencias": 88}}
}

def promedio_calificaciones(registro, matricula):
    if matricula in registro:
        calificaciones = registro[matricula]["calificaciones"]
        promedio = sum(calificaciones.values()) / len(calificaciones)
        return promedio
    else:
        return None
#Un meteorólogo registra las temperaturas diarias durante un mes y las almacena en un array. 
# Escribe una función que reciba este array y devuelva la temperatura media del mes, la máxima y la mínima.

temperaturas = [22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]

def estadisticas_temperaturas(temperaturas):
    temperatura_media = sum(temperaturas) / len(temperaturas)
    temperatura_maxima = max(temperaturas)
    temperatura_minima = min(temperaturas)
    
    return temperatura_media, temperatura_maxima, temperatura_minima
#Escribe una función que reciba un número variable de notas de estudiantes y devuelva la nota promedio. 
# Utiliza *args para recibir las notas.

def promedio_notas(*notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

#Creación de un perfil de usuario con **kwargs:

#Consigna: Escribe una función que reciba datos de un usuario como nombre, edad, correo electrónico, y cualquier otro dato adicional usando **kwargs. 
# La función debe devolver un diccionario con toda la información del usuario.

def crear_perfil(nombre, edad, email, **kwargs):
    perfil = {
        "nombre": nombre,
        "edad": edad,
        "email": email
    }

    perfil.update(kwargs)

    return perfil


usuario = crear_perfil(
    nombre="Luis",
    edad=25,
    email="juan@mail.com",
    ciudad="Mendoza"
)

print(usuario)

kwargs = {"ciudad": "Mendoza"}

#Consigna: Una empresa quiere administrar la información de sus empleados, donde cada empleado se representa como una tupla (nombre, edad, salario). Escribe una función que reciba un diccionario donde la clave es el ID del empleado y el valor es la tupla con su información. La función debe devolver un diccionario con los empleados que ganan más de un salario dado.
empleados = {
    1: ("Ana", 30, 3000),
    2: ("Luis", 25, 2500),
    3: ("María", 35, 4000)
}
def empleados_con_salario_mayor_a(empleados, salario):
    empleados_filtrados = {}
    for id_empleado, info in empleados.items():
        if info[2] > salario:
            empleados_filtrados[id_empleado] = info
    return empleados_filtrados
#Consigna: Una tienda quiere procesar sus ventas diarias almacenadas en un array. Escribe una función que reciba el array de ventas diarias y devuelva el total de ventas y el promedio de ventas por día.

ventas_diarias = [200, 450, 300, 400, 350, 500, 600]

def total_y_promedio_ventas(ventas):
    total_ventas = sum(ventas)
    promedio_ventas = total_ventas / len(ventas)
    return total_ventas, promedio_ventas
# Un club deportivo registra los resultados de sus partidos en un diccionario donde la clave es el nombre del equipo rival y el valor es una tupla con los goles anotados y recibidos.
#  Escribe una función que calcule el total de goles anotados y recibidos en la temporada.

resultados = {
    "Equipo A": (3, 2),
    "Equipo B": (1, 1),
    "Equipo C": (4, 0)
}

def total_goles_temporada(resultados):
    total_anotados = sum(goles[0] for goles in resultados.values())
    total_recibidos = sum(goles[1] for goles in resultados.values())
    return total_anotados, total_recibidos

# Escribe una función que reciba configuraciones opcionales para una aplicación como modo oscuro, idioma, notificaciones, etc., usando **kwargs. 
# La función debe devolver un diccionario con las configuraciones aplicadas.

def configurar_app(**kwargs):
    configuraciones = {
        "modo_oscuro": False,
        "idioma": "en",
        "notificaciones": True
    }

    configuraciones.update(kwargs)

    return configuraciones


configurar_app(modo_oscuro=True, idioma="es", notificaciones=False)

#Escribe una función que reciba una lista de tuplas donde cada tupla contiene un nombre y una puntuación. 
# La función debe devolver la lista ordenada por puntuación de mayor a menor.

puntuaciones = [("Ana", 85), ("Luis", 90), ("María", 78)]

def ordenar_puntuaciones(puntuaciones):
    return sorted(puntuaciones, key=lambda x: x[1], reverse=True)

print(ordenar_puntuaciones(puntuaciones))
# lanificación de viajes con tuplas y diccionarios:

#Consigna: Una agencia de viajes tiene diferentes paquetes turísticos, cada uno representado como una tupla (destino, precio, duración en días). Escribe una función que reciba una lista de estos paquetes y devuelva un diccionario con los destinos como claves y el precio total (precio por día * duración) como valor.

paquetes = [
    ("Paris", 200, 5),
    ("Roma", 150, 4),
    ("Londres", 180, 3)
]

def calcular_precio_total(paquetes):
    return {destino: precio * duracion for destino, precio, duracion in paquetes}

#Una tienda maneja su inventario de productos en un array donde cada índice representa un producto específico y su valor es la cantidad disponible. Escribe una función que reciba el array de inventario y un número de productos vendidos (otro array) y devuelva el inventario actualizado.

inventario = [50, 30, 20, 10]
ventas = [5, 10, 5, 2]

def actualizar_inventario(inventario, ventas):
    return [inventario[i] - ventas[i] for i in range(len(inventario))]
#Escribe una función que reciba un número variable de nombres de eventos y los imprima en un formato de lista numerada. Utiliza *args para recibir los nombres de los eventos.

def organizar_eventos(*eventos):
    for i, evento in enumerate(eventos, start=1):
        print(f"{i}. {evento}")

organizar_eventos("Concierto", "Exposición de arte", "Conferencia")

#Escribe una función que reciba diferentes tipos de ingresos y gastos como **kwargs y calcule el balance final. La función debe manejar ingresos como positivos y gastos como negativos.

def analizar_finanzas(**finanzas):
    balance = sum(valor for tipo, valor in finanzas.items() if tipo != "gastos")
    gastos = sum(valor for tipo, valor in finanzas.items() if tipo == "gastos")
    return balance - gastos

print(analizar_finanzas(sueldo=2000, renta=-800, transporte=-150, comida=-300, freelance=500))

#Escribe una función que reciba el nombre, edad, y salario de un empleado como parámetros obligatorios, y otros datos como dirección, número de teléfono, etc., como **kwargs. La función debe devolver un diccionario con toda la información del empleado.

def registro_empleado(nombre, edad, salario, **datos_adicionales):
    empleado = {
        "nombre": nombre,
        "edad": edad,
        "salario": salario
    }
    empleado.update(datos_adicionales)
    return empleado

print(registro_empleado("Ana", 30, 3000, direccion="Calle Falsa 123", telefono="123456789"))

#Escribe una función que reciba un array con las ventas de cada mes y devuelva un diccionario con el total de ventas, el promedio mensual, y el mes con mayores ventas.

ventas_mensuales = [2000, 2500, 3000, 2800, 3500, 4000, 4200, 3800, 3600, 3900, 4100, 4500]

def analizar_ventas(ventas):
    total = sum(ventas)
    promedio = total / len(ventas)
    max_venta = max(ventas)
    mes_max = ventas.index(max_venta) + 1
    return {
        "total": total,
        "promedio": promedio,
        "mes_max": mes_max,
        "max_venta": max_venta
    }

print(analizar_ventas(ventas_mensuales))
#Una biblioteca registra sus libros en un diccionario donde la clave es el título del libro y el valor es otro diccionario con la información del autor, año de publicación, y género. Escribe una función que reciba este diccionario y devuelva una lista de todos los libros publicados después del año 2000.

biblioteca = {
    "El señor de los anillos": {"autor": "J.R.R. Tolkien", "año": 1954, "género": "Fantasía"},
    "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "género": "Realismo mágico"},
    "El código Da Vinci": {"autor": "Dan Brown", "año": 2003, "género": "Suspenso"}
}

def libros_despues_2000(biblioteca):
    return [titulo for titulo, info in biblioteca.items() if info["año"] > 2000]

print(libros_despues_2000(biblioteca))

#Escribe una función que reciba una lista de tuplas donde cada tupla contiene el nombre de un estudiante y sus calificaciones en un array. La función debe devolver un diccionario con el nombre del estudiante como clave y su promedio de calificaciones como valor.

notas_estudiantes = [
    ("Ana", [85, 90, 78]),
    ("Luis", [88, 92, 80]),
    ("María", [75, 85, 70])
]

def calcular_promedios(notas):
    return {nombre: sum(calificaciones) / len(calificaciones) for nombre, calificaciones in notas}

print(calcular_promedios(notas_estudiantes))

#Escribe una función que reciba una lista de usuarios y sus preferencias de configuración como **kwargs. La función debe devolver un diccionario donde la clave es el nombre del usuario y el valor es un array con las configuraciones aplicadas.

usuarios = ["Ana", "Luis", "María"]
configurar_perfiles(usuarios, idioma="es", modo_oscuro=True, notificaciones=False)


def configurar_perfiles(usuarios, **kwargs):
    perfiles = {}
    for usuario in usuarios:
        perfiles[usuario] = kwargs
    return perfiles

#Escribe una función que administre publicaciones de una red social. La función debe recibir el nombre del usuario, el texto de la publicación y un número variable de etiquetas usando **kwargs y arrays. Además, debe manejar opciones adicionales como visibilidad pública o privada. La función debe devolver un diccionario con todos los detalles de la publicación.
def publicar(nombre_usuario, texto_publicacion, etiquetas=None, visibilidad="publica", likes=0):
    if etiquetas is None:
        etiquetas = []
    publicacion = {
        "usuario": nombre_usuario,
        "texto": texto_publicacion,
        "etiquetas": etiquetas,
        "visibilidad": visibilidad,
        "likes": likes
    }
    return publicacion
publicar("Juan", "Mi primer post!", etiquetas=["#hola", "#primerPost"], visibilidad="publica", likes=100)
#Una empresa quiere simular las ventas de diferentes productos. Escribe una función que reciba un número variable de ventas (tuplas) donde cada tupla contiene el producto, la cantidad vendida, y el precio por unidad. La función debe devolver el total de ingresos generados por las ventas.

def simular_ventas(*ventas):
    total = 0
    for producto, cantidad, precio in ventas:
        total += cantidad * precio
    return total

print(simular_ventas(("Producto A", 10, 15.0), ("Producto B", 5, 25.0), ("Producto C", 3, 50.0)))

#Un hotel maneja sus reservas utilizando un diccionario donde la clave es la fecha y el valor es una lista de tuplas, cada tupla contiene el nombre del huésped, la habitación asignada y el precio. Escribe una función que permita hacer una nueva reserva verificando primero si la habitación está disponible en la fecha seleccionada.

reservas = {
    "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
    "2024-08-16": [("Luis", 101, 150)]
}

def hacer_reserva(fecha, nombre_huesped, habitacion, precio):
    if fecha in reservas:
        for huesped, room, cost in reservas[fecha]:
            if room == habitacion:
                return False  # La habitación no está disponible
    else:
        reservas[fecha] = []

    reservas[fecha].append((nombre_huesped, habitacion, precio))
    return True

#Una empresa realiza encuestas de satisfacción y registra las respuestas en un diccionario donde la clave es la pregunta y el valor es un array con las respuestas recibidas. Escribe una función que calcule la frecuencia de cada respuesta para cada pregunta y devuelva un diccionario con estos resultados.

encuestas = {
    "¿Cómo califica el servicio?": [5, 4, 5, 3, 5, 4],
    "¿Recomendaría nuestro producto?": [1, 1, 0, 1, 1, 0]
}

def calcular_frecuencias(encuestas):
    frecuencias = {}
    for pregunta, respuestas in encuestas.items():
        frecuencias[pregunta] = {}
        for respuesta in respuestas:
            if respuesta in frecuencias[pregunta]:
                frecuencias[pregunta][respuesta] += 1
            else:
                frecuencias[pregunta][respuesta] = 1
    return frecuencias

print(calcular_frecuencias(encuestas))

#Una empresa de logística necesita optimizar sus rutas de entrega. Cada ruta se representa como una tupla (origen, destino, distancia). Escribe una función que reciba una lista de rutas y un array con las distancias máximas permitidas para cada ruta. La función debe devolver las rutas que cumplen con las restricciones.

rutas = [("Madrid", "Barcelona", 620), ("Madrid", "Valencia", 350), ("Barcelona", "Valencia", 350)]
distancias_max = [600, 400, 500]

def optimizar_rutas(rutas, distancias_max):
    rutas_optimizadas = []
    for i, (origen, destino, distancia) in enumerate(rutas):
        if distancia <= distancias_max[i]:
            rutas_optimizadas.append((origen, destino, distancia))
    return rutas_optimizadas

print(optimizar_rutas(rutas, distancias_max))
#Escribe una función que gestione el inventario de una cadena de tiendas. La función debe recibir el nombre de la tienda, el producto y la cantidad a actualizar usando **kwargs. Debe manejar un diccionario donde la clave es el nombre de la tienda y el valor es otro diccionario con los productos y sus cantidades. La función debe actualizar el inventario y devolver el estado actual.
inventario = {

    "Tienda A": {"producto_1": 50, "producto_2": 30},
    "Tienda B": {"producto_1": 20, "producto_2": 40}
}
def actualizar_inventario(**kwargs):
    tienda = kwargs.get("tienda")
    if tienda not in inventario:
        inventario[tienda] = {}

    for producto, cantidad in kwargs.items():
        if producto != "tienda":
            if producto in inventario[tienda]:
                inventario[tienda][producto] += cantidad
            else:
                inventario[tienda][producto] = cantidad

    return inventario

print(actualizar_inventario(tienda="Tienda A", producto_1=10, producto_2=-5))

#         Una empresa de marketing digital desea analizar las tendencias de hashtags en las redes sociales. Escribe una función que reciba un array de hashtags y una lista de tuplas donde cada tupla contiene un hashtag y su frecuencia de uso. La función debe devolver los hashtags que han sido mencionados más de una cierta cantidad de veces.

hashtags = ["#verano", "#moda", "#viajes", "#verano", "#moda", "#tecnologia"] 
tendencias = [("#verano", 120), ("#moda", 80), ("#tecnologia", 150)]

def analizar_tendencias(hashtags, tendencias, umbral):
    hashtags_filtrados = []
    for hashtag in hashtags:
        for h, frecuencia in tendencias:
            if hashtag == h and frecuencia > umbral:
                hashtags_filtrados.append(hashtag)
    return hashtags_filtrados

print(analizar_tendencias(hashtags, tendencias, 100))

#scribe una función que gestione las suscripciones a un servicio en línea. La función debe recibir el nombre del usuario, el tipo de suscripción (mensual, anual), y cualquier o	tra opción adicional usando **kwargs. La función debe actualizar un diccionario que almacene el historial de suscripciones de los usuarios y devolver el estado actualizado.

suscripciones = {
    "Jose": ["mensual", "anual"],
    "Ana": ["mensual"]
}
def actualizar_suscripcion(**kwargs):
    usuario = kwargs.get("usuario")
    if usuario not in suscripciones:
        suscripciones[usuario] = []

    suscripcion = kwargs.get("suscripcion")
    if suscripcion:
        suscripciones[usuario].append(suscripcion)

    return suscripciones

print(actualizar_suscripcion(usuario="Luis", suscripcion="mensual", auto_renovacion=True))
#Escribe una función que simule el comportamiento de acciones en un mercado bursátil. La función debe recibir un array con los precios diarios de una acción y una lista de tuplas donde cada tupla contiene un día y un precio de compra o venta. La función debe devolver el beneficio o pérdida total si las acciones se hubieran comprado y vendido en los días especificados.

precios_diarios = [100, 105, 102, 110, 108]
operaciones = [("compra", 0), ("venta", 3), ("compra", 2), ("venta", 4)]

def simular_mercado_bursatil(precios, operaciones):
    beneficio_total = 0
    for tipo, dia in operaciones:
        precio = precios[dia]
        if tipo == "compra":
            beneficio_total -= precio
        elif tipo == "venta":
            beneficio_total += precio
    return beneficio_total

print(simular_mercado_bursatil(precios_diarios, operaciones))
#Una universidad lleva un registro de las calificaciones de los estudiantes en diferentes materias. Cada estudiante tiene un ID único y su información se almacena en un diccionario donde la clave es el ID y el valor es otro diccionario con las materias y sus respectivas calificaciones (arrays). Escribe una función que reciba este diccionario y devuelva un ranking de estudiantes basado en su promedio general.


estudiantes = {
    101: {"matemáticas": [85, 90, 78], "ciencias": [88, 85, 80]},
    102: {"matemáticas": [92, 88, 84], "ciencias": [75, 80, 85]},
    103: {"matemáticas": [78, 85, 88], "ciencias": [90, 95, 92]}
}

def ranking_estudiantes(estudiantes_dict):
    promedios = []
    for id_estudiante, materias in estudiantes_dict.items():
        calificaciones = [cal for notas in materias.values() for cal in notas]
        promedio = sum(calificaciones) / len(calificaciones)
        promedios.append((id_estudiante, promedio))
    return sorted(promedios, key=lambda x: x[1], reverse=True)

print(ranking_estudiantes(estudiantes))