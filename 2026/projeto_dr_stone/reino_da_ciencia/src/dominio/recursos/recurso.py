# src/dominio/recursos/recurso.py

from src.dominio.value_objects.tipo_recurso import TipoRecurso


class Recurso:
    def __init__(self, tipo: TipoRecurso, quantidade: int = 0):
        if not isinstance(tipo, TipoRecurso):
            raise TypeError("tipo deve ser um TipoRecurso")

        if quantidade < 0:
            raise ValueError("quantidade inicial não pode ser negativa")

        self._tipo = tipo
        self._quantidade = quantidade

    @property
    def tipo(self) -> TipoRecurso:
        return self._tipo

    @property
    def quantidade(self) -> int:
        return self._quantidade

    def adicionar(self, quantidade: int) -> None:
        if quantidade <= 0:
            raise ValueError("quantidade a adicionar deve ser maior que zero")

        self._quantidade += quantidade

    def consumir(self, quantidade: int) -> None:
        if quantidade <= 0:
            raise ValueError("quantidade a consumir deve ser maior que zero")

        if quantidade > self._quantidade:
            raise ValueError("quantidade insuficiente para consumo")

        self._quantidade -= quantidade

    def __repr__(self) -> str:
        return f"Recurso(tipo={self._tipo.value}, quantidade={self._quantidade})"