"""
Responsable: Integrante 2 (ya implementado por el equipo en Ejercicio 2)
Caso principal: resta de dos números.
Subcaso: resta con negativos.
Nota: reutilizar la lógica ya probada en bughunters-resta-provisional.
"""
from validacion import validar_numero


def _validar_operandos(a: float, b: float) -> None:
    """Valida los dos operandos de una resta."""
    validar_numero(a)
    validar_numero(b)


def resta(a: float, b: float) -> float:
    """Caso principal: retorna la resta a - b."""
    _validar_operandos(a, b)
    return a - b


def resta_negativos(a: float, b: float) -> float:
    """Subcaso: permite realizar restas con números negativos."""
    _validar_operandos(a, b)
    return a - b