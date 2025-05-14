import pytest
from src.proceso import Proceso

def test_proceso_creacion():
    p = Proceso("P1", 10, 1)
    assert p.pid == "P1"
    assert p.duracion == 10
    assert p.prioridad == 1

def test_proceso_pid_duplicado():
    Proceso("P1", 10, 1)
    with pytest.raises(ValueError):
        Proceso("P1", 5, 2)
