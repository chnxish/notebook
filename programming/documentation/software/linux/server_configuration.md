# Server Configuration

## Folder

***

```
/workspace
/bash
/c
/cc
/javascript
    /react_chnxish
/python
    /chnxish
    /api
    /chnxish
    /innovation_studio
    /testtest
    /media
    /static
        /css
        /image
        /js
    /templates
        /web_page_name
/download
```

## Install

*** 

  + debian apt update 

    - apt update 

    - apt upgrade

  + gcc/g++

    - apt install build-essential

    - version management command

      - update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.8 20

      - update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.8 20

  + vim

    - apt install vim

    - copy src/.vimrc to ~/.vimrc

  + tree

    - apt install tree

  + make

    - apt install make (included in build-essential)

  + python3

    - python3.7.3
  
      - debian10 has python3.7.3 installed

    - python3.7.5

      - wget https://www.python.org/ftp/python/3.7.5/Python-3.7.5.tar.xz

      - tar -xvf Python-3.7.5.tar.xz

      - cd Python-3.7.5

      - ./conigure --enable-shared --enable-optimizations 

      - make && make install

      - apt install python3-dev

    - setuptools

      - wget https://files.pythonhosted.org/packages/94/23/e9e3d96500c063129a19feb854efbb01e6ffe7d913f1da8176692418ab8e/setuptools-51.1.1.tar.gz

      - tar -xvf setuptools-51.1.1.tar.gz

      - cd setuptools-51.1.1/

      - python3 setup.py install

    - pip 

      - wget https://files.pythonhosted.org/packages/b7/2d/ad02de84a4c9fd3b1958dc9fb72764de1aa2605a9d7e943837be6ad82337/pip-21.0.1.tar.gz

      - tar -xvf pip-21.0.1.tar.gz

      - cd pip-21.0.1/

      - python3 setup.py install

      - copy pip.conf to ~/.pip/pip.conf

  + apache

    - apt install apache2

    - apt install apache2-dev

    - execute enable command and start command

  + mod_wsgi

    - apt install libapache2-mod-wsgi-py3

  + mysql

    - wget https://downloads.mysql.com/archives/get/p/23/file/mysql-server_8.0.21-1debian10_amd64.deb-bundle.tar (for debian10)

    - tar -xvf mysql-server_8.0.21-1debian10_amd64.deb-budle.tar

    - mkdir mysql-8.0.21

    - mv *.deb mysql-8.0.21

    - cd mysql-8.0.21

    - dpkg -i package_name

```
for mysql-server_8.0.21-1debian10_amd64.deb
    for mysql-community-server_8.0.21-1debian10_amd64.deb
    for mysql-client_8.0.21-1debian10_amd64.deb
        for mysql-community-client_8.0.21-1debian10_amd64.deb
        for mysql-common_8.0.21-1debian10_amd64.deb
            for mysql-community-client-core_8.0.21-1debian10_amd64.deb
    for mysql-community-server-core_8.0.21-1debian10_amd64.deb
        for libmecab2(apt install)
        for libnuma1(apt install)
        apt --fix-broken install(in fact, only need)
    for psmisc(apt install)
```
