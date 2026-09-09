"""
Responsable: Arias Grageda Mayra
Caso principal: división de dos números (con manejo de división por cero).
Subcaso: división entera + residuo (divmod).

Nota (corrección Git Leader): se reescribió como función pura, rescatando
la lógica de signos que ya estaba en la versión original de Mayra, pero
sin input()/print() para que sea compatible con el menú y los tests.
"""
from validacion import validar_numero


def division(a: float, b: float) -> float:
    """Caso principal: divide a entre b."""
    validar_numero(a)
    validar_numero(b)
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return a / b


def division_entera(a: float, b: float) -> tuple:
    """Subcaso: retorna (cociente entero, residuo)."""
    validar_numero(a)
    validar_numero(b)
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return divmod(a, b)