# hellow-mcp

Run an MCP server on a Raspberry Pi at home so that Claude can work with the home server and its sensors.

## Design

A visual overview of the system design is in [`architecture/index.html`](architecture/index.html). Open it in a browser to view it.

## Hardware

| Item | Details |
|---|---|
| Board | Raspberry Pi 4 Model B (the one at home) |
| Memory | 4GB |
| Storage | Undecided (booting from a USB-connected SSD is recommended for always-on use) |
| Power | USB-C 5V 3A (15W) |

## Tech stack

| Item | Choice |
|---|---|
| Language | Python |
| MCP library | FastMCP |

## Run

```sh
uv run hellow-mcp
```

The server speaks MCP over stdio. To use it from Claude Desktop, add this to `mcpServers` in `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
"hellow-mcp": {
  "command": "uv",
  "args": ["--directory", "/path/to/hellow-mcp", "run", "hellow-mcp"]
}
```
