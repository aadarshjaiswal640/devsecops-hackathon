| Change Made             | What It Prevents                                 |
| ----------------------- | ------------------------------------------------ |
| Use `python:3.11-slim`  | Reduces attack surface and vulnerabilities       |
| Avoid `latest` tag      | Prevents unexpected package changes              |
| Create non-root user    | Limits impact of container compromise            |
| Pin dependency versions | Prevents dependency drift and supply-chain risks |
| Use `--no-cache-dir`    | Reduces image size and unnecessary files         |
