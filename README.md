# nginx_log_parser
## URLs
/admin/
/api/
/swagger/
/redoc/

## создания образа
docker build -it nginx_log_parser .

## загрузка файла
docker run -it --name temp_container -v $(pwd):/app/data nginx_log_parser python manage.py log_loading --path /app/data/nginx_json_logs.txt
docker commit temp_container nginx_log_parser_with_data 
docker rm temp_container

## запуска контейнера
docker run -d -p 8000:8000 --name nginx_log_parser_container nginx_log_parser_with_data
## установка суперпользователя для входа в админку
docker exec -it <id контейнера> python manage.py createsuperuser
