# Домашнее задание к занятию "3. Использование Yandex Cloud"

## Подготовка к выполнению
1. Подготовьте в Yandex Cloud три хоста: для clickhouse, для vector и для lighthouse.
Ссылка на репозиторий LightHouse: https://github.com/VKCOM/lighthouse

## Основная часть
1. Допишите playbook: нужно сделать ещё один play, который устанавливает и настраивает lighthouse.
2. При создании tasks рекомендую использовать модули: get_url, template, yum, apt.
3. Tasks должны: скачать статику lighthouse, установить nginx или любой другой webserver, настроить его конфиг для открытия lighthouse, запустить webserver.
4. Приготовьте свой собственный inventory файл prod.yml.
5. Запустите `ansible-lint site.yml` и исправьте ошибки, если они есть.
6. Попробуйте запустить playbook на этом окружении с флагом `--check`.
7. Запустите playbook на `prod.yml` окружении с флагом `--diff`. Убедитесь, что изменения на системе произведены.

```
[root@server1 playbook]# ansible-playbook -i inventory/prod.yml site.yml --diff

PLAY [Install Clickhouse] *******************************************************************************************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************************************************************************************************
ok: [clickhouse-01]

TASK [Clickhouse | Get clickhouse distrib] **************************************************************************************************************************************************************************************************
ok: [clickhouse-01] => (item=clickhouse-client)
ok: [clickhouse-01] => (item=clickhouse-server)
ok: [clickhouse-01] (item=clickhouse-common-static)

TASK [Clickhouse | Get clickhouse distrib] **************************************************************************************************************************************************************************************************
ok: [clickhouse-01]

TASK [Clickhouse | Install clickhouse packages] *********************************************************************************************************************************************************************************************
ok: [clickhouse-01]

TASK [Clickhouse | Create database] *********************************************************************************************************************************************************************************************************
ok: [clickhouse-01]

PLAY [Install Vector] ***********************************************************************************************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************************************************************************************************
ok: [vector-01]

TASK [Vector | Download packages] ***********************************************************************************************************************************************************************************************************
ok: [vector-01]

TASK [Vector | Install packages] ************************************************************************************************************************************************************************************************************
ok: [vector-01]

TASK [Vector | Apply template] **************************************************************************************************************************************************************************************************************
ok: [vector-01]

TASK [Vector | change systemd unit] *********************************************************************************************************************************************************************************************************
ok: [vector-01]

PLAY [Install lighthouse] *******************************************************************************************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************************************************************************************************
ok: [lighthouse-01]

TASK [Lighthouse | Install git] *************************************************************************************************************************************************************************************************************
ok: [lighthouse-01]

TASK [Lighhouse | Install nginx] ************************************************************************************************************************************************************************************************************
ok: [lighthouse-01]
PLAY RECAP **********************************************************************************************************************************************************************************************************************************
clickhouse-01              : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=1    ignored=0
lighthouse-01              : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
vector-01                  : ok=5    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

```

8. Повторно запустите playbook с флагом `--diff` и убедитесь, что playbook идемпотентен.
9. Подготовьте README.md файл по своему playbook. В нём должно быть описано: что делает playbook, какие у него есть параметры и теги.
10. Готовый playbook выложите в свой репозиторий, поставьте тег 08-ansible-03-yandex на фиксирующий коммит, в ответ предоставьте ссылку на него.

Ответ:

[08-ansible-03-yandex](https://github.com/mairambek1/devops-netology/tree/main/08-ansible-03-yandex/playbook).

---
---

### Как оформить ДЗ?

Выполненное домашнее задание пришлите ссылкой на .md-файл в вашем репозитории.

---