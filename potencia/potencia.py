"""
Responsable: Integrante 5
Caso principal: potenciación (base ^ exponente).
Subcaso: exponente negativo (resultado fraccionario).
"""
from validacion import validar_numero


def potencia(base: float, exponente: float) -> float:
    """Caso principal: eleva base a exponente."""
    validar_numero(base)
    validar_numero(exponente)
    # TODO: implementar/ajustar (considerar caso 0 ** 0 si aplica)
    # Manejo de casos matematicos no definidos o especiales
    if base == 0 and exponente == 0:
        raise ValueError("Indefinicion matematica: 0 elevado a la 0 no esta determinado")
    return base ** exponente


def potencia_negativa(base: float, exponente: float) -> float:
    """Subcaso: maneja explicitamente exponentes negativos."""
    validar_numero(base)
    validar_numero(exponente)
    if base == 0 and exponente < 0:
        raise ZeroDivisionError("No se puede elevar 0 a un exponente negativo")
    return base ** exponente