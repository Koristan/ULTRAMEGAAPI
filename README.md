# МИНИГАЙД ДЛЯ ВАС, C#'ники

Что и как создать, где пукнуть, куда нажать для начала

## Создаем окружение

1. Открываем cmd в директории проекта
2. Пишем туда 'python -m venv venv'
3. Потом его активируем командой venv\Scripts\activate.bat (Это для windows) | source venv/Scripts/activate (Это для Linux (Ну тут таких извергов нет))
4. И, наконец, пишем 'pip install -r req.txt'

Возникшие в процессе ошибки исправляйте сами, у меня все норм :З

## Запуск сервиса

Если все ок - пишите супер-пупер команду все в том же cmd:

uvicorn src.service:app --host localhost --port 8000 --log-config=log_config.yaml

Если все ок, то вы увидите примерно это:

```cmd
2024-03-21 16:16:34,389 - src.service - INFO - Загружена конфигурация сервиса по пути: .\src\configs\service_config.json
2024-03-21 16:16:34,392 - uvicorn.error - INFO - Started server process [35632]
2024-03-21 16:16:34,392 - uvicorn.error - INFO - Waiting for application startup.
2024-03-21 16:16:34,392 - uvicorn.error - INFO - Application startup complete.
2024-03-21 16:16:34,397 - uvicorn.error - INFO - Uvicorn running on http://localhost:8000 (Press CTRL+C to quit)
```

Ну а дальше вы все знаете.
