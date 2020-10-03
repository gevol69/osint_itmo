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

33.357778S = -33°21′28″ (-33 градуса, 21 минута, 28 секунд)

151.442750Е = 151°26′34″ (151 градус, 26 минут, 34 секунды)

### 4.	Напишите скрипт, который каждые 5 минут будет выдавать новые статьи, появившиеся на https://habr.com/ru/all/
Скрипт находится в файле [script_habr.py](https://github.com/gevol69/osint_itmo/blob/master/osint_hw3/script_habr.py)

### 5.	Поизучайте challenge https://osint-i1.thinkific.com/courses/take/osint-challenge: Кто его авторы? Попробуйте решить парочку заданий оттуда