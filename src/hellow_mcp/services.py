import json
import subprocess

from hellow_mcp.containers import list_containers


def _systemctl(*args: str) -> str:
    result = subprocess.run(
        ["systemctl", "--no-pager", *args],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout


def list_services() -> dict:
    """Return loaded systemd services that are active or failed, and all Docker containers.

    "services" has the state and main PID of each systemd service.
    pid is 0 when the service has no running main process (e.g. sub is "exited").
    "containers" is empty when Docker is not installed.
    """
    units = json.loads(_systemctl("list-units", "--type=service", "--output=json"))
    # systemctl show prints one value per unit, in the order the units are given.
    pids = _systemctl("show", "--property=MainPID", "--value", *(u["unit"] for u in units)).split()
    services = [
        {
            "unit": unit["unit"],
            "active": unit["active"],
            "sub": unit["sub"],
            "pid": int(pid),
            "description": unit["description"],
        }
        for unit, pid in zip(units, pids, strict=True)
    ]
    return {"services": services, "containers": list_containers()}
