from fastmcp import FastMCP

from hellow_mcp.containers import restart_container
from hellow_mcp.logs import read_logs
from hellow_mcp.services import list_services
from hellow_mcp.system import get_system_status

mcp = FastMCP("hellow-mcp")
mcp.tool(get_system_status)
mcp.tool(list_services)
mcp.tool(read_logs)
mcp.tool(restart_container)


def main() -> None:
    mcp.run()
