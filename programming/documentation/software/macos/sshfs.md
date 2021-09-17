# SSHFS

  + [Command](#command)

  + [Configuration](#configuration)

  + [Question](#question)

## Command

***

  + Install:

    - brew cask install osxfuse

    - brew install sshfs

    - reboot

  + Run:

    - mkdir local-file

    - sshfs root@ip:/workspace/mysite/ local-file

  + Remove: umount local-file

## Configuration

***

## Question

***

  + WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!

    - rm ~/.ssh/known_hosts
