🚀 Construindo uma API em Python

🎯 Objetivo
Criar uma API REST simples com:

- CRUD completo
- Estrutura organizada
- Boas práticas
- Pronta para evoluir

🧠 Escolha da Ferramenta

Vamos usar:
👉 FastAPI

Por quê?

- Moderna
- Rápida
- Fácil de usar
- Documentação automática (Swagger)

📦 Estrutura do Projeto
api-python/
│
├── src/
│   ├── main.py
│   │
│   ├── dominio/
│   │   └── usuario.py
│   │
│   ├── aplicacao/
│   │   └── usuario_service.py
│   │
│   ├── infraestrutura/
│   │   └── repositorio_usuario.py
│   │
│   └── interfaces/
│       └── usuario_controller.py
│
├── requirements.txt
└── README.md