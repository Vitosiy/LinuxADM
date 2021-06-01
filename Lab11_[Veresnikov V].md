## 1. Сделать image контейнера с необходимым ПО для запуска sshd
[Dockerfile](Dockerfile)

[docker-compose](docker-compose.yml)

## 2. Запустить docker-compose поднять два ssh сервера
`docker-compose up --build -d`

## 3. Вход по паролю

![Картинка](1.png?raw=true)

![Картинка](2.png?raw=true)


## 4. Вход по ключу
2 -> 1


![Картинка](2->1.png?raw=true)


1 -> 2


![Картинка](1->2.png?raw=true)


## 5. Выполнить команду

![Картинка](ls.png?raw=true)


## 6. Передать файл

![Картинка](scp.png?raw=true)


## 7. Продемонстрировать простейший обмен данными с помощью утилиты netcat
Отправка


![Картинка](send.png?raw=true)


Прием


![Картинка](gatch.png?raw=true)

