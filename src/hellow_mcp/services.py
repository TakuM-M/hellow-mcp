import json
import subprocess


def _systemctl(*args: str) -> str:
    result = subprocess.run(
        ["systemctl", "--no-pager", *args],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout


def list_services() -> list[dict]:
    """Return the state and main PID of loaded systemd services that are active or failed.

    pid is 0 when the service has no running main process (e.g. sub is "exited").
    """
    units = json.loads(_systemctl("list-units", "--type=service", "--output=json"))
    # systemctl show prints one value per unit, in the order the units are given.
    pids = _systemctl("show", "--property=MainPID", "--value", *(u["unit"] for u in units)).split()
    return [
        {
            "unit": unit["unit"],
            "active": unit["active"],
            "sub": unit["sub"],
            "pid": int(pid),
            "description": unit["description"],
        }
        for unit, pid in zip(units, pids, strict=True)
    ]
