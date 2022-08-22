#!/usr/bin/env python3
import socket
import time
# Нулевые значения
service_addr = {
    'drive.google.com': '0',
    'mail.google.com': '0',
    'google.com': '0'
}

# Получаем текущие на момент запуска скрипта значения (необходимо для последующего сравнения).
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
            print("[ERROR] "+item+" IP mismatch: old IP "+old_addr+", new IP "+new_addr)
        print(item + " - " + service_addr[item])
    print("######################################")
    time.sleep(10)

