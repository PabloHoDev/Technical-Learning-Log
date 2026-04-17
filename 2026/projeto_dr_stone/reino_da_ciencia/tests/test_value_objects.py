from src.dominio.value_objects.tipo_recurso import TipoRecurso


def test_tipo_recurso_enum():
    assert TipoRecurso.MADEIRA.value == "madeira"
    assert TipoRecurso.PEDRA.value == "pedra"
    assert TipoRecurso.FERRO.value == "ferro"
    assert TipoRecurso.ALIMENTO.value == "alimento"
