# 🐍 Flask CRUD Users
Um sistema simples em Python + Flask + SQLite, criado para estudos e prática de desenvolvimento backend, autenticação e testes automatizados com o Robot Framework.
O projeto evoluirá gradualmente com o tempo, começando com rotas e banco, depois interface e testes.

🚀 Objetivos

Implementar um CRUD de usuários (criar, ler, atualizar, deletar).

Criar sistema de login com permissões:

MEMBRO – acesso básico

VIP – acesso a áreas restritas

ADMIN – controle total do sistema

Integrar interface gráfica (HTML + Jinja + CSS).

Automatizar testes com o Robot Framework.

🧱 Tecnologias
Linguagem	Python 3.10+
Framework web	Flask
Banco de dados	SQLite
Testes automatizados	Robot Framework
Versionamento	Git + GitHub

⚙️ Instalação local

Clone o repositório:
git clone https://github.com/SEU_USUARIO/NOME_REPO.git
cd NOME_REPO


Crie e ative o ambiente virtual:

python -m venv .venv
.venv\Scripts\Activate.ps1


Instale as dependências:

pip install -r requirements.txt


Inicialize o banco de dados:

python -c "from db import init_db; init_db()"


Crie o usuário inicial (admin):

python -c "from auth import create_user; create_user('admin','a@a.com','admin123','ADMIN')"


Execute o servidor:

python app.py


Acesse no navegador:
👉 http://localhost:8000

🧠 Estrutura do projeto
crud_app/
├── app.py            # app principal Flask
├── auth.py           # autenticação e rotas de login/logout/registro
├── db.py             # conexão e inicialização do banco SQLite
├── models.sql        # schema do banco
├── requirements.txt  # dependências
└── templates/        # (futuramente) arquivos HTML

🔮 Próximos passos planejados

 Criar layout HTML (base, login, dashboard, admin)

 Adicionar CRUD completo de usuários (interface)

 Implementar controle de permissões em tela

 Integrar Robot Framework para testes de UI e API

 Dockerizar a aplicação

🧪 Testes (em breve)

Os testes serão escritos com Robot Framework, simulando o comportamento do usuário:

Login e logout

Acesso de cada tipo de conta (MEMBRO, VIP, ADMIN)

Cadastro e edição de usuários

Validação de restrições de acesso
