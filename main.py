"""Punto de entrada de la calculadora completa."""
from menu import mostrar_menu

if __name__ == "__main__":
    while True:
        mostrar_menu()
        continuar = input("\n¿Otra operación? (s/n): ").strip().lower()
        if continuar != "s":
            print("¡Hasta luego!")
            break
