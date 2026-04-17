Diagrama de todo projeto

reino-da-ciencia/
│
├── src/
│   │
│   ├── dominio/                ← (ESTRUTURA CRIADA ✔)
│   │   │
│   │   ├── value_objects/      ← (PRONTO PARA COMEÇAR 🔥)
│   │   │   ├── tipo_recurso.py
│   │   │   ├── especializacao.py
│   │   │   └── estado_tecnologia.py
│   │   │
│   │   ├── pessoas/            ← (VAZIO)
│   │   │   ├── pessoa.py
│   │   │   ├── cientista.py
│   │   │   ├── artesao.py
│   │   │   └── guerreiro.py
│   │   │
│   │   ├── recursos/           ← (PRÓXIMO PASSO)
│   │   │   └── recurso.py
│   │   │
│   │   ├── tecnologias/        ← (FUTURO)
│   │   │   ├── tecnologia.py
│   │   │   ├── arvore_tecnologica.py
│   │   │   └── requisitos.py
│   │   │
│   │   └── vila/               ← (AGGREGATE ROOT FUTURO)
│   │       └── vila.py
│   │
│   ├── aplicacao/              ← (AINDA NÃO USADO)
│   │   ├── casos_de_uso/
│   │   └── simulador.py
│   │
│   ├── infraestrutura/         ← (AINDA NÃO USADO)
│   │   ├── repositorios/
│   │   ├── persistencia/
│   │   └── configuracoes/
│   │
│   └── interfaces/             ← (AINDA NÃO USADO)
│       ├── linha_de_comando/
│       └── api/
│
├── tests/                      ← (PRONTO PARA COMEÇAR)
│   ├── test_pessoa.py
│   ├── test_recurso.py
│   ├── test_tecnologia.py
│   └── test_vila.py
│
├── docs/                       ← (JÁ MADURO ✔)
│
├── main.py                     ← (NÃO USAR AINDA 🚫)
└── README.md