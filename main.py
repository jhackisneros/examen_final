from src.proceso import Proceso
from src.scheduler import FCFSScheduler, RoundRobinScheduler
from src.repositorio import RepositorioProcesos
from src.metrics import calcular_metricas

class Aplicacion:
    def __init__(self):
        self.repositorio = RepositorioProcesos()

    def registrar_procesos(self):
        self.repositorio.agregar_proceso(Proceso("P1", 10, 1))
        self.repositorio.agregar_proceso(Proceso("P2", 5, 2))
        self.repositorio.agregar_proceso(Proceso("P3", 8, 3))

    def mostrar_procesos(self):
        print("Procesos registrados:")
        for proceso in self.repositorio.listar_procesos():
            print(proceso)

    def ejecutar_fcfs(self):
        scheduler = FCFSScheduler()
        gantt = scheduler.planificar(self.repositorio.listar_procesos())
        print("\nDiagrama de Gantt (FCFS):", gantt)
        metricas = calcular_metricas(self.repositorio.listar_procesos(), gantt)
        print("\nMétricas:", metricas)

    def ejecutar(self):
        self.registrar_procesos()
        self.mostrar_procesos()
        self.ejecutar_fcfs()

if __name__ == "__main__":
    app = Aplicacion()
    app.ejecutar()
