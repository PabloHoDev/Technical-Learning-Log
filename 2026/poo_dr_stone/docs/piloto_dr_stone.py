# 🧠 VISÃO GERAL — A REGRA DE DR. STONE

# “A ciência vence pela organização.”
# Na POO: o código vence pela estrutura.

# 🎭 Exemplo no mundo de Dr. Stone
# Mundo real	POO
# Senku	objeto
# Cientista	classe
# Inteligência, conhecimento	atributos
# Criar invenções	métodos

class Cientista:
    def __init__(self, nome, inteligencia, conhecimento):
        self.nome = nome
        self.inteligencia = inteligencia
        self.conhecimento = conhecimento

    def criar_invenção(self, invenção):
        return f"{self.nome} criou a invenção: {invenção}"
    
    def apresentar(self):
        return f"Olá, eu sou {self.nome}, com inteligência {self.inteligencia} e conhecimento {self.conhecimento}."





