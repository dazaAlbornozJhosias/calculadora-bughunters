"""
Responsable: Integrante 4
Caso principal: división de dos números (con manejo de división por cero).
Subcaso: división entera + residuo (divmod).
"""
from validacion import validar_numero


def division(a: float, b: float) -> float:
    """Caso principal: divide a entre b."""
    validar_numero(a)
    validar_numero(b)
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    # TODO: implementar/ajustar
    return a / b


def division_entera(a: float, b: float) -> tuple:
    """Subcaso: retorna (cociente entero, residuo)."""
    validar_numero(a)
    validar_numero(b)
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return divmod(a, b)
