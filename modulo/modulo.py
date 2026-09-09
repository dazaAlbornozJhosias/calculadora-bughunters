"""
Responsable: Integrante 6
Caso principal: módulo/residuo de dos números.
Subcaso: módulo con números negativos.
"""
import math
from validacion import validar_numero

def modulo(a: float, b: float) -> float:
    """Caso principal: residuo de a entre b."""
    validar_numero(a)
    validar_numero(b)
    if b == 0:
        raise ZeroDivisionError("No se puede calcular módulo entre cero")
    return a % b

def modulo_negativos(a: float, b: float) -> float:
    """
    Subcaso: verifica comportamiento matemático estricto con operandos negativos.
    A diferencia de '%', math.fmod conserva el signo del dividendo.
    """
    validar_numero(a)
    validar_numero(b)
    if b == 0:
        raise ZeroDivisionError("No se puede calcular módulo entre cero")
    return math.fmod(a, b)