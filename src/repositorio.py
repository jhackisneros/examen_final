import json
import csv
from src.proceso import Proceso

class RepositorioProcesos:
    def __init__(self):
        self.procesos = []

    def agregar_proceso(self, proceso: Proceso):
        if any(p.pid == proceso.pid for p in self.procesos):
            raise ValueError(f"El PID '{proceso.pid}' ya existe.")
        self.procesos.append(proceso)

    def listar_procesos(self):
        return self.procesos

    def eliminar_proceso(self, pid: str):
        self.procesos = [p for p in self.procesos if p.pid != pid]

    def guardar_json(self, filepath: str):
        with open(filepath, 'w') as f:
            json.dump([p.__dict__ for p in self.procesos], f)

    def cargar_json(self, filepath: str):
        with open(filepath, 'r') as f:
            data = json.load(f)
            self.procesos = [Proceso(**p) for p in data]

    def guardar_csv(self, filepath: str):
        with open(filepath, 'w', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(['pid', 'duracion', 'prioridad'])
            for p in self.procesos:
                writer.writerow([p.pid, p.duracion, p.prioridad])

    def cargar_csv(self, filepath: str):
        with open(filepath, 'r') as f:
            reader = csv.DictReader(f, delimiter=';')
            self.procesos = [Proceso(row['pid'], int(row['duracion']), int(row['prioridad'])) for row in reader]
