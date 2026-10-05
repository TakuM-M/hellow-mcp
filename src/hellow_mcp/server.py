from fastmcp import FastMCP

from hellow_mcp.system import get_system_status

mcp = FastMCP("hellow-mcp")
mcp.tool(get_system_status)


def main() -> None:
    mcp.run()
