"""
Responsable: Ronald Escobar Vargas
Caso principal: suma de dos números (enteros/decimales/negativos).
Subcaso: suma de una lista de números.
"""
from validacion import validar_numero, validar_lista


def suma(a: float, b: float) -> float:
    """Caso principal: suma dos números."""
    validar_numero(a)
    validar_numero(b)
    return a + b


def suma_lista(lista: list) -> float:
    """Subcaso: suma todos los elementos de una lista."""
    validar_lista(lista)
    return sum(lista)
