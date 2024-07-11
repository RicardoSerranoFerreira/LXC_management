# LXC Management Tool

## Introduction
This tool allows you to manage Linux Containers (LXC) from the command line. You can create, delete, execute commands within containers, copy files, and more. It employs namespaces, chroot for filesystem isolation, and cgroups for resource management.

## Installation and Setup
1. Clone this repository.
2. Run the setup script to install dependencies and set up the environment.
    ```bash
    ./setup.sh
    ```
3. Follow the instructions in `documentation.md` for detailed usage and examples.
4. Watch the demo video (`demo/demo_video.mp4`) for a visual walkthrough.

## Usage
Run the tool using Python:
```bash
python3 main.py --help