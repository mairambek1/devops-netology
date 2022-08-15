# Домашнее задание к лекции 2.«Условные конструкции. Операции сравнения»

## Задача №1
Задачи на [hackerrank](https://www.hackerrank.com/domains/python):  
Решить задачу на hackerrank ["Python If-Else"](https://www.hackerrank.com/challenges/py-if-else/problem).  

## Задача №2
На лекции мы рассматривали пример для военкомата. Сейчас мы знаем про его рост. Расширить это приложение следующими условиями:
1. Проверка на возраст призывника.
2. Количество детей.
3. Учится ли он сейчас.

## Задание №3
Разработать приложение для определения знака зодиака по дате рождения.  
Пример:  
```
Введите месяц: март
Введите число: 6

Вывод:
Рыбы
```
Решение:
```
#!/usr/bin/env python3

month = str(input("Введите месяц:"))
date = int(input("Введите число:"))


if (date>=21 and date<=31 and month=="Март") or( month=="Апрель" and date>=1 and date<=19):
    print("Знак зодиака:Овен")
elif (date>=20 and date<=30 and month=="Апрель") or( month=="Май" and date>=1 and date<=20):
    print("Знак зодиака:Телец")
elif (date>=21 and date<=31 and month=="Май") or( month=="Июнь" and date>=1 and date<=21):
    print("Знак зодиака:Близнецы")
elif (date>=22 and date<=30 and month=="Июнь") or( month=="Июль" and date>=1 and date<=22):
    print("Знак зодиака:Рак")
elif (date>=23 and date<=31 and month=="Июль") or( month=="Август" and date>=1 and date<=22):
    print("Знак зодиака:Лев")
elif (date>=23 and date<=31 and month=="Август") or( month=="Сентябрь" and date>=1 and date<=22):
    print("Знак зодиака:Дева")
elif (date>=23 and date<=30 and month=="Сентябрь") or( month=="Октябрь" and date>=1 and date<=23):
    print("Знак зодиака:Весы")
elif (date>=24 and date<=31 and month=="Октябрь") or( month=="Ноябрь" and date>=1 and date<=22):
    print("Знак зодиака:Скорпион")
elif (date>=23 and date<=30 and month=="Ноябрь" ) or( month=="Декабрь" and date>=1 and date<=21):
    print("Знак зодиака:Стрелец")
elif (date>=22 and date<=31 and month=="Декабрь") or( month=="Январь" and date>=1 and date<=20):
    print("Знак зодиака:Козерог")
elif (date>=21 and date<=31 and month=="Январь") or( month=="Февраль" and date>=1 and date<=18):
    print("Знак зодиака:Водолей")
elif (date>=19 and date<=29 and month=="Февраль") or( month=="Март" and date>=1 and date<=20):
    print("Знак зодиака:Рыбы")
```

## Задание №4
К следующей лекции прочитать про циклы [for](https://foxford.ru/wiki/informatika/tsikl-for-v-python) и
 [while](https://foxford.ru/wiki/informatika/tsikl-while-v-python).

---
Инструкция по выполнению домашнего задания:

1. Зарегистрируйтесь на сайте [Repl.IT](https://repl.it/).
2. Перейдите в раздел **my repls**.
3. Нажмите кнопку **Start coding now!**, если приступаете впервые, или **New Repl**, если у вас уже есть работы.
4. В списке языков выберите Python.
5. Код пишите в левой части окна.
6. Посмотреть результат выполнения файла можно, нажав на кнопку **Run**. Результат появится в правой части окна.


*Никаких файлов прикреплять не нужно.*
