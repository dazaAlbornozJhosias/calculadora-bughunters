"""
Responsable: Gael Olker Villarroel Sanchez
Caso principal: multiplicación de dos números.
Subcaso: multiplicación de todos los elementos de una lista (producto acumulado).
"""

from validacion import validar_numero, validar_lista


def multiplicacion(a: float, b: float) -> float:
    """
    Caso principal: multiplica dos números.
    """
    validar_numero(a)
    validar_numero(b)

    return a * b


def multiplicacion_lista(lista: list) -> float:
    """
    Subcaso: producto de todos los elementos de una lista.
    """
    validar_lista(lista)

    resultado = 1

    for elemento in lista:
        resultado *= elemento

    return resultado
