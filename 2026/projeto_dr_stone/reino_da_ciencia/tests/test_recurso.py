from src.dominio.recursos.recurso import Recurso
from src.dominio.value_objects.tipo_recurso import TipoRecurso

import pytest


def test_criar_recurso_valido():
    recurso = Recurso(TipoRecurso.MADEIRA, 10)
    assert recurso.quantidade == 10


def test_nao_permite_quantidade_inicial_negativa():
    with pytest.raises(ValueError):
        Recurso(TipoRecurso.MADEIRA, -5)


def test_adicionar_recurso():
    recurso = Recurso(TipoRecurso.MADEIRA, 10)
    recurso.adicionar(5)
    assert recurso.quantidade == 15


def test_nao_permite_adicionar_zero_ou_negativo():
    recurso = Recurso(TipoRecurso.MADEIRA, 10)

    with pytest.raises(ValueError):
        recurso.adicionar(0)

    with pytest.raises(ValueError):
        recurso.adicionar(-3)


def test_consumir_recurso():
    recurso = Recurso(TipoRecurso.MADEIRA, 10)
    recurso.consumir(4)
    assert recurso.quantidade == 6


def test_nao_permite_consumir_mais_do_que_existe():
    recurso = Recurso(TipoRecurso.MADEIRA, 5)

    with pytest.raises(ValueError):
        recurso.consumir(10)


def test_nao_permite_consumir_zero_ou_negativo():
    recurso = Recurso(TipoRecurso.MADEIRA, 5)

    with pytest.raises(ValueError):
        recurso.consumir(0)

    with pytest.raises(ValueError):
        recurso.consumir(-2)