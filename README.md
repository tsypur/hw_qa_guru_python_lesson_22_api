# API tests automation для проекта Pet Store

> web-сайт [Pet Store demo API](https://petstore.swagger.io)

## Содержание проекта

Фреймворк для автоматизации тестирования API с интеграцией с корпоративными сервисами включающий:

- **Pydantic schemas** 
- **Allure reporting**
- **Endpoint architecture** 
- **Telegram notifications** 
- **TestOps integration** 
- **Jenkins pipeline** 

---

## Используемый стек

<p align="center">
<a href="https://www.jetbrains.com/pycharm/"><img src="media/logo/pycharm.svg" width="50" height="50"  alt="PyCharm"/></a>
<a href="https://www.python.com/"><img src="media/logo/python.svg" width="50" height="50"  alt="Python"/></a>
<a href="https://github.com/"><img src="media/logo/github.svg" width="50" height="50"  alt="GitHub"/></a>
<a href="https://docs.pytest.org/"><img src="media/logo/pytest.svg" width="50" height="50"  alt="Pytest 5"/></a>
<a href="https://github.com/allure-framework/allure2"><img src="media/logo/allure.svg" width="50" height="50"  alt="Allure"/></a>
<a href="https://www.jenkins.io/"><img src="media/logo/jenkins.svg" width="50" height="50"  alt="Jenkins"/></a>
<a href="https://qameta.io/"><img src="media/logo/allure_TO.svg" width="50" height="50"  alt="Allure TestOps"/></a>
</p> 

---

## Запуск теста

### Установка

```bash
# 1. Склонировать репозиторий
git clone https://github.com/tsypur/hw_qa_guru_python_lesson_22_api
cd hw_qa_guru_python_lesson_22_api

# 2. Создание виртуального окружения
python -m venv venv

# 3. Активация виртуального окружения
# macOS / Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# 4. Установка зависимостей
pip install -r requirements.txt
```

### Запуск тестов
```bash
# Запуск всех тестов
pytest --alluredir=allure-results

# Запуск конкретных тестов
pytest tests/test_get.py -v

# Просмотр Allure report
allure serve allure-results
```

---

### Примеры отчётов

#### <img src="media/logo/allure.svg" width="25" height="25"  alt="Allure"/></a> <a target="_blank" href="https://jenkins.autotests.cloud/job/C11-voronirina-diploma-UI/46/allure/">Allure Report</a> [Jenkins](https://jenkins.autotests.cloud/job/tsypur_hw_qa_guru_python_lesson_22_api/) Build

![Jenkins Build](media/jb.png)

#### Allure Overview  
![Allure Report](media/ao.png)

#### Детали тестового прогона
![Test Details](media/atd.png)

#### <img src="media/logo/allure_TO.svg" width="25" height="25"  alt="Allure"/></a> <a target="_blank" href="https://allure.autotests.cloud/launch/38541/">TestOps</a> [TestOps](https://allure.autotests.cloud/project/5057/dashboards) Runs

![TestOps Runs](media/to.png)

#### Тест-кейсы TestOps
![TestOps Test Cases](media/tod.png)


#### Telegram Notification
![Telegram](media/tg.png)