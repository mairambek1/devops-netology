Vector
=========

This role can install and configure Vector for Clickhouse on Centos 8

Role Variables
--------------

| vars | Description | Value | Location |
|------|------------|---|---|
| vector_version | Vector version to install | 0.22.1 | defaults/main.yml |
| vector_clickhouse_ip | Addres of Clickhouse instance | localhost | defaults/main.yml |
| clickhouse_db_name | Clickhouse DB where to store logs |"logs"  | defaults/main.yml |
| clickhouse_table_name | Clickhouse table name to write logs | "data_logs" | defaults/main.yml |
| vector_url | URL for Vector download |  <https://packages.timber.io/vector/>{{ vector_version }}/vector-{{ vector_version }}-1.x86_64.rpm | vars/main.yml |
| vector_config_dir | Vector config file location | "/etc/vector" | vars/main.yml |
| vector_config | Vector config file | value below | default/main.yml |

`vector_config`

```text
  sources:
    demo_logs:
      type: demo_logs
      format: syslog
  sinks:
    to_clickhouse:
      type: clickhouse
      inputs:
        - demo_logs
      database: "{{ clickhouse_db_name }}"
      endpoint: "http://{{ vector_clickhouse_ip }}:8123"
      table: "{{ clickhouse_table_name }}"
      compression: gzip
      healthcheck: true
      skip_unknown_fields: true
```

You can replace `Vector` config with your own

Example Playbook
----------------

```yml
    - name: Install Vector
      hosts: servers
      roles:
        - vector
```

License
-------

MIT

Author Information
------------------

Nikita Kiselyov

<nkiselyov94@gmail.com>
