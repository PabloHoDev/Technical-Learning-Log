from src.dominio.value_objects.tipo_recurso import TipoRecurso


def test_tipo_recurso_enum():
    assert TipoRecurso.MADEIRA.value == "madeira"
