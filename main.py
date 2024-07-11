#### 2.2. `main.py`

import argparse
from src import lxc_manager, utils


def main():
    parser = argparse.ArgumentParser(description='LXC Management Tool')
    parser.add_argument('--create', metavar='NAME', type=str, help='Create a new container')
    parser.add_argument('--delete', metavar='NAME', type=str, help='Delete an existing container')
    parser.add_argument('--exec', nargs=2, metavar=('NAME', 'CMD'), help='Execute command in container')
    parser.add_argument('--copy', nargs=3, metavar=('NAME', 'SRC', 'DEST'), help='Copy file to container')
    parser.add_argument('--start', metavar='NAME', type=str, help='Start a container')
    parser.add_argument('--stop', metavar='NAME', type=str, help='Stop a container')
    parser.add_argument('--connect', metavar='NAME', type=str, help='Connect to container')
    parser.add_argument('--run', nargs=2, metavar=('NAME', 'APP'), help='Run application in container')
    parser.add_argument('--set-limits', nargs=3, metavar=('NAME', 'CPU', 'MEMORY'),help='Set resource limits for container')
    parser.add_argument('--get-limits', metavar='NAME', type=str,help='Get CPU and Memory Limits')
    parser.add_argument('--list', action='store_true', help='List all containers and their states')

    args = parser.parse_args()

    if args.create:
        lxc_manager.create_container(args.create)
    elif args.delete:
        lxc_manager.delete_container(args.delete)
    elif args.exec:
        lxc_manager.execute_command(args.exec[0], args.exec[1])
    elif args.copy:
        lxc_manager.copy_to_container(args.copy[0], args.copy[1], args.copy[2])
    elif args.start:
        lxc_manager.start_container(args.start)
    elif args.stop:
        lxc_manager.stop_container(args.stop)
    elif args.connect:
        lxc_manager.connect_to_container(args.connect)
    elif args.run:
        lxc_manager.run_application(args.run[0], args.run[1])
    elif args.set_limits:
        utils.set_resource_limits(args.set_limits[0], args.set_limits[1], args.set_limits[2])
    elif args.get_limits:
        utils.get_resource_limits(args.get_limits)
    elif args.list:
        lxc_manager.list_containers()


if __name__ == '__main__':
    main()
