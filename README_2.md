Инструкция для запуска:
1. Выполнить в терминале команду: docker-compose build для сбора сервисов, описанных в конфигурационных файлах
2. Выполнить в терминале команду: docker-compose up для развёртывания сервисов веб-приложений и создания из docker-образа новые контейнеры, а также сети, тома и все конфигурации, указанные в файле Docker Compose
4. Выполнить в терминале команду: docker-compose exec app python manage.py migrate для применения миграций базы данных
5. Остановить контейнер в терминале нажатием сочетаний клавишь CTRL+C
