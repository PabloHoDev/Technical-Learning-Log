DOCUMENTAÇÃO — Projeto Reino da Ciência
1️⃣ 📌 Visão Geral do Projeto
🎯 Objetivo

Criar um simulador orientado a objetos inspirado no universo de Dr. Stone, onde o jogador reconstrói a civilização por meio da ciência.

O sistema deve modelar:

Pessoas com habilidades específicas

Recursos naturais

Processos científicos

Tecnologias com dependências

Evolução da vila

2️⃣ 🧠 Problema que Estamos Modelando

No universo do anime:

A humanidade foi petrificada

A civilização precisa ser reconstruída do zero

Cada avanço depende de ciência + recursos + pessoas capacitadas

Nosso sistema vai simular isso.

3️⃣ 🏗 Domínio do Sistema
🔹 Entidades Principais
🧍 Pessoa

Representa qualquer membro da vila.

Responsabilidades:

Possui energia

Possui especialidade

Pode trabalhar em tarefas

🧪 Cientista (Herda Pessoa)

Especialista em pesquisa.

Responsabilidades:

Conduzir experimentos

Desenvolver tecnologias

🛠 Artesão (Herda Pessoa)

Especialista em produção.

Responsabilidades:

Criar ferramentas

Processar recursos

🪨 Recurso

Representa materiais disponíveis.

Exemplos:

Pedra

Ferro

Madeira

Enxofre

Responsabilidades:

Possuir quantidade

Ser consumido

Ser produzido

🔬 Tecnologia

Representa avanços científicos.

Responsabilidades:

Possuir custo

Ter requisitos

Ser desbloqueável

Desbloquear outras tecnologias

🏘 Vila

Representa o estado geral da civilização.

Responsabilidades:

Gerenciar pessoas

Gerenciar recursos

Controlar tecnologias

Controlar moral e energia geral

4️⃣ 📊 Relações Entre Entidades

Vila tem Pessoas

Vila tem Recursos

Vila tem Tecnologias

Tecnologia consome Recursos

Cientista desenvolve Tecnologia

Artesão produz Recursos

Isso ensina:

Composição

Responsabilidade única

Separação de interesses

5️⃣ 🧩 Regras do Sistema (Regras de Negócio)

Exemplo de regras importantes:

Uma tecnologia só pode ser desbloqueada se todos os requisitos forem atendidos

Pessoas gastam energia ao trabalhar

Recursos não podem ficar negativos

Algumas tecnologias desbloqueiam outras

Moral baixa reduz eficiência

Essas regras devem ficar dentro das classes, não espalhadas pelo código.

6️⃣ 🎯 Objetivo do Jogador

Desbloquear a árvore tecnológica completa

Manter a vila estável

Gerenciar recursos com eficiência

Evoluir da Idade da Pedra até a Era Científica

7️⃣ 🧠 Conceitos de POO Que Vamos Treinar
Conceito	Aplicação
Abstração	Modelar pessoas e tecnologias
Encapsulamento	Controle interno de energia e recursos
Herança	Especializações de Pessoa
Polimorfismo	Diferentes tipos de tecnologia
Composição	Vila contém entidades
SOLID	Organização limpa do domínio
8️⃣ 🚀 Evolução do Projeto (Fases)
Fase 1 — Modelo Básico

Criar classes principais

Criar simulação simples

Fase 2 — Sistema de Tecnologia

Criar árvore de dependência

Sistema de desbloqueio

Fase 3 — Sistema de Produção

Produção por turno

Consumo automático

Fase 4 — Arquitetura Profissional

Separar camadas

Aplicar SOLID

Adicionar testes

9️⃣ 📐 Arquitetura Planejada
src/
│
├── domain/        ← Regras do negócio
├── application/   ← Orquestração
├── infrastructure/← Persistência (futuro)
└── main.py

🔟 O Que NÃO Vamos Fazer

Não vamos misturar lógica no main

Não vamos colocar regras fora das classes

Não vamos usar herança sem necessidade

Não vamos criar “Deus classes”

🧠 Mentalidade Correta Para Desenvolver

Antes de codar, sempre perguntar:

Quem é responsável por isso?

Essa regra pertence a qual classe?

Estou violando responsabilidade única?

Estou criando dependência desnecessária?

🔥 Próximo Passo

Agora temos três caminhos:

Criar o Diagrama Conceitual

Criar o Diagrama UML

Criar o Documento de Regras Detalhadas

Criar a Primeira Versão das Classes (sem lógica complexa)