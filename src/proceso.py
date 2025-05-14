from typing import List

class Proceso:
    pids_existentes = set()

    def __init__(self, pid: str, duracion: int, prioridad: int):
        if pid in Proceso.pids_existentes:
            raise ValueError(f"El PID '{pid}' ya existe.")
        if duracion <= 0:
            raise ValueError("La duración debe ser un entero positivo.")
        if prioridad < 0:
            raise ValueError("La prioridad debe ser un entero no negativo.")

        self.pid = pid
        self.duracion = duracion
        self.prioridad = prioridad
        self.tiempo_restante = duracion
        self.tiempo_llegada = 0
        self.tiempo_inicio = None
        self.tiempo_fin = None

        Proceso.pids_existentes.add(pid)

    def __repr__(self):
        return f"Proceso(pid={self.pid}, duracion={self.duracion}, prioridad={self.prioridad})"
