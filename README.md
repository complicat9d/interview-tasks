# Запуск проекта

## Через Docker
_Пререквизит: установленный на машину docker_

Команды для запуска в заданной последовательности:
```bash
docker build -f Dockerfile . -t test_tasks
docker run test_tasks
```
Вывод логов контейнера при корректном прохождении тестов из папки `tests`:
```text
.......                                                                  [100%]
7 passed in 0.19s

```
## Мануально
_Пререквизит: установленный на машину python (3.11+)_

Команды для запуска в заданной последовательности:
```bash
python -m pip install --upgrade pip pipenv
pipenv install --deploy --system --clear
pytest
```