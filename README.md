# LXC Management Tool

## Author
Ricardo Ferreira 98441
UA DETI - AES

## Introduction
This tool allows you to manage Linux Containers (LXC) from the command line.
You can create, delete, execute commands within containers, copy files, and more. 


## Installation and Setup
1. Clone this repository.
2. Have both lxc and lxd (sudo apt install lxc lxd)
2. Watch the demo video (demo folder) for a visual walkthrough.
3. Run the tool help section as shown below

## What can be done via the command line tool
Create/Start/Stop/Delete Containers
Execute normal linux terminal in a Container
List all containers
Connect to a container and comunicate beetween containers
Set max CPU and Memory usage per container

## What isn't working at the time
Copying files from the host to the container

##
This tool works by getting command line arguments when main.py is run. 
All functions called by main are defined in either lxc_manager or utils.
These functions just use the lxc commands to do the work.

## Usage
Run the tool using Python:
```bash
python3 main.py --help
