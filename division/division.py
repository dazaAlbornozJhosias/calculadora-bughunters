"""
Responsable: Integrante 4
Caso principal: división de dos números (con manejo de división por cero).
Subcaso: división entera + residuo (divmod).
"""
def division_enteros():
    print("- DIVISIÓN CON ENTEROS O NEGATIVOS -")
    
    # Entrada de datos desde la consola
    num1 = int(input("Ingresa el dividendo"))
    num2 = int(input("Ingresa el divisor"))
    
    # Validación de división entre cero
    if num2 == 0:
        print("\nError: No es posible dividir entre cero.")
        return

    
    resultado = num1 / num2
    
    # Explicación según la ley de los signos
    print("\n- Resultado -")
    print(f"Operación: {num1} / {num2} = {resultado}")
    
    if (num1 < 0 and num2 > 0) or (num1 > 0 and num2 < 0):
        print("Resultado NEGATIVO")
    elif num1 < 0 and num2 < 0:
        print("Resultado POSITIVO")
    else:
        print("Resultado POSITIVO")

if __name__ == "__main__":
    division_enteros()