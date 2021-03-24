1) Как отобразить 4 последних выполненных команды?:

	history 4

2) Перевести задание в фоновый режим в bash можно командой:

	bg pid

3) Какая комбинация клавиш переключит вас на 4-ю виртуальную консоль?:

	ctrl+alt+f4

4) Какая переменная среды содержит путь к домашнему каталогу?:

	HOME

5) Установить в bash переменную MYVAR в качестве системной можно командой?:

	export MYVAR

6) Какие комбинации клавиш позволят выделить несколько файлов в Midnight Commander?:

	ctrl+t


7) Что выведет на экран этот сценарий?:


#!/bin/bash
VAR=`echo 'test'`
VAR2=`echo '$VAR'`
echo $VAR2

	Выведет $VAR
 

8) Что выведет на экран это сценарий?:


#!/bin/bash
cd /etc
VAR="$PWD"
if [ -n "$VAR" ]; then
 echo "$VAR"
else
 echo '$VAR'
fi 

	Выведет /etc
 

9) Что выведет на экран этот сценарий?:


#!/bin/bash
A=1
B=2
if [ $A -eq $B  ]; then
 echo '$A'
else
 echo "$B"
fi

	Выведет 2
	
	
 Задание №1:
 
 	![linux](https://sun9-58.userapi.com/impg/R6tiopgd2TZIbYmoSn1VPYr7zpsWFTGlVZErDA/OHSBwUd5DC4.jpg?size=552x412&quality=96&sign=de751f4a7f3f544caff225043a06a096&type=album)
 
 
 Задание №2:
 
 
    1)Настроить tmux:
    	
	echo "set -g mouse on" > ~/.tmux.conf
    	
    2)Научиться запускать:
    
	tmux
	
    3)Создавать новые pane:
    
    	CTRL+B c
    
    4)Делать split pane:
    
    	CTRL+B SHIFT+% - вертикальное деление
    	CTRL+B SHIFT+" - горизонтальное деление
    
    5)Управление мышью:
    
    	![linux](https://sun9-37.userapi.com/impg/zn6yfyxxipHOBbtpQtY6S_CR8CtK5GlBp8MqLg/imvaHTTIWhc.jpg?size=1920x1080&quality=96&sign=c5bf898bed66983600cb115b7b709471&type=album)
    
    6)Zoom:
    
    	 CTRL+B z
    
    7)Закрытие pane:
    
    	CTRL+B x
    
    8)Detach:
    
	CTRL+B d
