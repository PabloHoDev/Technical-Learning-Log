# src/dominio/value_objects/estado_tecnologia.py

from enum import Enum


class EstadoTecnologia(Enum):
    BLOQUEADA = "bloqueada"
    PESQUISANDO = "pesquisando"
    DESBLOQUEADA = "desbloqueada"