import subprocess
import os


def create_container(container_name):
    try:
        subprocess.run(
            ['lxc-create', '-n', container_name, '-t', 'download', '--', '--dist', 'ubuntu', '--release', 'focal',
             '--arch', 'amd64'], check=True)
        print(f"Container {container_name} created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to create container {container_name}: {e}")


def delete_container(container_name):
    try:
        subprocess.run(['lxc-destroy', '-n', container_name], check=True)
        print(f"Container {container_name} deleted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to delete container {container_name}: {e}")


def execute_command(container_name, command):
    try:
        result = subprocess.run(['lxc-attach', '-n', container_name, '--', 'bash', '-c', command], capture_output=True,
                                text=True, check=True)
        print(f"Command output:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute command in {container_name}: {e.stderr}")


def copy_to_container(container_name, source, destination):
    try:
        subprocess.run(['lxc-file', 'push', source, f"{container_name}/{destination}"], check=True)
        print(f"Copied {source} to {container_name}:{destination} successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to copy {source} to {container_name}:{destination}: {e}")


def start_container(container_name):
    try:
        subprocess.run(['lxc-start', '-n', container_name], check=True)
        print(f"Container {container_name} started successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to start container {container_name}: {e}")


def stop_container(container_name):
    try:
        subprocess.run(['lxc-stop', '-n', container_name], check=True)
        print(f"Container {container_name} stopped successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to stop container {container_name}: {e}")


def connect_to_container(container_name):
    try:
        subprocess.run(['lxc-console', '-n', container_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to connect to container {container_name}: {e}")


def run_application(container_name, application):
    execute_command(container_name, application)


def set_resource_limits(container_name, cpu_limit=None, memory_limit=None):
    if cpu_limit:
        try:
            subprocess.run(['lxc-cgroup', '-n', container_name, 'cpuset.cpus', cpu_limit], check=True)
            print(f"Set CPU limit for {container_name} to {cpu_limit}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to set CPU limit for {container_name}: {e}")

    if memory_limit:
        try:
            subprocess.run(['lxc-cgroup', '-n', container_name, 'memory.limit_in_bytes', memory_limit], check=True)
            print(f"Set memory limit for {container_name} to {memory_limit}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to set memory limit for {container_name}: {e}")
