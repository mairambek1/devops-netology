#!/usr/bin/env python3
height = int(input('Укажите ваш рост:'))
age = int(input('Укажите ваш возраст:'))
children = int(input('Количество детей:'))
student = input('Являетесь ли Вы студентом? ')
if student == 'Да':
    print('Вам нельзя служить')
else:
    if 18 < age < 27:
        if height < 170:
            print('В танкисты')
        elif height < 180:
            print('На флот')
        elif height < 200:
            print('Десантники')
        else:
            print('В другие войска')
    else:
        print('Непризывной возраст')
    if children > 0:
        print(f'Кол-во детей {children}')
    print('Армия ждет Вас')
