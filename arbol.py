# Trabajo Práctico Integrador - Programación I
# Tema: Árboles en Python
# Descripción: Implementación de un Árbol Binario de Búsqueda (ABB)
# Alumnos: Lis Araceli Lezcano Thomas y Axel Nicolás Gómez Sosa
# Archivo: arboles.py
# Fecha: 09 Junio 2025

class Nodo: 

#     Clase que representa un nodo del árbol binario

    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def insertar(nodo, valor):

#     Inserta un valor en el árbol de forma recursiva

    if nodo is None:
        return Nodo(valor)
    if valor < nodo.valor:
        nodo.izquierda = insertar(nodo.izquierda, valor)
    else:
        nodo.derecha = insertar(nodo.derecha, valor)
    return nodo

def buscar(nodo, valor):
    
#     Busca un valor en el árbol de forma recursiva
    
    if nodo is None or nodo.valor == valor:
        return nodo
    if valor < nodo.valor:
        return buscar(nodo.izquierda, valor)
    else:
        return buscar(nodo.derecha, valor)

# ---------------------
# Código principal
# ---------------------

valores = [50, 30, 70, 20, 40, 60, 80]
raiz = None

# Inserta valores en el árbol
for valor in valores:
    raiz = insertar(raiz, valor)

# Busca un valor específico
valor_buscado = 60
resultado = buscar(raiz, valor_buscado)

# Muestra resultado
if resultado:
    print(f"El valor {valor_buscado} fue encontrado en el árbol.")
else:
    print(f"El valor {valor_buscado} no se encuentra en el árbol.")
