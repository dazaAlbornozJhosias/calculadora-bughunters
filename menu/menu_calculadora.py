"""
Responsable: Art / Jhosias (Git Leader) - Integrante 10
Menú central de la calculadora. Debe RETORNAR el control al llamador,
nunca usar sys.exit(), para poder integrarse desde main.py.

Cada operación tiene un submenú con: caso principal + subcaso(s).
"""
from suma import suma, suma_lista
from resta import resta, resta_negativos
from multiplicacion import multiplicacion, multiplicacion_lista
from division import division, division_entera
from potencia import potencia, potencia_negativa
from raiz import raiz_cuadrada, raiz_n
from modulo import modulo, modulo_negativos
from porcentaje import porcentaje, variacion_porcentual, descuento


def _pedir_numero(mensaje: str) -> float:
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada inválida, intenta de nuevo.")


def _pedir_entero(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada inválida, ingresa un número entero.")


def _pedir_lista(mensaje: str) -> list:
    while True:
        entrada = input(mensaje).strip()
        try:
            return [float(x.strip()) for x in entrada.split(",") if x.strip() != ""]
        except ValueError:
            print("Entrada inválida. Usa números separados por coma, ej: 1,2,3")


def _ejecutar_binaria(funcion):
    a = _pedir_numero("Primer número: ")
    b = _pedir_numero("Segundo número: ")
    try:
        resultado = funcion(a, b)
        print(f"Resultado: {resultado}")
    except (ValueError, ZeroDivisionError, TypeError) as e:
        print(f"Error: {e}")


def _ejecutar_unaria(funcion):
    a = _pedir_numero("Número: ")
    try:
        resultado = funcion(a)
        print(f"Resultado: {resultado}")
    except (ValueError, ZeroDivisionError, TypeError) as e:
        print(f"Error: {e}")


def _ejecutar_lista(funcion):
    lista = _pedir_lista("Lista de números (separados por coma): ")
    try:
        resultado = funcion(lista)
        print(f"Resultado: {resultado}")
    except (ValueError, ZeroDivisionError, TypeError) as e:
        print(f"Error: {e}")


def _ejecutar_raiz_n(funcion):
    numero = _pedir_numero("Número: ")
    indice = _pedir_entero("Índice de la raíz (ej. 2 para cuadrada, 3 para cúbica): ")
    try:
        resultado = funcion(numero, indice)
        print(f"Resultado: {resultado}")
    except (ValueError, ZeroDivisionError, TypeError) as e:
        print(f"Error: {e}")


OPERACIONES = {
    "1": ("Suma", [
        ("Caso principal: suma(a, b)", suma, "binaria"),
        ("Subcaso: suma de una lista", suma_lista, "lista"),
    ]),
    "2": ("Resta", [
        ("Caso principal: resta(a, b)", resta, "binaria"),
        ("Subcaso: resta con negativos", resta_negativos, "binaria"),
    ]),
    "3": ("Multiplicación", [
        ("Caso principal: multiplicacion(a, b)", multiplicacion, "binaria"),
        ("Subcaso: producto de una lista", multiplicacion_lista, "lista"),
    ]),
    "4": ("División", [
        ("Caso principal: division(a, b)", division, "binaria"),
        ("Subcaso: división entera (cociente, residuo)", division_entera, "binaria"),
    ]),
    "5": ("Potencia", [
        ("Caso principal: potencia(base, exponente)", potencia, "binaria"),
        ("Subcaso: exponente negativo", potencia_negativa, "binaria"),
    ]),
    "6": ("Raíz", [
        ("Caso principal: raíz cuadrada", raiz_cuadrada, "unaria"),
        ("Subcaso: raíz n-ésima (número + índice)", raiz_n, "raiz_n"),
    ]),
    "7": ("Módulo", [
        ("Caso principal: modulo(a, b)", modulo, "binaria"),
        ("Subcaso: módulo con negativos (fmod)", modulo_negativos, "binaria"),
    ]),
    "8": ("Porcentaje", [
        ("Caso principal: X% de un número", porcentaje, "binaria"),
        ("Subcaso: variación porcentual", variacion_porcentual, "binaria"),
        ("Subcaso: descuento aplicado", descuento, "binaria"),
    ]),
}

_EJECUTORES = {
    "binaria": _ejecutar_binaria,
    "unaria": _ejecutar_unaria,
    "lista": _ejecutar_lista,
    "raiz_n": _ejecutar_raiz_n,
}


def _mostrar_submenu(nombre_operacion: str, subcasos: list):
    print(f"\n--- {nombre_operacion} ---")
    for i, (etiqueta, _, _) in enumerate(subcasos, start=1):
        print(f"{i}. {etiqueta}")
    print("0. Volver al menú principal")

    eleccion = input("Elige una opción: ").strip()

    if eleccion == "0":
        return

    try:
        indice = int(eleccion) - 1
        if indice < 0 or indice >= len(subcasos):
            raise IndexError
    except (ValueError, IndexError):
        print("Opción no válida.")
        return

    _, funcion, tipo = subcasos[indice]
    ejecutor = _EJECUTORES[tipo]
    ejecutor(funcion)


def mostrar_menu():
    print("\n=== Calculadora Bug Hunters ===")
    for clave, (nombre, _) in OPERACIONES.items():
        print(f"{clave}. {nombre}")
    print("0. Salir")

    opcion = input("Elige una operación: ").strip()

    if opcion == "0":
        print("Saliendo de la calculadora...")
        return

    if opcion not in OPERACIONES:
        print("Opción no válida.")
        return

    nombre, subcasos = OPERACIONES[opcion]
    _mostrar_submenu(nombre, subcasos)
