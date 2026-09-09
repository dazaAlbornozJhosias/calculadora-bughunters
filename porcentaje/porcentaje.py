"""
Responsable: Rodrigo Mamani Rocha
Caso principal: calcular el X% de un número.
Subcaso 1: variación porcentual entre dos valores.
Subcaso 2: cálculo de descuento porcentual aplicado a un precio/valor.
"""
from validacion import validar_numero


def porcentaje(numero: float, porcentaje_valor: float) -> float:
    """Caso principal: calcula el porcentaje_valor % de numero."""
    validar_numero(numero)
    validar_numero(porcentaje_valor)
    return (numero * porcentaje_valor) / 100


def variacion_porcentual(valor_inicial: float, valor_final: float) -> float:
    """
    Subcaso 1: calcula el % de variación entre dos valores.
    Fórmula: ((valor_final - valor_inicial) / valor_inicial) * 100
    Lanza ZeroDivisionError si el valor inicial es cero.
    """
    validar_numero(valor_inicial)
    validar_numero(valor_final)
    if valor_inicial == 0:
        raise ZeroDivisionError("El valor inicial no puede ser cero")
    return ((valor_final - valor_inicial) / valor_inicial) * 100


def descuento(precio: float, porcentaje_descuento: float) -> float:
    """
    Subcaso 2: calcula el valor final tras aplicar un porcentaje de descuento.
    Fórmula: precio - porcentaje(precio, porcentaje_descuento)
    """
    validar_numero(precio)
    validar_numero(porcentaje_descuento)
    return precio - porcentaje(precio, porcentaje_descuento)
