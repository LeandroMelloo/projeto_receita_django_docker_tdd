# Comando de instalação do Dockerfile

docker build .

# Comando de instalação do docker-compose

docker-compose build

# Comando de criação do projeto Django com docker

docker-compose run app sh -c "django-admin.py startproject app ."

# Comando para testes unitarios no python com docker

docker-compose run app sh -c "python manage.py test"

# Comando para testes unitarios no python com docker

docker-compose run app sh -c "python manage.py test && flake8"

# Comando de criação do app Django com docker

docker-compose run app sh -c "python manage.py startapp core"

# Comando de criação da(s) model(s) com docker

docker-compose run app sh -c "python manage.py makemigrations core"
