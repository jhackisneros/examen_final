from typing import List, Tuple
from proceso import Proceso

GanttEntry = Tuple[str, int, int]

def calcular_metricas(procesos: List[Proceso], gantt: List[GanttEntry]):
    tiempos_respuesta = []
    tiempos_retorno = []
    tiempos_espera = []

    for proceso in procesos:
        tiempo_inicio = next((inicio for pid, inicio, fin in gantt if pid == proceso.pid), None)
        tiempo_fin = next((fin for pid, inicio, fin in gantt if pid == proceso.pid), None)
        if tiempo_inicio is not None and tiempo_fin is not None:
            respuesta = tiempo_inicio - proceso.tiempo_llegada
            retorno = tiempo_fin - proceso.tiempo_llegada
            espera = retorno - proceso.duracion

            tiempos_respuesta.append(respuesta)
            tiempos_retorno.append(retorno)
            tiempos_espera.append(espera)

    return {
        "tiempo_respuesta_promedio": sum(tiempos_respuesta) / len(tiempos_respuesta),
        "tiempo_retorno_promedio": sum(tiempos_retorno) / len(tiempos_retorno),
        "tiempo_espera_promedio": sum(tiempos_espera) / len(tiempos_espera),
    }
