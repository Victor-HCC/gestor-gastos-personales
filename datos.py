import json
from rich.console import Console
from rich.text import Text
import os

console = Console()


def load_data():
  """
  Devuelve una lista de movimientos cargados desde un archivo JSON.
  
  Si el archivo no existe o hay un error de decodificación, crea un nuevo archivo
  y devuelve una lista vacía.
  """
  
  file_directory = 'data/movimientos.json' # Ruta del archivo JSON
  folder = os.path.dirname(file_directory) # Obtiene el directorio del archivo
  
  try:
    # Intenta abrir el archivo y cargar los datos
    with open(file_directory, 'r') as file:
      data = json.load(file)
      return data
  except FileNotFoundError:
    # Mensaje de error si el archivo no existe
    msg = Text(f"El archivo {file_directory} no existe. Se creará uno nuevo.")
    msg.stylize("bold white on yellow")
    console.print(msg)
    
    os.makedirs(folder, exist_ok=True) # Crea el directorio si no existe
    # Se crea un nuevo archivo vacío
    with open(file_directory, 'w') as file:
      json.dump([], file)
    return []
  except json.JSONDecodeError:
    # Mensaje de error si hay un problema al decodificar el JSON
    msg = Text(f"Error al decodificar el archivo {file_directory}. Se creará uno nuevo.")
    msg.stylize("bold white on yellow")
    console.print(msg)
    
    os.makedirs(folder, exist_ok=True)
    
    # Se crea un nuevo archivo vacío
    with open(file_directory, 'w') as file:
      json.dump([], file)
    return []
  
def save_data(data):
  """
  Recibe una lista de datos y los guarda en un archivo JSON.
  
  Si ocurre un error al escribir en el archivo, imprime un mensaje de error.
  """
  try:
    file_directory = 'data/movimientos.json'
    with open(file_directory, 'w') as file:
      json.dump(data, file, indent=2)
  except IOError as e:
    msg = Text(f"Error al guardar los datos en {file_directory}: {e}")
    msg.stylize("bold red")
    console.print(msg)
    return

