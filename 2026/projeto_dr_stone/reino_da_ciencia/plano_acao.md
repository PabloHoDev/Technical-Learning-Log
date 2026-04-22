🧪 🚀 PLANO DE AÇÃO ATUALIZADO (COERENTE COM O DOMÍNIO)

Agora o plano não é só técnico — é lógico dentro do universo do jogo.

🧱 FASE 1 — NÚCLEO ECONÔMICO (BASE DO SISTEMA)

👉 Antes de pessoas, antes de tecnologia…
👉 você constrói a economia.

🔹 PASSO 1 — FINALIZAR VALUE OBJECTS

📂 dominio/value_objects/

TipoRecurso ✔
Especializacao ✔
EstadoTecnologia ✔

✔ Testes passando
✔ Sem erro de import

👉 Isso define a linguagem

🔥 PASSO 2 — IMPLEMENTAR RECURSO (PRIMEIRO PILAR)

📂 dominio/recursos/recurso.py

Agora com as regras que você definiu:

Deve ter:
tipo (imutável)
quantidade (privada)
Métodos:
adicionar()
consumir()
Regras aplicadas:
❌ não aceita negativo
❌ não aceita zero
❌ não consome além do estoque
✔ lança erro sempre
🧪 PASSO 3 — TESTAR RECURSO

📂 tests/test_recurso.py

Testar:

criação válida
erro ao adicionar negativo
erro ao consumir além do estoque
consumo válido reduz quantidade

👉 Aqui você valida o coração econômico

🧠 FASE 2 — AGENTES DO SISTEMA (PESSOAS)

Agora que existe recurso, faz sentido ter quem usa.

🔹 PASSO 4 — PESSOA (BASE)

📂 pessoas/pessoa.py

Implementar:
nome
energia_atual
energia_maxima
especializacao
Métodos:
gastar_energia()
restaurar_energia()
pode_agir()
🔹 PASSO 5 — ESPECIALIZAÇÕES

📂 pessoas/

Agora sim conecta com recurso:

👨‍🔬 Cientista
consome energia
aumenta progresso de tecnologia
🛠 Artesão
consome energia
gera recurso (ex: madeira)
⚔ Guerreiro
não produz ainda
prepara para eventos futuros
🔬 FASE 3 — SISTEMA DE TECNOLOGIA

Agora entra progressão.

🔹 PASSO 6 — TECNOLOGIA

📂 tecnologias/tecnologia.py

Deve considerar:
custo em recursos
requisitos
progresso
estado
🔥 REGRA IMPORTANTE (QUE VOCÊ DEFINIU)
FERRO só existe após tecnologia

👉 Isso precisa estar aqui.

🏘 FASE 4 — VILA (AGGREGATE ROOT REAL)

Agora tudo se conecta.

🔹 PASSO 7 — VILA

📂 vila/vila.py

Responsabilidades:
controlar estoque de recursos
controlar pessoas
controlar tecnologias
validar ações
REGRA MAIS IMPORTANTE DO PROJETO:
NINGUÉM ALTERA NADA DIRETAMENTE

TUDO PASSA PELA VILA
🔁 FASE 5 — SISTEMA DE TURNOS

Agora o sistema começa a “viver”.

🔹 PASSO 8 — AVANÇAR TURNO

Na Vila:

restaura energia
executa produção
avança pesquisa
🧪 FASE 6 — TESTES DE COMPORTAMENTO

Agora você testa cenários reais:

produzir recurso
faltar recurso
avançar turno
pesquisar tecnologia
⚙️ FASE 7 — APLICAÇÃO

📂 aplicacao/

produzir_recurso
pesquisar_tecnologia
avancar_turno

👉 só orquestra

🖥 FASE 8 — INTERFACE

CLI simples.

Nada de regra.

🗄 FASE 9 — INFRAESTRUTURA

Salvar e carregar estado.

🎯 VISÃO FINAL DO FLUXO
Value Objects
      ↓
Recurso (economia)
      ↓
Pessoa (agentes)
      ↓
Especializações
      ↓
Tecnologia (progressão)
      ↓
Vila (controle total)
      ↓
Turnos
      ↓
Casos de uso
      ↓
Interface
🧠 O QUE MUDOU COM SUAS REGRAS

Antes:
👉 sistema genérico

Agora:
👉 sistema coerente com mundo real + Dr. Stone

🚨 ALERTA FINAL (IMPORTANTE)

Você agora entrou na fase onde:

👉 código começa a ter impacto estrutural

Se fizer errado aqui:

vai retrabalhar tudo depois

Se fizer certo:

o resto flui naturalmente
🎯 PRÓXIMA AÇÃO (SEM PULAR)

Agora não tem mais dúvida:

👉 você vai implementar:

dominio/recursos/recurso.py

Se quiser fazer no nível certo, me fala:

👉 “vamos implementar recurso com essas regras”

E eu te entrego:

código limpo
validação forte
encapsulamento correto
testes alinhados