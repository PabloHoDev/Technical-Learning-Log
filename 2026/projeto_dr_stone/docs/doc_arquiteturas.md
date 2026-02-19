📘 DOCUMENTAÇÃO OFICIAL DE ARQUITETURA
Projeto: Reino da Ciência

Inspirado em Dr. Stone

1️⃣ 🏛 Visão Arquitetural Geral

O projeto será estruturado com base em:

Arquitetura em Camadas

Princípios de Arquitetura Limpa

Conceitos de DDD (Design Orientado ao Domínio)

A organização busca:

Separação clara de responsabilidades

Isolamento das regras de negócio

Baixo acoplamento

Alta coesão

Facilidade de evolução

2️⃣ 📂 Estrutura Geral do Projeto
src/
│
├── dominio/
├── aplicacao/
├── infraestrutura/
└── interfaces/

3️⃣ 🧠 Camadas do Sistema
🧩 3.1 — Camada de Domínio (Núcleo do Sistema)

📍 Representa as regras do universo
📍 Não depende de nenhuma outra camada

Contém:

Entidades

Objetos de Valor

Agregados

Regras de negócio

Contratos (interfaces abstratas)

📂 Estrutura Interna do Domínio
dominio/
│
├── pessoas/
│   ├── pessoa.py
│   ├── cientista.py
│   ├── artesao.py
│   └── guerreiro.py
│
├── recursos/
│   └── recurso.py
│
├── tecnologias/
│   ├── tecnologia.py
│   ├── arvore_tecnologica.py
│   └── requisitos.py
│
└── vila/
    └── vila.py

📌 Regras Arquiteturais do Domínio

O domínio não pode importar nada da aplicação

O domínio não pode importar infraestrutura

Todas as regras devem estar aqui

Nenhuma regra deve estar no main

⚙️ 3.2 — Camada de Aplicação

📍 Orquestra os fluxos do sistema
📍 Coordena casos de uso

Ela:

Usa o domínio

Não cria regras

Apenas organiza execução

📂 Estrutura da Aplicação
aplicacao/
│
├── casos_de_uso/
│   ├── pesquisar_tecnologia.py
│   ├── produzir_recurso.py
│   ├── avancar_turno.py
│   └── recrutar_pessoa.py
│
└── simulador.py

🗄 3.3 — Camada de Infraestrutura

📍 Implementações técnicas

Contém:

Persistência de dados

Arquivos

Banco de dados (futuro)

Logs

Configurações

📂 Estrutura da Infraestrutura
infraestrutura/
│
├── repositorios/
│   └── repositorio_vila.py
│
├── persistencia/
│   └── armazenamento_arquivo.py
│
└── configuracoes/
    └── configuracao.py

🖥 3.4 — Camada de Interfaces

📍 Ponto de entrada do sistema

Pode conter:

Interface de linha de comando

API REST

Interface gráfica futura

📂 Estrutura das Interfaces
interfaces/
│
├── linha_de_comando/
│   └── menu.py
│
└── api/
    └── controladores.py

4️⃣ 🔬 Subarquiteturas do Domínio

Agora vamos detalhar a organização interna.

🧍 Módulo Pessoas

Responsável por:

Estado físico

Energia

Especialização

Comportamentos individuais

Especializações são herdadas da classe base Pessoa.

🧪 Módulo Tecnologias

Responsável por:

Controle de dependências

Sistema de desbloqueio

Consumo de recursos

Evolução tecnológica

Pode implementar:

Fábrica de tecnologias

Estratégias de pesquisa

Estados de progresso

🏘 Módulo Vila (Agregado Raiz)

A Vila é o núcleo agregador.

Ela controla:

Pessoas

Recursos

Tecnologias

Moral

Evita comunicação desorganizada entre objetos.

5️⃣ 🔄 Fluxo de Dependência Arquitetural
Interfaces
    ↓
Aplicação
    ↓
Domínio


Infraestrutura implementa contratos definidos no Domínio.

O Domínio nunca depende de nada externo.

6️⃣ 📐 Padrões Arquiteturais Aplicáveis

Podemos aplicar:

Repositório (para persistência)

Fábrica (criação de tecnologias)

Estratégia (diferentes métodos de pesquisa)

Observador (eventos da vila)

Estado (estágios da civilização)

7️⃣ 📏 Regras Arquiteturais Oficiais do Projeto

Nenhuma regra de negócio fora do domínio

Nenhum método com múltiplas responsabilidades

Nenhuma dependência invertida incorretamente

Nenhuma classe "Deus"

Código preparado para testes

8️⃣ 🎯 Preparação Para Crescimento Futuro

Arquitetura preparada para:

Interface gráfica

API externa

Persistência em banco de dados

Sistema de eventos

Testes automatizados

Dockerização