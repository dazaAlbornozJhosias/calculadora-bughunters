"""
Responsable: Integrante 2 (ya implementado por el equipo en Ejercicio 2)
Caso principal: resta de dos números.
Subcaso: resta con negativos.
Nota: reutilizar la lógica ya probada en bughunters-resta-provisional.
"""
from validacion import validar_numero


def resta(a: float, b: float) -> float:
    """Caso principal: resta a - b."""
    validar_numero(a)
    validar_numero(b)
    return a - b


def resta_negativos(a: float, b: float) -> float:
    """Subcaso: resta explícita con operandos negativos (función pura, sin input())."""
    validar_numero(a)
    validar_numero(b)
    return a - b
