# Anaconda

  + [Command](#command)

  + [Configuration](#configuration)

  + [Question](#question)

## Command

***

  + Install: 
  
    - download the installation package from anaconda.com

    - bash Anaconda.sh

    - source ~/.bashrc

  + Update: conda update conda

  + Activate: conda activate website

  + Deactivate: conda deactivate

  + Remove: 

    - rm -rf ~/anaconda3

    - removeing anaconda path from ~/.bashrc

    - rm -rf ~/.condarc ~/.conda ~/.continuum

  + Create: conda create --name env_name python=3.7

  + Info: conda info

## Configuration

***

  + Mirrors

    - mirror file: ~/.condarc

```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
    
conda config --set show_channel_urls yes
```

## Question

***
