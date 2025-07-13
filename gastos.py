import datos
import questionary
from datetime import datetime
import uuid
from rich.table import Table
from rich.console import Console
from rich import box

def registrar_movimiento():
  """
  Registra un nuevo movimiento de ingreso o gasto.
  
  Permite al usuario seleccionar el tipo de movimiento, monto y categoría.
  Guarda el movimiento en un archivo JSON.
  """
  movimientos = datos.load_data()
  
  tipo = questionary.select(
    "Selecciona el tipo de movimiento:",
    choices=["Ingreso", "Gastos"]
  ).ask()
  
  try:
    monto = float(input("Introduce el monto del movimiento: ").strip())
  except ValueError:
    print("❌ El monto debe ser un número válido.")
    return
  
  if tipo == "Ingreso":
    categorias = ["Salario", "Venta", "Regalo", "Otros"]
  else:
    categorias = ["Alimentación", "Transporte", "Salud", "Entretenimiento", "Otros"]
    
  categoria = questionary.select(
    "Selecciona la categoría del movimiento:",
    choices=categorias
  ).ask()
  
  fecha = datetime.now().strftime("%Y-%m-%d")
  
  movimiento_id = uuid.uuid4()
  
  movimiento = {
    "id": str(movimiento_id),
    "tipo": tipo,
    "monto": monto,
    "categoria": categoria,
    "fecha": fecha
  }
  
  movimientos.append(movimiento)
  datos.save_data(movimientos)
  
def mostrar_movimientos():
  """
  Muestra una lista de todos los movimientos registrados.
  
  Utiliza una tabla para mostrar la fecha, tipo, categoría y monto de cada movimiento.
  Si no hay movimientos, muestra un mensaje de advertencia.
  """
  movimientos = datos.load_data()
  console = Console()
  
  if not movimientos:
    console.print("\n [bold yellow]⚠ No hay movimientos registrados.[/bold yellow]")
    return
  
  tabla = Table(title="💰 Lista de Movimientos", box=box.ROUNDED, style="cyan")

  tabla.add_column("Fecha", style="dim", width=12)
  tabla.add_column("Tipo", style="bold")
  tabla.add_column("Categoría")
  tabla.add_column("Monto", justify="right")
  
  for mov in movimientos:
    tipo_color = "green" if mov["tipo"].lower() == "ingreso" else "red"
    
    tabla.add_row(
      mov["fecha"],
      f"[{tipo_color}]{mov['tipo']}[/{tipo_color}]",
      mov["categoria"],
      f"${mov['monto']:.2f}"
    )
    
  console.print(tabla)
    
def resumen_movimientos():
  """
  Muestra un resumen de los movimientos registrados.
  
  Calcula el total de ingresos, gastos y el balance general.
  
  Utiliza una tabla para mostrar el resumen.
  Si no hay movimientos, muestra un mensaje de advertencia.
  """
  
  movimientos = datos.load_data()
  console = Console()

  if not movimientos:
    console.print("\n [bold yellow]⚠ No hay movimientos registrados.[/bold yellow]")
    return
  
  ingresos = sum(mov['monto'] for mov in movimientos if mov['tipo'] == "Ingreso")
  gastos = sum(mov['monto'] for mov in movimientos if mov['tipo'] == "Gastos")
  balance = ingresos - gastos
  
  # Tabla con resumen
  tabla = Table(title="📊 Resumen General", box=box.SIMPLE_HEAVY, style="bold")
  tabla.add_column("Tipo", style="cyan")
  tabla.add_column("Monto", justify="right")

  tabla.add_row("💸 Ingresos", f"[green]${ingresos:.2f}[/green]")
  tabla.add_row("🧾 Gastos", f"[red]${gastos:.2f}[/red]")

  balance_color = "green" if balance >= 0 else "red"
  tabla.add_row("💼 Balance", f"[bold {balance_color}]${balance:.2f}[/bold {balance_color}]")

  console.print(tabla)