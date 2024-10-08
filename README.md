## Тестовое задание: Породистые котята
**Доп. информация под блоком запуска*

**В приложение импортируются тестовые данные автоматически*

**Для авторизации создано 2 тестовых аккаунта: admin/admin и test/test**

### Запуск проекта

1. Клонируйте репозиторий
```
git clone https://github.com/dianartv/kitten_test_project.git
```
2. Создайте директорию для проекта и перейдите в неё
3. Создайте виртуальное окружение командой в консоли
```
python -m venv venv
```
4. Активируйте виртуальное окружение командой
  
Linux/macOS
```
source \venv\Scripts\activate
```
Windows
```
.\venv\Scripts\activate
```
5. Перейдите в корень проекта
```
cd .\kitten_test_project\
```
6. Выполните команду для docker. Дождитесь создания контейнеров
```
docker-compose build
```
7. Запустите проект в докере командой
```
docker-compose up
```
8. Приложение работает по адресу:
```
http://127.0.0.1:8000/api/v1/kitten/
```
Документация доступна по адресу:
```
http://127.0.0.1:8000/swagger/
```

## Дополнительная информация
### Тесты
Запуск
```
pytest tests
```
Фикстуры с тестовыми данными импортируются автоматически
### Стэк технологий
1. Django, DRF.База данных, PostgreSQL
2. DRF
3. PostgreSQL

# Техническое задание

Тестовое задание:
 Стек:
Django, DRF.База данных, PostgreSQL или SQLite
Допускается использование вспомогательных библиотек и расширений на усмотрение кандидата.

 Цель задания:
 
Спроектировать REST API онлайн выставка котят:
                                                                       	
 API должно иметь следующие методы:
 - Получение списка пород
- Получение списка всех котят
- Получение списка котят определенной породы по фильтру.
- Получение подробной информации о котенке.
- Добавление информации о котенке
- Изменение информации о котенке
- Удаление информации о котенке
- JWT Авторизация пользователей
 
Бизнес логика:
 
Каждый котенок должен иметь – цвет, возраст (полных месяцев) и описание.
Удалять изменять или обновлять информацию пользователь может только о тех животных, которых он добавил сам.

 При возникновении неоднозначности в задаче – принятие конечного решения остается за кандидатом.

 Требования к приложению:



- Описание запуска приложения
- Документация в формате Swagger (должна быть ссылка на API)
 - Минимум данных, с помощью которых будет возможность проверить работоспособность приложения.
Будет плюсом:
Дополнительные возможности:
1.     Возможность оценки котят (от 1 до 5) каждый пользователь может просматривать котят других пользователей и ставить им оценки (от 1 до 5).
Тесты:
2.     Написать тесты с использованием pytest для проверки работоспособности функций API.
Контейнеризация:
3.     Обернуть приложение в контейнер Docker и docker-compose – для быстрого запуска инфраструктуры (например PostgreSQL)
Оценка:
-       Правильно спроектированная база данных для хранения сущностей
-       Чистота и логичность кода
-       Навыки использования фреймворка Django (включая запросы DjangoORM)
-       Наличие и качество тестов (если реализовано)
-       Docker конфигурация (если реализовано).


