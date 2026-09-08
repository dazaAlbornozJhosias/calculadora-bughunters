"""
Responsable: Integrante 1
Caso principal: suma de dos números (enteros/decimales/negativos).
Subcaso: suma de una lista de números.
"""
from validacion import validar_numero, validar_lista


def suma(a: float, b: float) -> float:
    """Caso principal: suma dos números."""
    validar_numero(a)
    validar_numero(b)
    # TODO: implementar/ajustar según casos que pida el docente
    return a + b


def suma_lista(lista: list) -> float:
    """Subcaso: suma todos los elementos de una lista."""
    validar_lista(lista)
    # TODO: implementar
    return sum(lista)
