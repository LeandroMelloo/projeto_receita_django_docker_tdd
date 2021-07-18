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
docker-compose run --rm app sh -c "python manage.py test && flake8"

# Comando de criação do app Django com docker

docker-compose run app sh -c "python manage.py startapp core"
docker-compose run --rm app sh -c "python manage.py startapp user"

# Comando de criação da(s) model(s) com docker

docker-compose run app sh -c "python manage.py makemigrations core"

# Comando de criação do superusuario

docker-compose run app sh -c "python manage.py createsuperuser"
