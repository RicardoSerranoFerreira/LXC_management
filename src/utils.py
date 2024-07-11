import subprocess
import os

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
