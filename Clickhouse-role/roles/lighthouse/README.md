Lighthouse
=========

This role can install and configure [Lighthouse](https://github.com/VKCOM/lighthouse.git) on Centos 8

Requirements
------------

You neeed to install and configure `git` and `NGINX` (or another web server) before run this role.

Role Variables
--------------

| vars | Description | Value | Location |
|------|------------|---|---|
| lighthouse_dir | Where to store Lighthouse files | "/home/{{ ansible_user_id }}/lighthouse" | defaults/main.yml |
| lighthouse_url | URL of Clickhouse repo | "https://github.com/VKCOM/lighthouse.git" | vars/main.yml |

Example Playbook
----------------

```yml
- name: Install lighthouse
  hosts: lighthouse
  handlers:
    - name: Nginx reload
      become: true
      ansible.builtin.service:
        name: nginx
        state: restarted
  pre_tasks:
    - name: Lighthouse | Install git
      become: true
      ansible.builtin.yum:
        name: git
        state: present
    - name: Lighhouse | Install nginx
      become: true
      ansible.builtin.yum:
        name: nginx
        state: present
    - name: Lighthouse | Apply nginx config
      become: true
      ansible.builtin.template:
        src: nginx.conf.j2
        dest: /etc/nginx/nginx.conf
        mode: 0644
  roles:
    - lighthouse
  post_tasks:
    - name: Lighthouse | Apply config
      become: true
      ansible.builtin.template:
        src: lighthouse_nginx.conf.j2
        dest: /etc/nginx/conf.d/lighthouse.conf
        mode: 0644
        notify: Nginx reload 
```

License
-------

MIT

Author Information
------------------

Nikita Kiselyov

<nkiselyov94@gmail.com>

