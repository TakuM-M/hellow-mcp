# hellow-mcp

Run an MCP server on a Raspberry Pi at home so that Claude can work with the home server and its sensors.

## Design

The source of truth for the system design is [`architecture/index.html`](architecture/index.html). Open it in a browser to view it.

## Hardware

| Item | Details |
|---|---|
| Board | Raspberry Pi 4 Model B (tentative: planning to use the one at home; to be confirmed on the device) |
| Memory | Unconfirmed (runs on 2GB or more; 4GB or more recommended if running several Docker containers) |
| Storage | Undecided (booting from a USB-connected SSD is recommended for always-on use) |
| Power | USB-C 5V 3A (15W) |

To check on the device:

```bash
cat /proc/device-tree/model   # e.g. Raspberry Pi 4 Model B Rev 1.4
free -h                       # memory size
```
