### 1. Что вы можете сказать об адресе http://205938.itmo.xyz/? Почему именно такие цифры?
Адрес 205938.itmo.xyz это поддомен itmo.xyz.

Цифры 205938 это табельный номер ИСУ. [В данном случае Ваш](https://isu.ifmo.ru/pls/apex/f?p=2143:3:111825262076412::NO:RP:PID:205938 ))0)0))

### 2.	Для каждого из вас в зоне itmo.xvz подготовлен ровно 1 домен, который нужно угнать. Сделайте так, чтобы при переходе по нему отображалась ваша фамилия.
Для нашей группы каждому были выделены домены вида {табельный_номер_ИСУ}.itmo.xyz

Мой табельный номер - 282858 и такой домен есть:

    dig 282858.itmo.xyz

    ; <<>> DiG 9.16.1-Ubuntu <<>> 282858.itmo.xyz
    ;; global options: +cmd
    ;; Got answer:
    ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 41257
    ;; flags: qr rd ra; QUERY: 1, ANSWER: 5, AUTHORITY: 0, ADDITIONAL: 1

    ;; OPT PSEUDOSECTION:
    ; EDNS: version: 0, flags:; udp: 512
    ;; QUESTION SECTION:
    ;282858.itmo.xyz.               IN      A

    ;; ANSWER SECTION:
    282858.itmo.xyz.        299     IN      CNAME   itmo-osint-282858.github.io.
    itmo-osint-282858.github.io. 3599 IN    A       185.199.109.153
    itmo-osint-282858.github.io. 3599 IN    A       185.199.111.153
    itmo-osint-282858.github.io. 3599 IN    A       185.199.110.153
    itmo-osint-282858.github.io. 3599 IN    A       185.199.108.153

    ;; Query time: 375 msec
    ;; SERVER: 8.8.8.8#53(8.8.8.8)
    ;; WHEN: Sat Oct 03 15:39:20 MSK 2020
    ;; MSG SIZE  rcvd: 149

Процесс перехвата домена:

1. Создание репозитория на github c именем itmo-osint-282858.github.io.

2. Создание файла CNAME в этом репозитории с таким содержимым:

        282858.itmo.xyz
3. Теперь Github по имени [282858.itmo.xyz](http://282858.itmo.xyz) резолвит сайт на gevol69.github.io/itmo-osint-282858.github.io.

### 3.	Где расположено это место 33.357778S, 151.442750Е? Переведите координаты в минуты и секунды.
Место находится [здесь](https://www.google.com/maps/place/33°21'28.0%22S+151°26'33.9%22E/@-33.357778,151.4405613,723m/data=!3m2!1e3!4b1!4m5!3m4!1s0x0:0x0!8m2!3d-33.357778!4d151.44275) - 9 Bon-Mace Cl, Berkeley Vale NSW 2261, Австралия

Перевод координат производил [тут](http://the-mostly.ru/konverter_geograficheskikh_koordinat.html)

33.357778S = 33°21′28″ ю.ш. (33 градуса, 21 минута, 28 секунд)

151.442750Е = 151°26′34″ в.д. (151 градус, 26 минут, 34 секунды)

### 4.	Напишите скрипт, который каждые 5 минут будет выдавать новые статьи, появившиеся на https://habr.com/ru/all/
Скрипт находится в файле [script_habr.py](https://github.com/gevol69/osint_itmo/blob/master/osint_hw3/script_habr.py)

### 5.	Поизучайте challenge https://osint-i1.thinkific.com/courses/take/osint-challenge: Кто его авторы? Попробуйте решить парочку заданий оттуда
Автор этого челленджа - Andy F1 (Andrew Fordred - andy1@intelligence-i1.com)
Глобальная цель как я понял - провести расследование, исходные данные - [этот видос](https://drive.google.com/drive/folders/1ErZfdgPfJeqcp6xegzmST6Ulxme5W1jM)

#### Вопрос 1

Найти время и место наблюдения за автомобилем с этим номером, используя видео.

![](https://s3.amazonaws.com/thinkific/file_uploads/100237/images/aa0/089/a8d/1565678098131.jpg)

[Добро пожаловать в Лас Вегас!](https://www.google.ru/maps/@36.0819248,-115.1725663,3a,75y,355.31h,90.63t/data=!3m6!1e1!3m4!1sKjgBlUJxf5D50Grblufg_w!2e0!7i16384!8i8192?hl=ru)

Автомобиль найден на 36:07

![](https://image.prntscr.com/image/8MZMjD5ASLWEUSdKvmOnIg.png)
Ищем дату, когда было снято видео. На 13:20 есть цифровой борд с информацией. На нем промелькнула точная стоимость фондового индекса Доу Джонса:

![](https://image.prntscr.com/image/KZkxTs54Rj2CH-R0eD90vA.png)

Стоимость 24585.43 была только 13 декабря 2017го года.

![](https://image.prntscr.com/image/hyNBzfFQSaa9l1zqNLYzlA.png)


Внимательно изучал видео дальше и увидел на 22:37 и точное время и дату:

![](https://image.prntscr.com/image/J5NIJrgERHqGKLzgEIMr2Q.png)

4:53 - это время, когда на видео было 22:37.

Автомобиль найден на 36:07

36:07 - 22:37 = 13:30

4:53:00 + 0:13:30 = 5:06:30


То есть приблизительная дата и время обнаружения автомобиля - **14.12.2017 в 5:06 - 5:07 утра**

Чтобы обнаружить конкретное место, можно погулять по гугл картам одновременно с автомобилем, который снимает Лас-Вегас на видео, место обнаружения [здесь](https://www.google.ru/maps/@36.1714189,-115.1392054,3a,75y,32.83h,90.28t/data=!3m6!1e1!3m4!1sqWIB1qfw6q5d21x3LnLx-Q!2e0!7i16384!8i8192?hl=ru) - **северный бульвар Лас Вегас**

#### Вопрос 3
Минута на видео: 27:33

Little Vegas Chapel - ELVIS

![](https://image.prntscr.com/image/V867IshLTC_1t7acTQ4Yow.png)

Отель - Holiday House Motel

[Камера](https://www.earthcam.com/usa/nevada/lasvegas/index.php?cam=wedding)

IP-адрес что-то найти не получается. Комбайны ничего не дают.

#### Вопрос 4

Стивен Пэддок вечером 1 октября 2017 года открыл огонь по толпе с 32го этажа 135й комнаты отеля Mandalay Bay Hotel.

30.09.2017 в 14:57 он был замечен на кадрах видеонаблюдения.

Не нашел видео с камер конкретно в 14:57, но нашел в 14:48 - он заходил в лифт и спускается к машине.

![](https://image.prntscr.com/image/QvVRNf4UTnGWcOJjCKNJWg.png)

Сразу после этого в 15:06 он садится в свою машину.

![](https://image.prntscr.com/image/aKd4oCdvRwiV1oiN25A-Cg.png)

Информацию нашел [здесь](https://www.nytimes.com/2018/03/22/us/las-vegas-shooting-stephen-paddock.html)