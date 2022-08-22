#!/usr/bin/env python3
date = int(input("Введите день рождения:"))
month = int(input("Введите месяц рождения:"))
year = int(input("Введите год рождения:"))

if (date>=21 and date<=31 and month=='март') or( month=='Апрель' and date>=1 and date<=19):
    print("Знак зодиака:Овен")
elif (date>=20 and date<=30 and month==4) or( month==5 and date>=1 and date<=20):
    print("Знак зодиака:Телец")
elif (date>=21 and date<=31 and month==5) or( month==6 and date>=1 and date<=21):
    print("Знак зодиака:Близнецы")
elif (date>=22 and date<=30 and month==6) or( month==7 and date>=1 and date<=22):
    print("Знак зодиака:Рак")
elif (date>=23 and date<=31 and month==7) or( month==8 and date>=1 and date<=22):
    print("Знак зодиака:Лев")
elif (date>=23 and date<=31 and month==8) or( month==9 and date>=1 and date<=22):
    print("Знак зодиака:Дева")
elif (date>=23 and date<=30 and month==9) or( month==10 and date>=1 and date<=23):
    print("Знак зодиака:Весы")
elif (date>=24 and date<=31 and month==10) or( month==11 and date>=1 and date<=22):
    print("Знак зодиака:Скорпион")
elif (date>=23 and date<=30 and month==11) or( month==12 and date>=1 and date<=21):
    print("Знак зодиака:Стрелец")
elif (date>=22 and date<=31 and month==12) or( month==1 and date>=1 and date<=20):
    print("Знак зодиака:Козерог")
elif (date>=21 and date<=31 and month==1) or( month==2 and date>=1 and date<=18):
    print("Знак зодиака:Водолей")
elif (date>=19 and date<=29 and month==2) or( month==3 and date>=1 and date<=20):
    print("Знак зодиака:Рыбы")
