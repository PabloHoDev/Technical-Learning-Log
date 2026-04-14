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

📥 1️⃣ Instalação
pip install fastapi uvicorn


📄 src/main.py
from fastapi import FastAPI
from src.interfaces.usuario_controller import router as usuario_router

app = FastAPI()

app.include_router(usuario_router)

@app.get("/")
def home():
    return {"mensagem": "API funcionando 🚀"}

👤 3️⃣ Domínio
📄 dominio/usuario.py
class Usuario:
    def __init__(self, id: int, nome: str):
        self.id = id
        self.nome = nome

⚙️ 4️⃣ Repositório (Infraestrutura)
📄 infraestrutura/repositorio_usuario.py

class RepositorioUsuario:
    def __init__(self):
        self.usuarios = []

    def listar(self):
        return self.usuarios

    def adicionar(self, usuario):
        self.usuarios.append(usuario)

    def buscar(self, id):
        for u in self.usuarios:
            if u.id == id:
                return u
        return None

    def remover(self, id):
        self.usuarios = [u for u in self.usuarios if u.id != id]

🧠 5️⃣ Aplicação (Service)
📄 aplicacao/usuario_service.py
from src.infraestrutura.repositorio_usuario import RepositorioUsuario
from src.dominio.usuario import Usuario

repo = RepositorioUsuario()

class UsuarioService:

    def listar(self):
        return repo.listar()

    def criar(self, id, nome):
        usuario = Usuario(id, nome)
        repo.adicionar(usuario)
        return usuario

    def buscar(self, id):
        usuario = repo.buscar(id)
        if not usuario:
            raise ValueError("Usuário não encontrado")
        return usuario

    def deletar(self, id):
        repo.remover(id)

🌐 6️⃣ Interface (Controller)
📄 interfaces/usuario_controller.py
from fastapi import APIRouter, HTTPException
from src.aplicacao.usuario_service import UsuarioService

router = APIRouter(prefix="/usuarios")

service = UsuarioService()

@router.get("/")
def listar():
    return service.listar()

@router.post("/")
def criar(id: int, nome: str):
    return service.criar(id, nome)

@router.get("/{id}")
def buscar(id: int):
    try:
        return service.buscar(id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{id}")
def deletar(id: int):
    service.deletar(id)
    return {"mensagem": "Usuário removido"}

▶️ 7️⃣ Rodando o Projeto
uvicorn src.main:app --reload

🌐 8️⃣ Testando no Navegador

Abra:

👉 http://127.0.0.1:8000/docs

Você terá o Swagger automático 🔥