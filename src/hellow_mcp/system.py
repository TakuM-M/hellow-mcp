import time

import psutil


def get_system_status() -> dict:
    """Return CPU temperature, load average, memory, free disk space on / and uptime."""
    temps = getattr(psutil, "sensors_temperatures", lambda: {})()
    readings = next(iter(temps.values()), [])
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    return {
        "cpu_temp_c": readings[0].current if readings else None,
        "load_avg": list(psutil.getloadavg()),
        "memory": {
            "total_bytes": memory.total,
            "available_bytes": memory.available,
            "percent": memory.percent,
        },
        "disk": {
            "total_bytes": disk.total,
            "free_bytes": disk.free,
            "percent": disk.percent,
        },
        "uptime_seconds": int(time.time() - psutil.boot_time()),
    }
