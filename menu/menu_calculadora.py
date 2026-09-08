"""
Responsable: Art (Git Leader) - Integrante 10
Menú central de la calculadora. Debe RETORNAR el control al llamador,
nunca usar sys.exit(), para poder integrarse desde main.py.
"""
from suma import suma, suma_lista
from resta import resta, resta_negativos
from multiplicacion import multiplicacion, multiplicacion_lista
from division import division, division_entera
from potencia import potencia, potencia_negativa
from raiz import raiz_cuadrada, raiz_n
from modulo import modulo, modulo_negativos
from porcentaje import porcentaje, variacion_porcentual


OPCIONES = {
    "1": ("Suma", suma),
    "2": ("Resta", resta),
    "3": ("Multiplicación", multiplicacion),
    "4": ("División", division),
    "5": ("Potencia", potencia),
    "6": ("Raíz cuadrada", raiz_cuadrada),
    "7": ("Módulo", modulo),
    "8": ("Porcentaje", porcentaje),
    "0": ("Salir", None),
}


def _pedir_numero(mensaje: str) -> float:
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada inválida, intenta de nuevo.")


def mostrar_menu():
    """Muestra el menú, ejecuta la opción elegida y RETORNA (no hace sys.exit)."""
    print("\n=== Calculadora Bug Hunters ===")
    for clave, (nombre, _) in OPCIONES.items():
        print(f"{clave}. {nombre}")

    opcion = input("Elige una opción: ").strip()

    if opcion == "0":
        print("Saliendo de la calculadora...")
        return

    if opcion not in OPCIONES:
        print("Opción no válida.")
        return

    nombre, funcion = OPCIONES[opcion]

    if opcion == "6":  # raíz cuadrada solo pide un número
        a = _pedir_numero("Número: ")
        try:
            print(f"Resultado: {funcion(a)}")
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}")
        return

    a = _pedir_numero("Primer número: ")
    b = _pedir_numero("Segundo número: ")
    try:
        print(f"Resultado: {funcion(a, b)}")
    except (ValueError, ZeroDivisionError, TypeError) as e:
        print(f"Error: {e}")
