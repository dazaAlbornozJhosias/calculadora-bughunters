"""
Responsable: Integrante 6
Caso principal: raíz cuadrada de un número.
Subcaso: raíz n-ésima (con manejo de índice par + número negativo -> error).
"""
import math
from validacion import validar_numero


def raiz_cuadrada(numero: float) -> float:
    """Caso principal: raíz cuadrada de un número."""
    validar_numero(numero)
    if numero < 0:
        raise ValueError("No existe raíz cuadrada real de un número negativo")
    # TODO: implementar/ajustar
    return math.sqrt(numero)


def raiz_n(numero: float, indice: int) -> float:
    """Subcaso: raíz n-ésima de un número."""
    validar_numero(numero)
    validar_numero(indice)
    if numero < 0 and indice % 2 == 0:
        raise ValueError("No existe raíz real de índice par para un número negativo")
    if numero < 0:
        return -(-numero) ** (1 / indice)
    return numero ** (1 / indice)
