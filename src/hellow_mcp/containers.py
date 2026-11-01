import json
import shutil
import subprocess

import yaml

from hellow_mcp.logs import CONFIG_PATH


def _docker(*args: str) -> str:
    # Capture stdout because the MCP protocol uses the stdout of the server.
    result = subprocess.run(
        ["sudo", "-n", "docker", *args],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip())
    return result.stdout


def _parse_containers(output: str) -> list[dict]:
    """Convert the JSON lines from docker ps to container records."""
    return [
        {
            "name": container["Names"],
            "image": container["Image"],
            "state": container["State"],
            "status": container["Status"],
        }
        for container in map(json.loads, output.splitlines())
    ]


def list_containers() -> list[dict]:
    """Return all Docker containers, or an empty list when Docker is not installed."""
    if shutil.which("docker") is None:
        return []
    return _parse_containers(_docker("ps", "--all", "--format", "json"))


def restart_container(name: str) -> str:
    """Restart a Docker container on the allowlist in config.yaml."""
    allowed = yaml.safe_load(CONFIG_PATH.read_text())["allowed_containers"]
    if name not in allowed:
        raise ValueError(f"{name} is not allowed. Allowed containers: {allowed}")
    _docker("restart", name)
    return f"Restarted {name}"
