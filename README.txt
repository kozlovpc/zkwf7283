Django проект gopy9249
Основное приложение gopy9250

установить nginx 1.28.0 
Обязательно попробовать запустить стандартную страницу nginx

Скачать PostgreSQL последней версии
для удобства установить PgAdmin 4 и в нём подключить PostgreSQL

Задать пароль для сервера "pass" (без кавычек)
Создать таблицу test (не создавать поля, Django автоматически создаёт)

Команды при развороте .venv в проекте Django

0)Развернуть .venv в котором установить Django и все необходимые библиотеки
Данные библиотеки при отсутствии отображаются в extensions

В настройках конфигурации 
nginx-1.28.0\conf\nginx.conf необходимо поменять конфигурацию

Файл конфигурации находится в GitHub репозитории
Его необходимо заменить

обновить pip (python -m pip install --upgrade pip)

1) Set-ExecutionPolicy RemoteSigned -Scope Process -Force
2) .\.venv\bin\activate
3) pip install waitress
4) waitress-serve --port=8000 gopy9249.wsgi:application