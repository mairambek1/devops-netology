# Домашнее задание к занятию "8.4 Работа с Roles"

Данный плейбук предназначен для установки `Clickhouse`, `Vector` и `Lighthouse` на хосты, указанные в `inventory` файле.

## group_vars

| Переменная  | Назначение  |
|:---|:---|
| `clickhouse_version` | версия `Clickhouse` |
| `clickhouse_listen_host` | адрес, на котором будет прослушиваться `Clickhouse` |
| `vector_clickhouse_ip` | IP адрес инстанса `Clickhouse` для настройки конфига `Vector` |
| `vector_version` | версия `Vector` |
| `vector_config` | конфиг `Vector` |
| `lighthouse_nginx_user` | пользователь, из-под которого будет работать `Nginx`. Для упрощения процесса на тестовом стенде используем root пользователя|

## Inventory файл

Группа "clickhouse" состоит из 1 хоста `clickhouse-01`

Группа "vector" состоит из 1 хоста `vector-01`

Группа "vector" состоит из 1 хоста `lighthouse-01`

## Роли

Используются 3 роли:

1. clickhouse

```yaml
  - src: git@github.com:mairambek1/ansible-clickhouse.git
    scm: git
    version: "1.11.0"
    name: clickhouse
```

2. vector

```yaml
- src: git@github.com:mairambek1/vector-role.git
    scm: git
    version: "1.0.0"
    name: vector
```

3. lighthouse
   
```yaml
  - src: git@github.com:mairambek1/lighthouse-role.git
    scm: git
    version: "1.0.0"
    name: lighthouse
```

## Playbook

Playbook состоит из 3 `play`.

Play "Install Clickhouse" применяется на группу хостов "Clickhouse" и предназначен для установки и запуска `Clickhouse`

Данный `play` запускает роль `Clickhouse`

---

Play "Install Vector" применяется на группу хостов "Vector" и предназначен для установки и запуска `Vector`

Данный `play` запускает роль `Vector`

---

Play "Install lighthouse" применяется на группу хостов "lighthouse" и предназначен для установки и запуска `lighthouse`

Используется роль `Lighthouse`
Объявляем `handler` для перезапуска `Nginx`.

```yaml
 handlers:
    - name: Nginx reload
      become: true
      ansible.builtin.service:
        name: nginx
        state: restarted
```
Устанавливаем `GIT` и `NGINX`. Производим первоначальную настройку веб-сервера

| Имя pretask | Описание |
|--------------|---------|
| `Lighthouse \| Install git` | Устанавливаем `git` |
| `Lighhouse \| Install nginx` | Устанавливаем `Nginx` |
| `Lighthouse \| Apply nginx config` | Применяем конфиг `Nginx`. |

Применяем конфиг `Lighthouse` для `NGINX`

| Имя posttask | Описание |
|--------------|---------|
| `Lighthouse \| Apply config` | Применяем конфиг `Nginx` для `lighthouse`. После этого перезапускаем `nginx` для применения изменений |

## Template

Шаблон "nginx.conf.j2" используется для первичной настройки `nginx`. Мы задаем пользователя для работы `nginx` и удаляем настройки root директории по умолчанию.

Шаблон "lighthouse_nginx.conf.j2" настраивает `nginx` на работу с `lighthouse`. В нем прописываем порт 80, root директорию и index страницу.
