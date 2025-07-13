import questionary
import gastos

"""
Programa principal para gestionar gastos personales.

Permite registrar movimientos, consultar movimientos y ver un resumen de los mismos.
"""
while True:
  try:
    print("\n💰 Bienvenido al gestor de gastos personales")
    # Se usa la librería questionary para crear un menú interactivo
    # que permite al usuario seleccionar una opción.
    choice = questionary.select(
      "\n Selecciona una opción:",
      choices=[
        "1. Registrar nuevo movimiento.",
        "2. Consultar movimientos.",
        "3. Ver resumen.",
        "4. Salir"
      ]
    ).ask()
    
    if choice is None:
      print("\n👋 Saliendo...")
      break
    elif choice.startswith("1"):
      gastos.registrar_movimiento()
    elif choice.startswith("2"):
      gastos.mostrar_movimientos()
    elif choice.startswith("3"):
      gastos.resumen_movimientos()
    elif choice.startswith("4"):
      print("\n👋 Saliendo...")
      break
  except Exception as e:
    print(f"Error al seleccionar una opción: {e}")
    continue