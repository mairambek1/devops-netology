# Домашнее задание к занятию "4.2. Использование Python для решения типовых DevOps задач"

## Обязательная задача 1

Есть скрипт:
```python
#!/usr/bin/env python3
a = 1
b = '2'
c = a + b
```

### Вопросы:
| Вопрос  | Ответ |
| ------------- | ------------- |
| Какое значение будет присвоено переменной `c`?  | будет ошибка, типы не соответсвуют для операции , int и str  |
| Как получить для переменной `c` значение 12?  | c = str(a) + b |
| Как получить для переменной `c` значение 3?  | a + int(b) |

## Обязательная задача 2
Мы устроились на работу в компанию, где раньше уже был DevOps Engineer. Он написал скрипт, позволяющий узнать, какие файлы модифицированы в репозитории, относительно локальных изменений. Этим скриптом недовольно начальство, потому что в его выводе есть не все изменённые файлы, а также непонятен полный путь к директории, где они находятся. Как можно доработать скрипт ниже, чтобы он исполнял требования вашего руководителя?

```python
#!/usr/bin/env python3

import os

bash_command = ["cd ~/netology/sysadm-homeworks", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
is_change = False
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(prepare_result)
        break
```

### Ваш скрипт:
```python
#!/usr/bin/env python3

import os
import sys

path = "./"
if len(sys.argv) >= 2:
    path = sys.argv[1]
    if not os.path.isdir(path):
          sys.exit("Directory doesn't exist: " + path)

bash_command = ["cd " + path, "git status 2>&1"]
git_command = ["git rev-parse --show-toplevel"]

result_os = os.popen(' && '.join(bash_command)).read()
if result_os.find('not a git') != -1:
    sys.exit("not a git repository: " + path)

git_top_level = (os.popen(' && '.join(git_command)).read()).replace('\n', '/')

for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(git_top_level + prepare_result)
```

### Вывод скрипта при запуске при тестировании:
```
devops@devops:~/devops-netology$ sudo ./test2.py
/home/devops/devops-netology/homwork_horoscope.py
/home/devops/devops-netology/04-script-02-py/README.md
/home/devops/devops-netology/test2.txt
```

## Обязательная задача 3
Доработать скрипт выше так, чтобы он мог проверять не только локальный репозиторий в текущей директории, а также умел воспринимать путь к репозиторию, который мы передаём как входной параметр. Мы точно знаем, что начальство коварное и будет проверять работу этого скрипта в директориях, которые не являются локальными репозиториями.

### Ваш скрипт
```python
#!/usr/bin/env python3

import os

bash_command = ["cd ~/devops-netology", "pwd", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
#is_change = False
cwd=result_os.split('\n')
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = cwd[0]+'/'+result.replace('\tmodified:   ', '')
        print(prepare_result)
        #break
```
### Вывод скрипта при запуске при тестировании:
```
devops@devops:~$ sudo ./test7.py
/root/devops-netology/test.txt
/root/devops-netology/test2.txt
```

## Обязательная задача 4
1. Наша команда разрабатывает несколько веб-сервисов, доступных по http. Мы точно знаем, что на их стенде нет никакой балансировки, кластеризации, за DNS прячется конкретный IP сервера, где установлен сервис. Проблема в том, что отдел, занимающийся нашей инфраструктурой очень часто меняет нам сервера, поэтому IP меняются примерно раз в неделю, при этом сервисы сохраняют за собой DNS имена. Это бы совсем никого не беспокоило, если бы несколько раз сервера не уезжали в такой сегмент сети нашей компании, который недоступен для разработчиков. Мы хотим написать скрипт, который опрашивает веб-сервисы, получает их IP, выводит информацию в стандартный вывод в виде: <URL сервиса> - <его IP>. Также, должна быть реализована возможность проверки текущего IP сервиса c его IP из предыдущей проверки. Если проверка будет провалена - оповестить об этом в стандартный вывод сообщением: [ERROR] <URL сервиса> IP mismatch: <старый IP> <Новый IP>. Будем считать, что наша разработка реализовала сервисы: `drive.google.com`, `mail.google.com`, `google.com`.

### Ваш скрипт:
```python
#!/usr/bin/env python3
import socket
import time
service_addr = {
‘drive.google.com’: ‘0’,
‘mail.google.com’: ‘0’,
‘google.com’: ‘0’
}
#Вывод скрипта при запуске при тестировании:

for item in service_addr:
initial_addr = socket.gethostbyname(item)
service_addr[item] = initial_addr

while True:
# Перебираем все ключи в словаре
for item in service_addr:
old_addr = service_addr[item]
new_addr = socket.gethostbyname(item)
# Если старое и новое не совпадают - адрес изменился. Перезаписываем значение в словаре и выводим ошибку
if new_addr != old_addr:
service_addr[item] = new_addr
print("[ERROR] “+item+” IP mismatch: old IP “+old_addr+”, new IP “+new_addr)
print(item + " - " + service_addr[item])
print(”######################################")
time.sleep(10)
``` 
### Вывод скрипта при запуске при тестировании:
```
root@devops:~# ./test.py
[ERROR] drive.google.com IP mismatch: old IP 74.125.131.138, new IP 74.125.131.102
drive.google.com - 74.125.131.102
[ERROR] mail.google.com IP mismatch: old IP 173.194.220.18, new IP 173.194.220.83
mail.google.com - 173.194.220.83
[ERROR] google.com IP mismatch: old IP 173.194.221.138, new IP 173.194.221.102
google.com - 173.194.221.102
######################################
[ERROR] drive.google.com IP mismatch: old IP 74.125.131.102, new IP 74.125.131.138
drive.google.com - 74.125.131.138
[ERROR] mail.google.com IP mismatch: old IP 173.194.220.83, new IP 173.194.220.18
mail.google.com - 173.194.220.18
[ERROR] google.com IP mismatch: old IP 173.194.221.102, new IP 173.194.221.100
google.com - 173.194.221.100
######################################
[ERROR] drive.google.com IP mismatch: old IP 74.125.131.138, new IP 74.125.131.113
drive.google.com - 74.125.131.113
[ERROR] mail.google.com IP mismatch: old IP 173.194.220.18, new IP 173.194.220.83
mail.google.com - 173.194.220.83
[ERROR] google.com IP mismatch: old IP 173.194.221.100, new IP 173.194.221.101
google.com - 173.194.221.101
######################################
[ERROR] drive.google.com IP mismatch: old IP 74.125.131.113, new IP 74.125.131.102
drive.google.com - 74.125.131.102
[ERROR] mail.google.com IP mismatch: old IP 173.194.220.83, new IP 173.194.220.19
mail.google.com - 173.194.220.19
[ERROR] google.com IP mismatch: old IP 173.194.221.101, new IP 173.194.221.102
google.com - 173.194.221.102
######################################
[ERROR] drive.google.com IP mismatch: old IP 74.125.131.102, new IP 74.125.131.101
drive.google.com - 74.125.131.101
[ERROR] mail.google.com IP mismatch: old IP 173.194.220.19, new IP 173.194.220.17
mail.google.com - 173.194.220.17
[ERROR] google.com IP mismatch: old IP 173.194.221.102, new IP 173.194.222.100
google.com - 173.194.222.100
######################################
```
