# Calculadora Bug Hunters (Ejercicio 2 - a nivel de equipo)

Calculadora completa desarrollada por el equipo **Bug Hunters** (10 integrantes),
donde cada persona implementa una operación distinta.

## Estructura

```
calculadora-bughunters/
├── main.py                  # Punto de entrada
├── __init__.py               # Registro de módulos completos
├── suma/                     # Integrante 1
├── resta/                    # Integrante 2 (ya probado en Ejercicio 2 nivel curso)
├── multiplicacion/           # Integrante 3
├── division/                 # Integrante 4
├── potencia/                 # Integrante 5
├── raiz/                     # Integrante 6
├── modulo/                   # Integrante 7
├── porcentaje/                # Integrante 8
├── validacion/                # Integrante 9 (validaciones comunes)
├── menu/                      # Art - Git Leader (integración)
└── tests/                     # Art - Git Leader (integración)
```

## Reglas del equipo

- Cada función debe ser **pura**: recibe parámetros, retorna un valor. Nada de `input()` ni `print()` dentro de `operacion.py`.
- Cada módulo importa validaciones desde `validacion` (no dupliques lógica de validación).
- Cada carpeta tiene su propio `__init__.py` que expone sus funciones.
- Imports **relativos** dentro de cada módulo (`from .archivo import funcion`), imports **absolutos simples** entre módulos hermanos (`from validacion import validar_numero`) porque todos cuelgan del mismo root.
- Antes de subir cambios: `git pull` de la rama de integración, verificar que compila y que los tests pasan, recién ahí hacer push.
- Nunca push directo a `main` — trabajar en tu rama personal → PR a `integration/eq02-calculadora`.

## Flujo de ramas sugerido

```
main
  └── integration/eq02-calculadora
        ├── feature/suma-<usuario>
        ├── feature/resta-<usuario>
        ├── feature/multiplicacion-<usuario>
        ├── feature/division-<usuario>
        ├── feature/potencia-<usuario>
        ├── feature/raiz-<usuario>
        ├── feature/modulo-<usuario>
        ├── feature/porcentaje-<usuario>
        └── feature/validacion-<usuario>
```

## Cómo correr los tests

```bash
python -m unittest tests/test_calculadora.py
```

## Cómo correr la calculadora

```bash
python main.py
```
