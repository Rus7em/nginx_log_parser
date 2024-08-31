# nginx_log_parser
## URLs
/admin/
/api/
/swagger/
/redoc/

## создания образа
docker build -it nginx_log_parser .

## запуска контейнера c монтированой директории 
docker run -d -p 8000:8000 -v <путь к деректории с файлом>:/app/data --name nginx_log_parser_container nginx_log_parser
### если текущая директория
docker run -d -p 8000:8000 -v $(pwd):/app/data --name nginx_log_parser_container nginx_log_parser

## установка суперпользователя для входа в админку
docker exec -it <id контейнера> python manage.py createsuperuser

## загрузка файла с логами
docker exec -it <id контейнера> python manage.py --path /app/data/nginx_json_logs.txt

