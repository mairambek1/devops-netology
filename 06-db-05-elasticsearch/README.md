# Домашнее задание к занятию "6.5. Elasticsearch"

## Задача 1

В этом задании вы потренируетесь в:
- установке elasticsearch
- первоначальном конфигурировании elastcisearch
- запуске elasticsearch в docker

Используя докер образ [elasticsearch:7](https://hub.docker.com/_/elasticsearch) как базовый:

- составьте Dockerfile-манифест для elasticsearch
- соберите docker-образ и сделайте `push` в ваш docker.io репозиторий
- запустите контейнер из получившегося образа и выполните запрос пути `/` c хост-машины

Требования к `elasticsearch.yml`:
- данные `path` должны сохраняться в `/var/lib` 
- имя ноды должно быть `netology_test`

В ответе приведите:
- текст Dockerfile манифеста
Ответ:
```
FROM centos:centos7

RUN yum -y install wget; yum clean all && \
        groupadd --gid 1000 elasticsearch && \
        adduser --uid 1000 --gid 1000 --home /usr/share/elasticsearch elasticsearch && \
        mkdir /var/lib/elasticsearch/ && \
        chown -R 1000:1000 /var/lib/elasticsearch/

USER 1000:1000

WORKDIR /usr/share/elasticsearch

ENV EL_VER=8.0.1

RUN wget -q https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-${EL_VER}-linux-x86_64.tar.gz && \
        tar -xzf elasticsearch-${EL_VER}-linux-x86_64.tar.gz && \
        cp -rp elasticsearch-${EL_VER}/* ./ && \
        rm -rf elasticsearch-${EL_VER}*

COPY ./config/elasticsearch.yml /usr/share/elasticsearch/config/

EXPOSE 9200

CMD ["bin/elasticsearch"]
```
- ссылку на образ в репозитории dockerhub
Ответ:
```
https://hub.docker.com/r/momukeev/test-docker
```

- ответ `elasticsearch` на запрос пути `/` в json виде:
```
[root@70abd1df8029 /]# curl -X GET "localhost:9200/?pretty"
{
  "name" : "70abd1df8029",
  "cluster_name" : "netology_test",
  "cluster_uuid" : "XocEXjlVSqyk66tdnkuCEQ",
  "version" : {
    "number" : "7.11.1",
    "build_flavor" : "default",
    "build_type" : "tar",
    "build_hash" : "ff17057114c2199c9c1bbecc727003a907c0db7a",
    "build_date" : "2021-02-15T13:44:09.394032Z",
    "build_snapshot" : false,
    "lucene_version" : "8.7.0",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
```

Подсказки:
- при сетевых проблемах внимательно изучите кластерные и сетевые настройки в elasticsearch.yml
- при некоторых проблемах вам поможет docker директива ulimit
- elasticsearch в логах обычно описывает проблему и пути ее решения
- обратите внимание на настройки безопасности такие как `xpack.security.enabled` 
- если докер образ не запускается и падает с ошибкой 137 в этом случае может помочь настройка `-e ES_HEAP_SIZE`
- при настройке `path` возможно потребуется настройка прав доступа на директорию

Далее мы будем работать с данным экземпляром elasticsearch.

## Задача 2

В этом задании вы научитесь:
- создавать и удалять индексы
- изучать состояние кластера
- обосновывать причину деградации доступности данных

Ознакомтесь с [документацией](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-create-index.html) 
и добавьте в `elasticsearch` 3 индекса, в соответствии со таблицей:

| Имя | Количество реплик | Количество шард |
|-----|-------------------|-----------------|
| ind-1| 0 | 1 |
| ind-2 | 1 | 2 |
| ind-3 | 2 | 4 |

Ответ:
```
[root@70abd1df8029 /]# curl -X PUT "localhost:9200/ind-1?pretty" -H 'Content-Type: application/json' -d'
{
>   "settings": {
>     "number_of_shards": 1,
>     "number_of_replicas": 0
>   }
> }

```
```
[root@70abd1df8029 /]# curl -X PUT "localhost:9200/ind-2?pretty" -H 'Content-Type: application/json' -d'
> {
>   "settings": {
>     "number_of_shards": 2,
>     "number_of_replicas": 1
>   }
> }

```
```
[root@70abd1df8029 /]# curl -X PUT "localhost:9200/ind-3?pretty" -H 'Content-Type: application/json' -d'
> {
>   "settings": {
>     "number_of_shards": 4,
>     "number_of_replicas": 2
>   }
> }
> '

```

Получите список индексов и их статусов, используя API и **приведите в ответе** на задание.

```
[root@70abd1df8029 /]# curl -X GET -u undefined:$ESPASS "localhost:9200/_cat/indices/ind-*?v=true&s=index&pretty"
health status index uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   ind-1 lN7XX6Y5R96ha0FD7v6Qzw   1   0          0            0       208b           208b
yellow open   ind-2 rIX2NxYKSEmF5W8PMzeH3A   2   1          0            0       416b           416b
yellow open   ind-3 AtuAVxBFQBKFoljj08eRTg   4   2          0            0       832b           832b
```

Получите состояние кластера `elasticsearch`, используя API.

```
[root@70abd1df8029 /]# curl -X GET -u undefined:$ESPASS "localhost:9200/_cluster/health?pretty"
{
  "cluster_name" : "netology_test",
  "status" : "yellow",
  "timed_out" : false,
  "number_of_nodes" : 1,
  "number_of_data_nodes" : 1,
  "active_primary_shards" : 7,
  "active_shards" : 7,
  "relocating_shards" : 0,
  "initializing_shards" : 0,
  "unassigned_shards" : 10,
  "delayed_unassigned_shards" : 0,
  "number_of_pending_tasks" : 0,
  "number_of_in_flight_fetch" : 0,
  "task_max_waiting_in_queue_millis" : 0,
  "active_shards_percent_as_number" : 41.17647058823529
}
```

Как вы думаете, почему часть индексов и кластер находится в состоянии yellow?
Состояние yellow по кластеру связано с тем, что есть unassigned шарды.

Удалите все индексы.

Ответ:
```
[root@70abd1df8029 /]#  curl -X DELETE 'http://127.0.0.1:9200/ind-1'
{"acknowledged":true}
[root@70abd1df8029 /]# curl -X DELETE 'http://127.0.0.1:9200/ind-2'
{"acknowledged":true}
[root@70abd1df8029 /]# curl -X DELETE 'http://127.0.0.1:9200/ind-3'
{"acknowledged":true}
```

**Важно**

При проектировании кластера elasticsearch нужно корректно рассчитывать количество реплик и шард,
иначе возможна потеря данных индексов, вплоть до полной, при деградации системы.

## Задача 3

В данном задании вы научитесь:
- создавать бэкапы данных
- восстанавливать индексы из бэкапов

Создайте директорию `{путь до корневой директории с elasticsearch в образе}/snapshots`.

Используя API [зарегистрируйте](https://www.elastic.co/guide/en/elasticsearch/reference/current/snapshots-register-repository.html#snapshots-register-repository) 
данную директорию как `snapshot repository` c именем `netology_backup`.

Ответ:
```
[root@70abd1df8029 /]# curl -XPOST localhost:9200/_snapshot/netology_backup?pretty -H 'Content-Type: application/json' -d'{"type": "fs", "settings": { "location":"myrepo" }}'
{
  "acknowledged" : true
}
```

**Приведите в ответе** запрос API и результат вызова API для создания репозитория.

Ответ:
```
[root@70abd1df8029 /]# curl -X GET 'http://localhost:9200/_snapshot/netology_backup?pretty'
{
  "netology_backup" : {
    "type" : "fs",
    "settings" : {
      "location" : "myrepo"
    }
  }
}
```

Создайте индекс `test` с 0 реплик и 1 шардом и **приведите в ответе** список индексов.

Ответ:
```
[root@70abd1df8029 /]# curl -X PUT localhost:9200/test -H 'Content-Type: application/json' -d'{ "settings": { "number_of_shards": 1,  "number_of_replicas": 0 }}'
{"acknowledged":true,"shards_acknowledged":true,"index":"test"}
[root@70abd1df8029 /]# curl -X GET 'http://localhost:9200/test?pretty'
{
  "test" : {
    "aliases" : { },
    "mappings" : { },
    "settings" : {
      "index" : {
        "routing" : {
          "allocation" : {
            "include" : {
              "_tier_preference" : "data_content"
            }
          }
        },
        "number_of_shards" : "1",
        "provided_name" : "test",
        "creation_date" : "1667204277202",
        "number_of_replicas" : "0",
        "uuid" : "vdouR7MbT_OA5H6j0JfkIw",
        "version" : {
          "created" : "7110199"
        }
      }
    }
  }
}
[root@70abd1df8029 /]#

```

[Создайте `snapshot`](https://www.elastic.co/guide/en/elasticsearch/reference/current/snapshots-take-snapshot.html) 
состояния кластера `elasticsearch`.

Ответ:
```
[root@70abd1df8029 /]# curl -X PUT localhost:9200/_snapshot/netology_backup/elasticsearch?wait_for_completion=true
{"snapshot":{"snapshot":"elasticsearch","uuid":"X3yRu8yXRVyyHF1gLWFSNA","version_id":7110199,"version":"7.11.1","indices":["test"],"data_streams":[],"include_global_state":true,"state":"SUCCESS","start_time":"2022-10-31T08:20:29.185Z","start_time_in_millis":1667204429185,"end_time":"2022-10-31T08:20:29.385Z","end_time_in_millis":1667204429385,"duration_in_millis":200,"failures":[],"shards":{"total":1,"failed":0,"successful":1}}}
```

**Приведите в ответе** список файлов в директории со `snapshot`ами.

Ответ:
```
[root@70abd1df8029 myrepo]# ls -la
total 56
drwxr-xr-x 3 elasticsearch elasticsearch  4096 Oct 31 08:20 .
drwxr-xr-x 1 elasticsearch elasticsearch  4096 Oct 31 08:07 ..
-rw-r--r-- 1 elasticsearch elasticsearch   437 Oct 31 08:20 index-0
-rw-r--r-- 1 elasticsearch elasticsearch     8 Oct 31 08:20 index.latest
drwxr-xr-x 3 elasticsearch elasticsearch  4096 Oct 31 08:20 indices
-rw-r--r-- 1 elasticsearch elasticsearch 31037 Oct 31 08:20 meta-X3yRu8yXRVyyHF1gLWFSNA.dat
-rw-r--r-- 1 elasticsearch elasticsearch   269 Oct 31 08:20 snap-X3yRu8yXRVyyHF1gLWFSNA.dat
```



Удалите индекс `test` и создайте индекс `test-2`. **Приведите в ответе** список индексов.

Ответ:
```
[root@70abd1df8029 ~]# curl -X DELETE 'http://localhost:9200/test?pretty'
{
  "acknowledged" : true
}
[root@70abd1df8029 ~]# curl -X PUT localhost:9200/test-2?pretty -H 'Content-Type: application/json' -d'{ "settings": { "number_of_shards": 1,  "number_of_replicas": 0 }}'
{
  "acknowledged" : true,
  "shards_acknowledged" : true,
  "index" : "test-2"
}
[root@70abd1df8029 ~]#
```

[Восстановите](https://www.elastic.co/guide/en/elasticsearch/reference/current/snapshots-restore-snapshot.html) состояние
кластера `elasticsearch` из `snapshot`, созданного ранее. 

Ответ:
```
[root@70abd1df8029 ~]# curl -X POST localhost:9200/_snapshot/netology_backup/elasticsearch/_restore?pretty -H 'Content-Type: application/json' -d'{"include_global_state":true}'
{
  "accepted" : true
}
[root@70abd1df8029 ~]#
```

**Приведите в ответе** запрос к API восстановления и итоговый список индексов.

Ответ:
```
[root@70abd1df8029 ~]# curl -X GET http://localhost:9200/_cat/indices?v
health status index  uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   test-2 zpVvJsi-SLCv3i2EHiKLxQ   1   0          0            0       208b           208b
green  open   test   Zf_MX4HbRX6ZfEKyvXaqMw   1   0          0            0       208b           208b
[root@70abd1df8029 ~]#

```

Подсказки:
- возможно вам понадобится доработать `elasticsearch.yml` в части директивы `path.repo` и перезапустить `elasticsearch`

---

### Как cдавать задание

Выполненное домашнее задание пришлите ссылкой на .md-файл в вашем репозитории.

---
