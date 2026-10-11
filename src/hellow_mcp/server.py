from fastmcp import FastMCP

from hellow_mcp.services import list_services
from hellow_mcp.system import get_system_status

mcp = FastMCP("hellow-mcp")
mcp.tool(get_system_status)
mcp.tool(list_services)


def main() -> None:
    mcp.run()
