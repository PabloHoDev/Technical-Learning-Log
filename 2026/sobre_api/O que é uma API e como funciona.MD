🔌 1️⃣ O que é uma API?

API (Application Programming Interface) é um contrato de comunicação entre sistemas.

Ela define:

O que pode ser solicitado

Como deve ser solicitado

O que será retornado

Em qual formato

Sem API, sistemas ficam isolados.
Com API, eles colaboram.

🧠 Conceito de API (de forma simples)

Imagine um restaurante:

Você → Cliente

Garçom → API

Cozinha → Servidor

Você não entra na cozinha.
Você faz o pedido ao garçom.
O garçom leva para a cozinha.
A comida volta para você.

A API é o garçom do sistema.

🌍 Cliente vs Servidor
🧍 Cliente

É quem faz a requisição.

Pode ser:

Navegador

App mobile

Outro sistema

Postman

Frontend React

Script Python

🖥 Servidor

É quem recebe a requisição e responde.

Ele:

Processa dados

Consulta banco

Executa regras

Retorna resposta

🔁 Requisição e Resposta

Toda API funciona nesse ciclo:

📤 Requisição (Request)

Cliente envia:

Método (GET, POST, etc.)

Endpoint (/usuarios)

Headers

Body (às vezes)

📥 Resposta (Response)

Servidor retorna:

Status Code (200, 404, 500)

Body (normalmente JSON)

Headers