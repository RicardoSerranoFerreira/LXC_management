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
        # Construct the command for copying files into the container
        command = ['sudo', 'lxc', 'file', 'push', source, f"{container_name}/{destination}/"]

        # Execute the command and capture the output
        result = subprocess.run(command, capture_output=True, text=True, check=True)

        # Print success message if the command succeeds
        print(f"Copied {source} to {container_name}:{destination} successfully.")

        # Print the command output if needed
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        # Print error message if the command fails
        print(f"Failed to copy {source} to {container_name}:{destination}: {e}")
        # Print the error output for debugging
        print(e.stderr)


# Example usage:
copy_to_container("Test3", "./demo/TestFile", "/home")


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

def list_containers():
    try:
        # Run lxc-ls command to list containers
        list_output = subprocess.run(['sudo', 'lxc-ls', '--fancy'], capture_output=True, text=True, check=True)

        # Process the output to extract container names and their states
        container_lines = list_output.stdout.strip().split('\n')[1:]  # Skip header line

        print("Existing containers and their states:")
        for line in container_lines:
            parts = line.split()
            if len(parts) >= 2:
                container_name = parts[0]
                state = parts[1]
                print(f"{container_name}: {state}")

    except subprocess.CalledProcessError as e:
        print(f"Failed to list containers: {e}")
