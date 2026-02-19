📌 Introdução

Escrever código que funciona não é suficiente.
Software profissional exige:

Confiabilidade

Manutenibilidade

Segurança contra regressões

Clareza estrutural

Testes automatizados e boas práticas de qualidade são o que diferenciam código amador de código profissional.

1️⃣ O Que São Testes Automatizados?

Testes automatizados são códigos escritos para validar o comportamento de outros códigos.

Eles garantem que:

A funcionalidade continua correta

Mudanças futuras não quebrem o sistema

Regras de negócio sejam respeitadas

2️⃣ Tipos de Testes
🔹 Testes Unitários

Testam a menor unidade possível do sistema (normalmente uma função ou método).

Características:

Rápidos

Isolados

Sem dependência externa

Focados em lógica de negócio

Exemplo conceitual:

def test_soma():
    assert soma(2, 3) == 5

🔹 Testes de Integração

Testam a comunicação entre partes do sistema.

Exemplo:

Serviço + Banco de dados

API + Camada de aplicação

🔹 Testes End-to-End (E2E)

Testam o fluxo completo do usuário.

São mais lentos, mas validam o sistema como um todo.

3️⃣ Pirâmide de Testes

Modelo recomendado:

        E2E
     Integração
   Unitários


✔ Muitos testes unitários
✔ Alguns testes de integração
✔ Poucos testes E2E

Motivo:

Unitários são rápidos e baratos

E2E são lentos e caros

4️⃣ TDD — Test Driven Development

Desenvolvimento Orientado a Testes.

Fluxo:

Escrever o teste

Ver o teste falhar

Implementar o código mínimo para passar

Refatorar

Benefícios:

Código mais limpo

Menos acoplamento

Design mais modular

Maior segurança

5️⃣ Mock e Isolamento

Mocks são objetos simulados usados para:

Isolar dependências externas

Testar comportamento específico

Evitar uso de banco real ou API real

Exemplo:

Simular um repositório

Simular uma resposta HTTP

6️⃣ Qualidade de Código

Testes não são suficientes se o código for mal estruturado.

Qualidade envolve:

Clareza

Organização

Legibilidade

Baixo acoplamento

Alta coesão

7️⃣ Código Limpo (Clean Code)

Princípios importantes:

Nomes claros

Funções pequenas

Uma responsabilidade por classe

Evitar duplicação

Evitar complexidade desnecessária

8️⃣ Code Smells (Sinais de Problema)

Alguns sinais de alerta:

Funções muito longas

Classes gigantes

Muitos parâmetros

Código duplicado

Comentários excessivos para explicar código confuso

Se precisa explicar demais, provavelmente está mal estruturado.

9️⃣ Refatoração

Refatorar é:

Melhorar a estrutura interna sem alterar comportamento externo.

Deve ser feita:

Após testes estarem passando

Com segurança garantida pelos testes

🔟 Por Que Testes São Importantes Profissionalmente?

Empresas valorizam desenvolvedores que:

Escrevem código testável

Entendem regressão

Sabem evitar bugs futuros

Pensam em manutenção

Testes são investimento, não desperdício de tempo.

📈 Conclusão

Código sem teste pode funcionar hoje.
Código com testes continua funcionando amanhã.

Qualidade de software não é apenas entregar rápido —
é entregar algo sustentável.


✅ Checklist de Qualidade de Código em Python
📌 1. Legibilidade

 Os nomes de variáveis são claros e descritivos? (total_price em vez de tp)

 As funções têm nomes que explicam o que fazem?

 O código evita abreviações desnecessárias?

 O código segue o padrão PEP 8?

 A indentação está correta (4 espaços)?

📌 2. Organização e Estrutura

 Cada função faz apenas uma responsabilidade?

 O código está dividido em módulos quando necessário?

 Não há duplicação de código (DRY – Don't Repeat Yourself)?

 As funções não são excessivamente longas?

 As classes têm responsabilidades bem definidas?

📌 3. Boas Práticas Python

 Uso adequado de list comprehensions?

 Uso correto de with para arquivos?

 Uso de enumerate() em vez de contador manual?

 Uso de zip() quando apropriado?

 Uso de f-strings em vez de concatenação antiga?

Exemplo ruim:

print("Nome: " + nome)


Exemplo melhor:

print(f"Nome: {nome}")

📌 4. Tratamento de Erros

 Uso adequado de try/except?

 Não usa except: genérico?

 Erros são tratados de forma clara?

 Não oculta erros silenciosamente?

Exemplo ruim:

try:
    x = 10 / 0
except:
    pass


Exemplo melhor:

try:
    x = 10 / 0
except ZeroDivisionError:
    print("Divisão por zero não é permitida.")

📌 5. Performance

 Evita loops desnecessários?

 Evita cálculos repetidos?

 Usa estruturas adequadas (set para busca rápida)?

 Evita criar listas quando pode usar generators?

Exemplo:

# Melhor para grandes volumes
soma = sum(x for x in range(1000000))

📌 6. Testes

 O código tem testes?

 Funções são testáveis isoladamente?

 Não depende de input direto dentro da lógica?

 Usa pytest ou unittest?

📌 7. Segurança

 Não há senhas hardcoded?

 Não usa eval() desnecessariamente?

 Valida dados de entrada?

 Evita SQL Injection (se usar banco)?

📌 8. Documentação

 Funções têm docstrings?

 O código explica o “porquê”, não o óbvio?

 Existe README no projeto?

 Tipagem com type hints foi usada?

Exemplo:

def calcular_total(preco: float, quantidade: int) -> float:
    """Calcula o valor total com base no preço e quantidade."""
    return preco * quantidade

📌 9. Código Limpo

 Não há prints de debug esquecidos?

 Não há código comentado desnecessário?

 Imports estão organizados?

 Variáveis não utilizadas foram removidas?

🧠 Checklist Rápido para Revisão Final

Antes de entregar:

✔ O código é fácil de entender em 1 leitura?
✔ Outro desenvolvedor conseguiria manter isso?
✔ Está preparado para falhas?
✔ Está testado?
✔ Está seguindo padrões do Python?