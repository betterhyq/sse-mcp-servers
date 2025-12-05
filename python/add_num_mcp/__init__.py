from pydantic import Field
from mcp.server.fastmcp import FastMCP

from . import add_tool

def main(port: int) -> None:
    mcp = FastMCP(
        name="Add Num MCP", 
        host="0.0.0.0", 
        port=port
    )

    @mcp.tool(description="Add Num MCP")
    def add(a: int = Field(description="The first number"), b: int = Field(description="The second number")) -> str:
        return add_tool.add(a, b)
        

    mcp.run(transport="sse")
