# rootgit

A set of command line utilities to version the Linux root filesystem.

## Status

Planning!

## Goals:

- Grant root access to multiple administartors and track files which edited by
    them.

- Easily revert back any breaking change.
- History of server configuration for future investigations.


## How?

Using git!


The main idea is to add anything into `.gitignore` file but system
configuration files. so, the effective part of the project is it's git ignore
list.

The rest of the `rootgit` is a set of optional command-line utilities to
automatically find the sudoer's main user id and commit changes with his/her
identity. it helps people to be responsible for their changes in the server 
configuration.

## Installation

<TODO>


## Usage

The most of command-line interface is the same as the git, so you no need to 
learn anything here, just take a look!


### Setup

This command makes the root `/` directory as a git repo. (`/.git`)


```bash
rootgit init [remote-url]
```

or 

```bash
rootgit clone <remote-url>
```



