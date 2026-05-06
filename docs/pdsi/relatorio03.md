# Relatório de Sprint Review
### 1. Identificação
**Projeto:** Steamdex

**Sprint:** Sprint 3

**Período:** 26/04 à 02/05

**Data da Reunião:** 02/05

**Trello:** https://trello.com/b/SrcqeCwi/steamdex


### 2. Integrantes
Godofredo Dantas de Medeiros Maia


### 3. Introdução ao projeto
Steamdex é um site para críticos de jogos que desejam deixar público suas opiniões sobre seus jogos favoritos.

A plataforma permite registrar, avaliar, criar listas e escrever críticas sobre jogos.

O público-alvo do Steamdex são usuários que desejam compartilhar reviews e opiniões sobre jogos.

Suas principais tecnologias são: 
-
- Python
- HTML5
- CSS3
- FastAPI

Suas principais metodologias são:
-
- Scrum

## 5. Fichamento da Reunião (Sprint Review)
Ponto 1: Implementação do sistema de autenticação

Descrição: Desenvolvimento das funcionalidades de cadastro e login de usuários utilizando FastAPI, incluindo criptografia de senha e geração de token JWT.

Decisões tomadas: Utilizar bcrypt para hash de senhas e JWT para autenticação, garantindo segurança básica da aplicação.

Ponto 2: Modelagem do banco de dados

Descrição: Criação das entidades principais do sistema, especialmente a tabela de usuários, com validações como email único.

Decisões tomadas: Definir regras de negócio diretamente no banco (como unicidade) e utilizar ORM (SQLAlchemy) para facilitar manipulação dos dados.

Ponto 3: Estruturação do backend

Descrição: Organização do backend em módulos (auth, models, api), visando melhor manutenção e escalabilidade.

Decisões tomadas: Adotar arquitetura modular separando rotas, serviços e modelos, facilitando futuras expansões do sistema.

## 5. Tarefas Finalizadas na Sprint

- Implementação do endpoint de cadastro de usuário
- Implementação do endpoint de login com JWT
- Criptografia de senha com bcrypt
- Criação da estrutura base do backend com FastAPI
- Configuração do banco de dados com SQLAlchemy

## 6. Tarefas Planejadas
- Implementar endpoint de perfil do usuário (/users/me)
- Criar CRUD de jogos
- Iniciar desenvolvimento do sistema de reviews
- Integrar autenticação com rotas protegidas