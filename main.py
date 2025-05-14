from src.repositorio_procesos import RepositorioProcesos
from src.scheduler import FCFSScheduler, RoundRobinScheduler
from src.metrics import calcular_metricas

class AplicacionScheduler:
    def __init__(self):
        self.repositorio = RepositorioProcesos("database/procesos.json")  # Archivo JSON para la base de datos

    def cargar_procesos_demo(self):
        self.repositorio.agregar_proceso("P1", 10, 1)
        self.repositorio.agregar_proceso("P2", 5, 2)
        self.repositorio.agregar_proceso("P3", 8, 3)

    def ejecutar_fcfs(self):
        procesos = self.repositorio.listar_procesos()
        if not procesos:  # Validar si no hay procesos
            print("No hay procesos registrados para ejecutar FCFS.")
            return

        print("\nProcesos registrados:")
        for p in procesos:
            print(p)

        scheduler = FCFSScheduler()
        gantt = scheduler.planificar(procesos)
        metricas = calcular_metricas(procesos, gantt)

        print("\nDiagrama de Gantt (FCFS):", gantt)
        print("Métricas:", metricas)

    def ejecutar_round_robin(self, quantum=4):
        procesos = self.repositorio.listar_procesos()
        if not procesos:  # Validar si no hay procesos
            print("No hay procesos registrados para ejecutar Round Robin.")
            return

        scheduler = RoundRobinScheduler(quantum=quantum)
        gantt = scheduler.planificar(procesos)
        metricas = calcular_metricas(procesos, gantt)

        print(f"\nDiagrama de Gantt (Round Robin, quantum={quantum}):", gantt)
        print("Métricas:", metricas)

    def ejecutar(self):
        self.cargar_procesos_demo()
        self.ejecutar_fcfs()
        self.ejecutar_round_robin(quantum=4)

if __name__ == "__main__":
    app = AplicacionScheduler()
    app.ejecutar()
