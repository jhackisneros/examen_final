from src.proceso import Proceso
import json
import csv

class RepositorioProcesos:
    def __init__(self):
        self.procesos = {}

    def agregar_proceso(self, pid, duracion, prioridad):
        if pid in self.procesos:
            raise ValueError("PID duplicado")
        proceso = Proceso(pid, duracion, prioridad)
        self.procesos[pid] = proceso

    def listar_procesos(self):
        return list(self.procesos.values())

    def eliminar_proceso(self, pid):
        if pid in self.procesos:
            del self.procesos[pid]

    def obtener_proceso(self, pid):
        return self.procesos.get(pid)

    def guardar_json(self, ruta):
        with open(ruta, "w") as f:
            json.dump([p.to_dict() for p in self.procesos.values()], f)

    def cargar_json(self, ruta):
        with open(ruta, "r") as f:
            datos = json.load(f)
            self.procesos = {d["pid"]: Proceso.from_dict(d) for d in datos}

    def guardar_csv(self, ruta):
        with open(ruta, "w", newline='') as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(["pid", "duracion", "prioridad"])
            for p in self.procesos.values():
                writer.writerow([p.pid, p.duracion, p.prioridad])

    def cargar_csv(self, ruta):
        with open(ruta, "r") as f:
            reader = csv.DictReader(f, delimiter=";")
            self.procesos = {}
            for row in reader:
                pid = row["pid"]
                duracion = int(row["duracion"])
                prioridad = int(row["prioridad"])
                self.agregar_proceso(pid, duracion, prioridad)
