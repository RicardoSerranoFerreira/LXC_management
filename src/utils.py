import subprocess
import logging

# Set up logger
logger = logging.getLogger(__name__)

def set_resource_limits(container_name, cpu_limit=None, memory_limit=None):
    if cpu_limit:
        try:
            subprocess.run(['lxc-cgroup', '-n', container_name, 'cpuset.cpus', cpu_limit], check=True)
            logger.info(f"Set CPU limit for {container_name} to {cpu_limit}")
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to set CPU limit for {container_name}: {e}")

    if memory_limit:
        try:
            subprocess.run(['lxc-cgroup', '-n', container_name, 'memory.limit_in_bytes', memory_limit], check=True)
            logger.info(f"Set memory limit for {container_name} to {memory_limit}")
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to set memory limit for {container_name}: {e}")

def get_resource_limits(container_name):
    try:
        cpu_limit_process = subprocess.run(['lxc-cgroup', '-n', container_name, 'cpuset.cpus'], capture_output=True, text=True, check=True)
        cpu_limit = cpu_limit_process.stdout.strip()

        memory_limit_process = subprocess.run(['lxc-cgroup', '-n', container_name, 'memory.limit_in_bytes'], capture_output=True, text=True, check=True)
        memory_limit = memory_limit_process.stdout.strip()

        logger.info(f"Current resource limits for {container_name}:")
        logger.info(f"CPU limit: {cpu_limit if cpu_limit else 'Not set'}")
        logger.info(f"Memory limit: {memory_limit if memory_limit else 'Not set'}")

    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to get resource limits for {container_name}: {e}")
