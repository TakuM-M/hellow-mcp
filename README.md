# hellow-mcp

自宅の Raspberry Pi で MCP サーバーを動かし、Claude から自宅サーバーやセンサーを扱えるようにするプロジェクト。

## 設計

設計の正本は [`architecture/index.html`](architecture/index.html)。ブラウザで開いて確認する。

## ハードウェア

| 項目 | 内容 |
|---|---|
| 本体 | Raspberry Pi 4 Model B（暫定。自宅にあるものを使う予定、実機で要確認） |
| メモリ | 未確認（2GB 以上で動作、Docker を複数動かすなら 4GB 以上が目安） |
| ストレージ | 未定（常時稼働のため USB 接続 SSD からの起動を推奨） |
| 電源 | USB-C 5V 3A（15W） |

実機での確認方法:

```bash
cat /proc/device-tree/model   # 例: Raspberry Pi 4 Model B Rev 1.4
free -h                       # メモリ容量
```
