# Тестовое задание BRENDWALL
## Создайте файл .env в корне проекта. 
### Пример: 
```
DEBUG=True
SECRET_KEY=django-insecure-jeg%!c1$-sampi3@%6w@m1x*ghwg_#e!8jifry7!e*l8)uuzkh
DOMAIN_NAME=http://0.0.0.0

DJANGO_SUPERUSER_PASSWORD=admin
DJANGO_SUPERUSER_EMAIL=admin@gmail.com
DJANGO_SUPERUSER_USERNAME=admin
```
 
## Запуск приложения
```
docker compose up --build
```

## Остановка приложения
```
docker compose down -v
```
