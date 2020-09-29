### 1. Найти настоящий IP адрес сайта [osint.itmo.xyz](https://osint.itmo.xyz)
itmo.xyz - 31.184.255.217 ([найдено тут](https://gmap.io/dns/domain/itmo.xyz) и [тут](https://viewdns.info/iphistory/?domain=itmo.xyz))

Следующей командой было получено подтверждение того, что osint.itmo.xyz и itmo.xyz находятся на одном IP адресе:

    curl https://osint.itmo.xyz --resolve osint.itmo.xyz:443:31.184.255.217

    Gotcha
    <!-- flag{cf9f0bcccfd3036c4a3c2993d34275b2} -->

Следовательно, osint.itmo.xyz также имеет IP адрес 31.184.255.217

### 2. Найти все домены, которые ссылаются на данный IP ↖
| Domain  |  Source  |
|---------|---------|
| californiahomeloanz.com  | [источник](https://viewdns.info/reverseip/?host=31.184.255.217&t=1)  |
| fastfoodcareers.net  |[источник](https://viewdns.info/reverseip/?host=31.184.255.217&t=1)  |
| quiz.itmo.xyz  |[источник](http://prntscr.com/uq2dlk)|
| confg.plus07.sistemaatualizado.com.de | [источник](https://hackertarget.com/reverse-ip-lookup/) |
| sms.sushishop.ru | [источник](https://hackertarget.com/reverse-ip-lookup/) |

Эти домены отвечают 301м кодом ошибки:

    l5.itmo.xyz
    demo.wad.itmo.xyz
    jfjfjfjfjfjff.itmo.xyz
    quiz.itmo.xyz
    wad.itmo.xyz
    comment.cloud.itmo.xyz
    20.itmo.xyz


### 3. Составить запросы для выдачи сайтов, которые ссылаются на codex.so (google, yandex, yahoo/bing)
[Google](https://www.google.com/search?q=link:codex.so+%7C+intext:codex.so&newwindow=1&client=firefox-b-d&sxsrf=ALeKk00eZtxX3jKSLQOMpHFQco0kVoIC-g:1601398725678&tbas=0&source=lnt&sa=X&ved=2ahUKEwiz2b-R647sAhXBwosKHf4YDg4QpwV6BAgGEBk&biw=2560&bih=938)  - link:codex.so | intext:codex.so

[Yandex](https://yandex.ru/search/?text=%2B%22codex.so%22&lr=2)  - +"codex.so"

[Yahoo](https://search.yahoo.com/search?n=10&ei=UTF-8&va_vt=any&vo_vt=any&ve_vt=any&vp_vt=any&vst=0&vf=all&vm=i&fl=0&p=%22codex.so%22&vs=)  - "codex.so"

[Bing](https://www.bing.com/search?q=%2B%22codex.so%22&form=QBLH&sp=-1&pq=%2B%22codex.so%22&sc=1-11&qs=n&sk=&cvid=50259D6A70174A10AB88C6D5C834B033)  - +"codex.so"

### 4. Найдите домен, связанный с фастфудом, который ведёт на [itmo.xyz](https://itmo.xyz), выясните всё о нём
fastfoodcareers.net ([найден тут](https://viewdns.info/reverseip/?host=31.184.255.217&t=1) и [тут](https://gmap.io/dns/host/31.184.255.217/domains))

У домена есть 2 поддомена, которые не работают:

    mail.fastfoodcareers.net
    20.fastfoodcareers.net

Информация с whois:

    Registry Domain ID: 1926174549_DOMAIN_NET-VRSN
    Registrar WHOIS Server: whois.launchpad.com
    Registrar URL: LaunchPad.com
    Updated Date: 2020-04-21T03:31:23Z
    Creation Date: 2015-05-06T16:45:57Z
    Registrar Registration Expiration Date: 2021-05-06T16:45:57Z
    Registrar: Launchpad, Inc. (HostGator)
    Registrar IANA ID: 955
    Domain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited
    Registry Registrant ID: Not Available From Registry
    Registrant Name: Domain Admin
    Registrant Organization: Privacy Protect, LLC (PrivacyProtect.org)
    Registrant Street: 10 Corporate Drive
    Registrant City: Burlington
    Registrant State/Province: MA
    Registrant Postal Code: 01803
    Registrant Country: US
    Registrant Phone: +1.8022274003
    Registrant Email: contact@privacyprotect.org
    Registry Admin ID: Not Available From Registry
    Admin Name: Domain Admin
    Admin Organization: Privacy Protect, LLC (PrivacyProtect.org)
    Admin Street: 10 Corporate Drive
    Admin City: Burlington
    Admin State/Province: MA
    Admin Postal Code: 01803
    Admin Country: US
    Admin Phone: +1.8022274003
    Admin Email: contact@privacyprotect.org
    Registry Tech ID: Not Available From Registry
    Tech Name: Domain Admin
    Tech Organization: Privacy Protect, LLC (PrivacyProtect.org)
    Tech Street: 10 Corporate Drive
    Tech City: Burlington
    Tech State/Province: MA
    Tech Postal Code: 01803
    Tech Country: US
    Tech Phone: +1.8022274003
    Tech Email: contact@privacyprotect.org
    Name Server: dns1.namecheaphosting.com
    Name Server: dns2.namecheaphosting.com
    DNSSEC: Unsigned
    Registrar Abuse Contact Email: abuse@websitewelcome.com
    Registrar Abuse Contact Phone: +1.713-574-5287


### 5. https://30.ctf.su/tasks/MN_blblbl, https://30.ctf.su/tasks/KR_paz
https://30.ctf.su/tasks/MN_blblbl - Виталий Бутерин (поиск по картинке в Яндексе)

https://30.ctf.su/tasks/KR_paz - Цутому Симомура (поиск по картинке в гугле)

### 6. https://freehackquest.com/quest/100, https://freehackquest.com/quest/102
https://freehackquest.com/quest/100 - Albuquerque

https://freehackquest.com/quest/102 - ЛЯПАС

### 7. https://hy17-fbi.spb.ctf.su/
[Фото с маками с инстаграма Ыжа](https://www.instagram.com/p/BZ9dLnUgnXJ/)

На фото запечатлены следующие мак адреса:

    92:2A:A8:9A:2E:76
    AC:3:1E:f6:6F:B1
    B0:C5:54:1A:69:31
    00:10:68:A9:53:5C
    9C:C7:A6:BE:F9:69
    92:E6:2C:27:40:70
    9C:1C:12:2B:A4:68

С помощью wigle были найдены координаты этих маков и искомая улица - Louvigny

    The FBI squad found Yzh there!
    Here is your flag: hy17{ffb9fec8c69eb0e0eb34d1d22529194b}

### 8. По легенде, пользователь johnsmith130405@ya.ru заказал взлом сайта, найдите исполнителя
Был найден [гитхаб](https://github.com/johnsmith130405/SimpleUtilit/blob/master/Main.cs) Джона Смита и в коде на второй строке эта почта: johnsmith130405@mailforspam.com

[Письмо с mailforspam](https://www.mailforspam.com/mail/johnsmith130405/1)

[Твиттер Матвея Королёва](https://twitter.com/matveiikorolev)

[Максим из твиттера Матвея](https://twitter.com/maximgolovatov)

    flag{to_be_or_not_to_be}

