# Создаём битлинки и считаем количество кликов.
Скрипт предлагает пользователю ввести ссылку. Если ссылка является битлинком юзера (определяемого по токену bit.ly) то скрипт запросит и выведет информацию о количестве кликов по битлинку.
Если ссылка не является битлинком, скрипт запросит новый битлинк для ссылки и выведет битлник на экран. Скрипт работает сервисом Bitly, вам понадобится получить токен.
## Окружение
### Требования
Python3 должен быть установлен. Установите необходимые библиотеки:
```bash
puthon3 -m venv env 
```
```bash
source env/bin/activate
```
```bash
pip3 install -r requirements.txt
```
### Переменные окружения
- TOKEN_BITLY
1. Создайте файл ".env" рядом со скриптом.
2. Запишите в .env файл ваш токен API Bitly.com
### Получить токен
1. Зарегистрируйтесь на сайте [bitly.com](https://bitly.com/)
2. Получите токен доступа к API. [Вот инструкция.](https://support.bitly.com/hc/en-us/articles/230647907-How-do-I-generate-an-OAuth-access-token-for-the-Bitly-API-#:~:text=Log%20in%20to%20your%20Bitly,password%20and%20click%20Generate%20token.)
## Запуск
Запустите файл script.py с помощью CLI:
```bash
python3 script.py
```
Пример работы:  
``` bash
$ python3 script.py
Введите ссылку: 
https://slides.dvmn.org/voron434/requests/#/3
Ваш битлинк:https://bit.ly/3vxU7Ct
```
``` bash
$ python3 script.py
Введите ссылку: 
https://bit.ly/3vxU7Ct
Всего кликов за всё время: 1
```
## Цель проекта
Код написан в учебных целях в рамках курса о работе Python с API сервисами.  
[DEVMAN.org](https://devman.org)