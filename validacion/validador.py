"""
Responsable: Integrante 9
Validaciones reutilizables por TODOS los módulos de operaciones.
Mantener estas funciones puras (sin input(), sin print()).
"""
import math


def validar_numero(valor):
    """Valida que 'valor' sea un número real (no NaN, no infinito)."""
    if not isinstance(valor, (int, float)):
        raise TypeError(f"Se esperaba un número, se recibió {type(valor).__name__}")
    if isinstance(valor, float) and (math.isnan(valor) or math.isinf(valor)):
        raise ValueError("El valor no puede ser NaN ni infinito")
    return True


def validar_lista(lista):
    """Valida que 'lista' sea una lista no vacía de números válidos."""
    if not isinstance(lista, list):
        raise TypeError("Se esperaba una lista")
    if len(lista) == 0:
        raise ValueError("La lista no puede estar vacía")
    for elemento in lista:
        validar_numero(elemento)
    return True


def validar_matriz(matriz):
    """Valida que 'matriz' sea una lista de listas no vacía, con filas del mismo tamaño."""
    if not isinstance(matriz, list) or len(matriz) == 0:
        raise ValueError("La matriz no puede estar vacía")
    ancho = len(matriz[0])
    for fila in matriz:
        validar_lista(fila)
        if len(fila) != ancho:
            raise ValueError("Todas las filas deben tener el mismo tamaño")
    return True
