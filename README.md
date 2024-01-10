# Создаём битлинки и считаем количество кликов.
Скрипт через API Bitly сокращает ссылки и показывает
количество кликов по сокращённой ссылке.
## Окружение
### Требования
Python3 должен быть установлен. Установите необходимые библиотеки:
```bash
python3 -m venv env 
```
```bash
source env/bin/activate
```
```bash
pip3 install -r requirements.txt
```
### Переменные окружения
- BITLY_TOKEN
1. Создайте файл ".env" рядом со скриптом.
2. Запишите в .env файл ваш токен API Bitly.com
### Получить токен
1. Зарегистрируйтесь на сайте [bitly.com](https://bitly.com/a/sign_up)
2. Получите токен доступа к API. [Вот инструкция.](https://support.bitly.com/hc/en-us/articles/230647907-How-do-I-generate-an-OAuth-access-token-for-the-Bitly-API-#:~:text=Log%20in%20to%20your%20Bitly,password%20and%20click%20Generate%20token.)
## Запуск
Запустите файл script.py с помощью CLI:
```bash
python3 script.py
```
Пример работы:  
``` bash
$ python3 script.py https://slides.dvmn.org/voron434/requests/#/3
Ваш битлинк:https://bit.ly/3vxU7Ct
```
``` bash
$ python3 script.py https://bit.ly/3vxU7Ct
Всего кликов за всё время: 1
```
## Цель проекта
Код написан в учебных целях в рамках курса о работе Python с API сервисами.  
[DEVMAN.org](https://devman.org)
