# funciones_intermedias_1.py — Código completo
# ================================
# Actualizar valores en diccionarios y listas
# ================================

# Ejemplo de estructuras para practicar actualizaciones:
x = [ [5, 2, 3], [10, 8, 9] ]
estudiantes = [
    {"nombre": "Michael", "apellido": "Jordan"},
    {"nombre": "John", "apellido": "Rosales"}
]
deportes = {
    "basketball": ["Kobe", "Jordan", "James"],
    "futbol": ["Messi", "Ronaldo", "Rooney"]
}
z = [{"x": 10, "y": 20}]

# Ejemplos de actualizaciones:
x[1][0] = 15
estudiantes[0]["apellido"] = "Bryant"
deportes["futbol"][0] = "Andrés"
z[0]["y"] = 30


# ================================
# 1. iterarDiccionario(lista)
# Recorre una lista de diccionarios e imprime cada par clave-valor.
# ================================
def iterarDiccionario(lista):
    for dic in lista:
        salida = ""
        for clave, valor in dic.items():
            salida += f"{clave} - {valor}, "
        print(salida.rstrip(", "))


# ================================
# 2. iterarDiccionario2(llave, lista)
# Imprime solo los valores asociados a una llave específica.
# ================================
def iterarDiccionario2(llave, lista):
    for dic in lista:
        if llave in dic:
            print(dic[llave])
        else:
            print(f"La llave '{llave}' no existe en el diccionario.")


# ================================
# 3. imprimirInformacion(diccionario)
# Recibe un diccionario cuyas llaves tienen listas como valores.
# Imprime la cantidad de elementos y luego cada elemento.
# ================================
def imprimirInformacion(diccionario):
    for clave, lista in diccionario.items():
        print(f"{len(lista)} {clave.upper()}")
        for elemento in lista:
            print(elemento)
        print()  # línea en blanco para separar secciones


# ================================
# Ejemplos de prueba (puedes borrarlos si no los necesitas)
# ================================
if __name__ == "__main__":
    estudiantes = [
        {"nombre": "Michael", "apellido": "Jordan"},
        {"nombre": "John", "apellido": "Rosales"},
        {"nombre": "Mark", "apellido": "Guillen"},
        {"nombre": "KB", "apellido": "Tonel"}
    ]

    print("=== iterarDiccionario ===")
    iterarDiccionario(estudiantes)

    print("\n=== iterarDiccionario2('nombre') ===")
    iterarDiccionario2("nombre", estudiantes)

    print("\n=== imprimirInformacion ===")
    dojo = {
        "ubicaciones": ["San Jose", "Seattle", "Dallas"],
        "instructores": ["Michael", "Amy", "Eduardo"]
    }
    imprimirInformacion(dojo)
