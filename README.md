### **С помощью этого проекта вам больше не нужно каждые 3 часа заходить в Hamster Kombat чтобы забрать заработок** 

#### Требования:

* <u>доступ к вашему telegram аккаунту с web.telegram.org</u>

* <u>python версии 3.10 или выше</u> 

  

---





#### Получаем ваш секретный токен Hamster:

1. Делаем все по инструкции [тут (клик)](https://github.com/mudachyo/Hamster-Kombat?tab=readme-ov-file#%D1%81%D0%BF%D0%BE%D1%81%D0%BE%D0%B1-1)
2. Переходим в [Hamster Kombat (клик)](https://web.telegram.org/a/#?tgaddr=tg%3A%2F%2Fresolve%3Fdomain%3Dhamster_kombat_bot)
3. Открываем игру, и она у вас должна загрузится 
4. Нажимаем <u>F12</u> и переходим в раздел <u>Network</u> или <u>Сеть</u>
5. Выбираем в подразделе Fetch ([скрин](https://i.imgur.com/RPJhLz9.png)) и вставляем в Filter или Фильтр "`https://api.hamsterkombat.io/auth/me-telegram`"
6. Нажимаем на 3 точки в Hamster Kombat ([скрин](https://i.imgur.com/jXQIdmQ.png)) и нажимаем "<u>Reload</u>" или "<u>Обновить</u>"
7. Находим наш запрос в разделе <u>Network</u> или <u>Сеть</u> ([скрин](https://i.imgur.com/7YBfyWM.png)) 
8. Крутим, то что я обозначил в фиолетовый прямоугольник вниз и находим <u>Authorization</u> (он находится в <u>Request Headers</u> или <u>Заголовки запросов</u>) ([скрин](https://i.imgur.com/7uQszz8.png))
9. Копируем все, кроме "<u>Bearer</u>" ([скрин](https://i.imgur.com/VeUMKhU.png)) - это ваш токен



#### Устанавливаем скрипт на вашу систему

##### Инструкция для Windows:



Скачиваем репозиторий через git (`git clone https://github.com/frymex/hamster_eternal_online`) 

или через zip архивом: [клик](https://github.com/frymex/hamster_eternal_online/archive/refs/heads/main.zip) 



Создаем виртуальное окружение python (`python -m venv .venv`)

Активируем его `(.\ .venv\Scripts\activate.bat`)

Активируем конфиг: переменуйте *config.py.example* в *config.py*


##### Инструкция для Ubuntu:

Скачиваем репозиторий через git (`git clone https://github.com/frymex/hamster_eternal_online`) 

или через zip архивом: [клик](https://github.com/frymex/hamster_eternal_online/archive/refs/heads/main.zip) 

создаем виртуальное окружение python (`python3 -m venv .venv`)

активируем его (`source .venv/bin/activate`)

активируем конфиг: `cp config.py.example config.py`


##### Установите ваш API token в config.py


##### Установка нужных модулей:

`pip install -r requirements.txt`





##### Запуск скрипта:

`python main.py`



(запуск в фоне (только для linux)):

`nohup python main.py &`


---

### Вы можете поддержать меня отправив донат: 

https://donate.cazqev.com/
