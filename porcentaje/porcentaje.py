"""
Responsable: Integrante 8
Caso principal: calcular el X% de un número.
Subcaso: variación porcentual entre dos números.
"""
from validacion import validar_numero


def porcentaje(numero: float, porcentaje_valor: float) -> float:
    """Caso principal: calcula el porcentaje_valor % de numero."""
    validar_numero(numero)
    validar_numero(porcentaje_valor)
    # TODO: implementar/ajustar
    return (numero * porcentaje_valor) / 100


def variacion_porcentual(valor_inicial: float, valor_final: float) -> float:
    """Subcaso: calcula el % de variación entre dos valores."""
    validar_numero(valor_inicial)
    validar_numero(valor_final)
    if valor_inicial == 0:
        raise ZeroDivisionError("El valor inicial no puede ser cero")
    return ((valor_final - valor_inicial) / valor_inicial) * 100
