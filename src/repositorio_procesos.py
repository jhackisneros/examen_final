from typing import Dict
from .proceso import Proceso
from database.json_database import JSONDatabase

class RepositorioProcesos:
    def __init__(self, archivo):
        self.archivo = archivo
        self.procesos = []  # Lista para almacenar los procesos en memoria

    def agregar_proceso(self, nombre, duracion, prioridad):
        proceso = {"nombre": nombre, "duracion": duracion, "prioridad": prioridad}
        self.procesos.append(proceso)  # Agregar a la lista en memoria
        self.guardar_procesos()  # Guardar en el archivo JSON

    def listar_procesos(self):
        self.cargar_procesos()  # Cargar los procesos desde el archivo JSON
        return self.procesos

    def guardar_procesos(self):
        import json
        with open(self.archivo, "w") as f:
            json.dump(self.procesos, f)

    def cargar_procesos(self):
        import json
        try:
            with open(self.archivo, "r") as f:
                self.procesos = json.load(f)
        except FileNotFoundError:
            self.procesos = []
