# Meu primeiro projeto Django
# Instrução para baixar, editar e executar local
1. clone do projeto
## git clone https://github.com/vfsphotos/projeto1.git
2. entre na pasta do projeto e crie um ambiente virtual python
cd projeto1
python -m venv .venv

Caso somente "python" não funcione, faça usando o "python3"

3. ative o ambiente virtual no windows:
## .venv\Scripts\activate

no linux:
source .venv/bin/activate

4.instale as dependências
pip install -r requirements-dev.txt
5. execute as migrações
python manage.py migrate
6. execute o servidor
python manage.py runserver
7. acesse o projeto no navegador
http://127.0.0.1:8000/

