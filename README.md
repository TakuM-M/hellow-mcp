# hellow-mcp

Run an MCP server on a Raspberry Pi at home so that Claude can work with the home server and its sensors.

## Design

A visual overview of the system design is in [`architecture/index.html`](architecture/index.html). Open it in a browser to view it.

## Hardware

| Item | Details |
|---|---|
| Board | Raspberry Pi 4 Model B (the one at home) |
| Memory | 4GB |
| Storage | microSD card |
| Power | USB-C 5V 3A (15W) |

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

## Run on the Pi

The server runs on the Pi as the low-privilege user `mcp`, and Claude starts it over SSH (route ① in the design).

On the Pi, as `mcp`:

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
git clone https://github.com/TakuM-M/hellow-mcp.git
cd hellow-mcp && ~/.local/bin/uv sync
```

On your PC, register it with Claude Code:

```sh
claude mcp add hellow-mcp -- ssh -T -o BatchMode=yes mcp@raspberrypi.local /home/mcp/.local/bin/uv --directory /home/mcp/hellow-mcp run hellow-mcp
```

Claude cannot type an SSH key passphrase, so on macOS store it in the Keychain once with `ssh-add --apple-use-keychain ~/.ssh/id_ed25519` and add this to `~/.ssh/config`:

```
Host raspberrypi.local
    UseKeychain yes
```
