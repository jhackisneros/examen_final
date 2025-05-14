from abc import ABC, abstractmethod
from typing import List, Tuple
from src.proceso import Proceso  # Cambiar a una importación relativa al módulo raíz

GanttEntry = Tuple[str, int, int]

class Scheduler(ABC):
    @abstractmethod
    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        pass

    def calcular_metricas(self, gantt: List[GanttEntry], procesos: List[Proceso]) -> dict:
        if not procesos:  # Validar si la lista de procesos está vacía
            return {
                "tiempo_respuesta_medio": 0,
                "tiempo_espera_medio": 0,
                "tiempo_retorno_medio": 0,
            }

        tiempos_respuesta = []
        tiempos_espera = []
        tiempos_retorno = []

        for proceso in procesos:
            tiempo_inicio = next(entry[1] for entry in gantt if entry[0] == proceso.pid)
            tiempo_fin = next(entry[2] for entry in gantt if entry[0] == proceso.pid)
            tiempo_respuesta = tiempo_inicio - proceso.tiempo_llegada
            tiempo_espera = tiempo_respuesta
            tiempo_retorno = tiempo_fin - proceso.tiempo_llegada

            tiempos_respuesta.append(tiempo_respuesta)
            tiempos_espera.append(tiempo_espera)
            tiempos_retorno.append(tiempo_retorno)

        return {
            "tiempo_respuesta_medio": sum(tiempos_respuesta) / len(procesos),
            "tiempo_espera_medio": sum(tiempos_espera) / len(procesos),
            "tiempo_retorno_medio": sum(tiempos_retorno) / len(procesos),
        }

class FCFSScheduler(Scheduler):
    def planificar(self, procesos: List[Proceso]) -> Tuple[List[GanttEntry], dict]:
        gantt = []
        tiempo_actual = 0
        for proceso in procesos:
            proceso.tiempo_inicio = tiempo_actual
            proceso.tiempo_fin = tiempo_actual + proceso.duracion
            gantt.append((proceso.pid, proceso.tiempo_inicio, proceso.tiempo_fin))
            tiempo_actual += proceso.duracion
        metricas = self.calcular_metricas(gantt, procesos)
        return gantt, metricas

class RoundRobinScheduler(Scheduler):
    def __init__(self, quantum: int):
        if quantum <= 0:
            raise ValueError("El quantum debe ser un entero positivo.")
        self.quantum = quantum

    def planificar(self, procesos: List[Proceso]) -> Tuple[List[GanttEntry], dict]:
        gantt = []
        tiempo_actual = 0
        cola = procesos[:]
        while cola:
            proceso = cola.pop(0)
            if proceso.tiempo_restante > self.quantum:
                gantt.append((proceso.pid, tiempo_actual, tiempo_actual + self.quantum))
                proceso.tiempo_restante -= self.quantum
                tiempo_actual += self.quantum
                cola.append(proceso)
            else:
                gantt.append((proceso.pid, tiempo_actual, tiempo_actual + proceso.tiempo_restante))
                tiempo_actual += proceso.tiempo_restante
                proceso.tiempo_restante = 0
        metricas = self.calcular_metricas(gantt, procesos)
        return gantt, metricas
