import json
from typing import Any, Dict

class JSONDatabase:
    def __init__(self, archivo: str):
        self.archivo = archivo

    def guardar(self, datos: Dict[str, Any]):
        """Guarda los datos en el archivo JSON."""
        try:
            with open(self.archivo, 'w') as f:
                json.dump(datos, f, indent=4)
        except Exception as e:
            raise IOError(f"Error al guardar en la base de datos: {e}")

    def cargar(self) -> Dict[str, Any]:
        """Carga los datos desde el archivo JSON."""
        try:
            with open(self.archivo, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}  # Si el archivo no existe, devolver un diccionario vacío
        except Exception as e:
            raise IOError(f"Error al cargar la base de datos: {e}")
