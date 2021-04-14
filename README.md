Projeto de desenvolvimento web feito em django com a funcionalidade de uma lista telefônica.

Neste projeto foram criadas as funcionalidades de criar, editar, excluir e filtrar um contato pelo seu nome, podendo ser utilizado o nome completo ou parte dele na busca. Os contatos são organizados por ordem alfabética de seus nome e, ao serem criados seus números passam por validação realizada pela biblioteca instalada "django-phone-field".

Ao baixar o projeto, o primeiro passo é ativar o venv, no windows, no diretório em que o venv se encontra, usa-se:

venv\Scripts\activate.bat

depois deve-se entrar no diretório com o manage.py e instalar os itens necessários:

pip install -r requirements.txt

Com isto, basta apenas rodar:

python manage.py runserver 

Vale ressaltar que ao não utilizar o docker, necessita-se criar um banco de dados, ou voltar a confiração para o default.
