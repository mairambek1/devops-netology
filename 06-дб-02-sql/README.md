# Домашнее задание к занятию "6.2. SQL"
## Задача 1

Используя docker поднимите инстанс PostgreSQL (версию 12) c 2 volume, 
в который будут складываться данные БД и бэкапы.

Приведите получившуюся команду или docker-compose манифест.

root@server1:~# docker pull postgres:12

root@server1:~# docker volume create vol2

root@server1:~# docker volume create vol1

root@server1:~# docker run --rm --name pg-docker -e POSTGRES_PASSWORD=postgres -ti -p 5432:5432 -v vol1:/var/lib/postgresql/data -v vol2:/var/lib/postgresql postgres:12

# Ответ:
![img.png](SQL1.png)

## Задача 2

В БД из задачи 1: 
- создайте пользователя test-admin-user и БД test_db
- в БД test_db создайте таблицу orders и clients (спeцификация таблиц ниже)
- предоставьте привилегии на все операции пользователю test-admin-user на таблицы БД test_db
- создайте пользователя test-simple-user  
- предоставьте пользователю test-simple-user права на SELECT/INSERT/UPDATE/DELETE данных таблиц БД test_db

Таблица orders:
- id (serial primary key)
- наименование (string)
- цена (integer)

Таблица clients:
- id (serial primary key)
- фамилия (string)
- страна проживания (string, index)
- заказ (foreign key orders)

Приведите:
- итоговый список БД после выполнения пунктов выше,
- описание таблиц (describe)
- SQL-запрос для выдачи списка пользователей с правами над таблицами test_db
- список пользователей с правами над таблицами test_db

# Ответ:

CREATE DATABASE test_db

CREATE ROLE "test-admin-user" SUPERUSER NOCREATEDB NOCREATEROLE NOINHERIT LOGIN;

CREATE TABLE orders 

(

id integer, 

name text, 

price integer, 

PRIMARY KEY (id) 

);


CREATE TABLE clients 

(

        id integer PRIMARY KEY,
	
	lastname text,
	
	country text,
	
	booking integer,
	
	FOREIGN KEY (booking) REFERENCES orders (Id)

);


CREATE ROLE "test-simple-user" NOSUPERUSER NOCREATEDB NOCREATEROLE NOINHERIT LOGIN;

GRANT SELECT ON TABLE public.clients TO "test-simple-user";

GRANT INSERT ON TABLE public.clients TO "test-simple-user";

GRANT UPDATE ON TABLE public.clients TO "test-simple-user";

GRANT DELETE ON TABLE public.clients TO "test-simple-user";

GRANT SELECT ON TABLE public.orders TO "test-simple-user";

GRANT INSERT ON TABLE public.orders TO "test-simple-user";

GRANT UPDATE ON TABLE public.orders TO "test-simple-user";

GRANT DELETE ON TABLE public.orders TO "test-simple-user";

![img.png](SQL3.png)
![img.png](SQL4.png)

## Задача 3

Используя SQL синтаксис - наполните таблицы следующими тестовыми данными:

Таблица orders

|Наименование|цена|
|------------|----|
|Шоколад| 10 |
|Принтер| 3000 |
|Книга| 500 |
|Монитор| 7000|
|Гитара| 4000|

Таблица clients

|ФИО|Страна проживания|
|------------|----|
|Иванов Иван Иванович| USA |
|Петров Петр Петрович| Canada |
|Иоганн Себастьян Бах| Japan |
|Ронни Джеймс Дио| Russia|
|Ritchie Blackmore| Russia|

Используя SQL синтаксис:
- вычислите количество записей для каждой таблицы 
- приведите в ответе:
    - запросы 
    - результаты их выполнения.
    
# Ответ:

insert into orders VALUES (1, 'Шоколад', 10), (2, 'Принтер', 3000), (3, 'Книга', 500), (4, 'Монитор', 7000), (5, 'Гитара', 4000);

insert into clients VALUES (1, 'Иванов Иван Иванович', 'USA'), (2, 'Петров Петр Петрович', 'Canada'), (3, 'Иоганн Себастьян Бах', 'Japan'), (4, 'Ронни Джеймс Дио', 'Russia'), (5, 'Ritchie Blackmore', 'Russia');

select count (*) from orders;

select count (*) from clients;


![img.png](SQL5.png)  

## Задача 4

Часть пользователей из таблицы clients решили оформить заказы из таблицы orders.

Используя foreign keys свяжите записи из таблиц, согласно таблице:

|ФИО|Заказ|
|------------|----|
|Иванов Иван Иванович| Книга |
|Петров Петр Петрович| Монитор |
|Иоганн Себастьян Бах| Гитара |

Приведите SQL-запросы для выполнения данных операций.

Приведите SQL-запрос для выдачи всех пользователей, которые совершили заказ, а также вывод данного запроса.
 
Подсказк - используйте директиву `UPDATE`.

# Ответ:

update  clients set booking = 3 where id = 1;

update  clients set booking = 4 where id = 2;

update  clients set booking = 5 where id = 3;

select * from clients as c where  exists (select id from orders as o where c.booking = o.id) ;

select * from clients where booking is not null


![img.png](SQL6.png)

## Задача 5

Получите полную информацию по выполнению запроса выдачи всех пользователей из задачи 4 
(используя директиву EXPLAIN).

Приведите получившийся результат и объясните что значат полученные значения.

![img.png](SQL7.png)

cost - стоимость операции

row - ожидаемое число строк

width - средняя ширина строки в байтах

## Задача 6

Создайте бэкап БД test_db и поместите его в volume, предназначенный для бэкапов (см. Задачу 1).

Остановите контейнер с PostgreSQL (но не удаляйте volumes).

Поднимите новый пустой контейнер с PostgreSQL.

Восстановите БД test_db в новом контейнере.

Приведите список операций, который вы применяли для бэкапа данных и восстановления. 

создаем дамп базы данных текстовом формате

pg_dump -U postgres test_db > /tmp/dump_test.sql

останавливаем контейнер

запускаем новый контейнер и востаналивем данные 

psql -U postgres test_db -f /tmp/dump_test.sql

![img.png](SQL8.png)
