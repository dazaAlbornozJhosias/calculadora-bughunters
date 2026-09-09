"""
Responsable: Santiago Piscoya Bellido
Caso principal: raíz cuadrada de un número.
Subcaso: raíz n-ésima (con manejo de índice par + número negativo -> error).
"""
import math
from validacion import validar_numero


def raiz(numero, indice=2):
    
    validar_numero(numero)
    validar_numero(indice)

    if indice == 0:
        raise ValueError("El índice de la raíz no puede ser 0.")

    if numero < 0:
        if indice % 2 == 0:
            raise ValueError(
                "No existe raíz real de índice par para un número negativo."
            )
        return -((-numero) ** (1 / indice))

    return numero ** (1 / indice)


def raiz_cuadrada(numero):
    """Atajo para la raíz cuadrada (equivale a raiz(numero, 2))."""
    return raiz(numero, 2)
