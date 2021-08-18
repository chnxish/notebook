# Server Configuration

  + [Folder](#folder)

  + [Software](#software)

  + [Library](#library)

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

## Software

*** 

  + debian apt update 

    - copy src/sources.list to /etc/apt/sources.list

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

  + git 

    - apt install git

  + nodejs and npm

    - curl -sL https://deb.nodesource.com/setup_14.x | bash -

    - apt install nodejs

    - install yarn
  
      - To install the Yarn package manager, run:(after nodejs installation is completed)

    - copy src/.npmrc to ~/.npmrc

    - yarn config set registry 'https://registry.npm.taobao.org'

    - update nodejs

      - open website: https://github.com/nvm-sh/nvm#installing-and-updating

      - curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash

      - source ~/.bashrc(if sources lines are added to .bashrc profile file)

      - nvm ls-remote(view node version)

      - copy to ~/.bashrc file

        - NVM_NODEJS_ORG_MIRROR=https://npm.taobao.org/dist

        - source ~/.bashrc

      - nvm install v14.17.3

    - update npm

      - npm install npm@latest -g

## Library

***

  + python

    - django

  + javascript

    - react
