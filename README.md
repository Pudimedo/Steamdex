# Steamdex
Projeto para a disciplina Programação Orientada a Serviços

# Equipe
- Godofredo

# Descrição do Tema
Steamdex é um site para críticos de jogos que desejam deixar público suas opniões de seus jogos favoritos. 

A plataforma permite registrar, avaliar, criar listas e escrever críticas sobre Jogos.

# Tecnologia de Frontend
Será usado NextJS para o frontend

# Cronograma Inicial do Projeto divido por etapas
O versionamento deve ser documentado por relatórios semanais ditando o que foi feito em cada commit

## Etapa 1 – Planejamento e Definição de Requisitos
- Definir funcionalidades principais do sistema:
- Cadastro e login de usuários
  - Listagem de jogos
  - Avaliação (notas)
  - Criação de reviews
  - Criação de listas personalizadas
- Modelar entidades principais (Usuário, Jogo, Review, Lista)
- Definir arquitetura geral do sistema
- Criar wireframes/telas iniciais
- Configurar repositório no GitHub

## Etapa 2 – Configuração do Ambiente de Desenvolvimento
- Configurar ambiente local:
  - Python + FastAPI
  - Node.js + Next.js
- Criar estrutura inicial dos projetos (frontend e backend)
- Configurar ferramentas de desenvolvimento
- Rodar frontend e backend localmente

## Etapa 3 – Desenvolvimento do Backend (FastAPI)

- Criar estrutura base do backend
- Implementar modelos (ORM):
  - Usuário
  - Jogo
  - Review
  - Lista
- Criar rotas:
  - Autenticação (login/registro)
  - CRUD de jogos
  - CRUD de reviews
  - CRUD de listas
- Implementar validações
- Testar endpoints

## Etapa 4 – Integração com API da Steam
- Estudar API da Steam
- Implementar busca de jogos
- Armazenar dados relevantes no banco
- Tratar erros e limites da API

## Etapa 5 – Desenvolvimento do Frontend (Next.js)
- Criar páginas principais:
  - Home
  - Login/Registro
  - Perfil
  - Página de jogo
- Integrar com backend
- Implementar navegação

## Etapa 6 – Funcionalidades Principais
- Sistema de avaliação
- Reviews
- Listas personalizadas
- Exibir dados nas páginas
- Implementar autenticação no frontend

## Etapa 7 – Testes e Integração Geral
- Testar frontend + backend juntos
- Corrigir bugs
- Validar fluxos completos:
  - Cadastro
  - Login
  - Avaliação
  - Criação de listas
 
## Etapa 8 – Containerização com Docker
- Criar Dockerfile para:
  - Backend (FastAPI)
  - Frontend (Next.js)
- Configurar banco de dados em container
- Testar execução completa via Docker
- Ajustar variáveis de ambiente

## Etapa 9 – Finalização e Documentação
- Revisar README:
  - Como rodar o projeto
  - Tecnologias utilizadas
- Revisar código
- Preparar apresentação
- Garantir que o projeto roda via Docker corretamente
