# src/dominio/value_objects/especializacao.py

from enum import Enum


class Especializacao(Enum):
    CIENTISTA = "cientista"
    ARTESAO = "artesao"
    GUERREIRO = "guerreiro"
    MENTALISTA = "mentalista"
    MEDICO = "medico"
    ASTRONAUTA = "astronauta"
    REI = "rei"