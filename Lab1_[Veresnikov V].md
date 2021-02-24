1) Основные принципы Unix-way:
	
	Одна задача - одна программа
	Есть множество путей решения
	Все есть файл
	
2) Линус Торвальдс является разработчиком чего:
	
	Ядра ОС Linux 
	
3) Как посмотреть  название ядра системы из консоли?:
	
	uname -r
	
4) Промежутки измерения загрузки системы для команды uptime следующие:
	
	1,5,15 минут
	
5) какой командой узнать сколько занято на HDD:
	
	df -H
	
6) какие разделы содержит вывод команды vmstat:

	procs - количество процессов
	memory - память
	swap - память, которая использует файл подкачки для записи с/на диск(а)
	io - загрузка ввода-вывода
	cpu - загрузка процессора
	
7) Описать работу своего Linux дистрибутива: какое ядро, архитектура, размеры hdd, объеме ОЗУ, загрузке процессора и т.д:

	Ядро, архитектура:
	uname -ar
	Linux ubuntu 5.8.0-43-generic #49~20.04.1-Ubuntu SMP Fri Feb 5 09:57:56 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux

	Информация HDD:
	
	df -H
	
	Файл.система   Размер Использовано  Дост Использовано% Cмонтировано в	
	udev             2,1G            0  2,1G            0% /dev
	tmpfs            410M         2,0M  408M            1% /run
	/dev/sda5         73G          11G   59G           16% /
	tmpfs            2,1G            0  2,1G            0% /dev/shm
	tmpfs            5,3M         4,1k  5,3M            1% /run/lock
	tmpfs            2,1G            0  2,1G            0% /sys/fs/cgroup
	/dev/loop1        59M          59M     0          100% /snap/core18/1944
	/dev/loop0        59M          59M     0          100% /snap/core18/1988
	/dev/loop2        63M          63M     0          100% /snap/discord/120
	/dev/loop4       171M         171M     0          100% /snap/gnome-3-28-1804/145
	/dev/loop3        80M          80M     0          100% /snap/discord/121
	/dev/loop6       230M         230M     0          100% /snap/gnome-3-34-1804/66
	/dev/loop5       269M         269M     0          100% /snap/gnome-3-34-1804/36
	/dev/loop9        53M          53M     0          100% /snap/snap-store/467
	/dev/loop7        66M          66M     0          100% /snap/gtk-common-themes/1506
	/dev/loop10       33M          33M     0          100% /snap/snapd/10707
	/dev/loop11       54M          54M     0          100% /snap/snap-store/518
	/dev/loop8        69M          69M     0          100% /snap/gtk-common-themes/1514
	/dev/loop12       33M          33M     0          100% /snap/snapd/11036
	/dev/sda1        536M         4,1k  536M            1% /boot/efi
	tmpfs            410M          78k  410M            1% /run/user/1000


	Информация ОЗУ:
	free -h
		      всего        занято        свободно      общая  буф./врем.   доступно
	Память:       3,8Gi         3,0Gi           359Mi      139Mi      512Mi       500Mi
	Подкачка:     2,0Gi         239Mi           1,8Gi

	Загрузка процессора:
	uptime
	 13:26:23 up 35 min,  1 user,  load average: 1,70, 1,60, 1,47
