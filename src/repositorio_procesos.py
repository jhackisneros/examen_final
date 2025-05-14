from typing import Dict
from .proceso import Proceso
from database.json_database import JSONDatabase

class RepositorioProcesos:
    def __init__(self, archivo_db: str):
        self.db = JSONDatabase(archivo_db)
        self.procesos: Dict[str, Proceso] = {}
        self.cargar_desde_base_datos()

    def agregar_proceso(self, proceso: Proceso):
        if proceso.pid in self.procesos:
            raise ValueError(f"El proceso con PID '{proceso.pid}' ya existe.")
        self.procesos[proceso.pid] = proceso
        self.guardar_en_base_datos()

    def eliminar_proceso(self, pid: str):
        if pid in self.procesos:
            del self.procesos[pid]
            self.guardar_en_base_datos()

    def obtener_proceso(self, pid: str) -> Proceso:
        return self.procesos.get(pid)

    def listar_procesos(self):
        return list(self.procesos.values())

    def guardar_en_base_datos(self):
        datos = {pid: vars(proceso) for pid, proceso in self.procesos.items()}
        self.db.guardar(datos)

    def cargar_desde_base_datos(self):
        datos = self.db.cargar()
        self.procesos = {pid: Proceso(**atributos) for pid, atributos in datos.items()}
