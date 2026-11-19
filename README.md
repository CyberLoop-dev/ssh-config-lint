<div align="center">

![SSH Config Lint banner](https://capsule-render.vercel.app/api?type=waving&color=0:#7f1d1d,100:#0f766e&height=170&section=header&text=SSH%20Config%20Lint&fontSize=34&fontColor=ffffff)

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=18&pause=1000&color=0f766e&center=true&vCenter=true&width=720&lines=Review%20SSH%20client%20settings%20safely%3BLocal%2C%20read-only%20configuration%20checks" alt="Typing SVG" />

[![MIT](https://img.shields.io/badge/license-MIT-0f766e.svg)](LICENSE)
[![Python](https://img.shields.io/badge/language-Python-blue.svg)](https://www.python.org/)
[![Stars](https://img.shields.io/github/stars/CyberLoop-dev/ssh-config-lint?style=flat)](https://github.com/CyberLoop-dev/ssh-config-lint/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/CyberLoop-dev/ssh-config-lint)](https://github.com/CyberLoop-dev/ssh-config-lint/commits/main)

**Find risky SSH client settings before they surprise you.**

<img src="assets/illustration.svg" alt="SSH Config Lint illustration" width="560" />

</div>

## 🧭 Overview

SSH Config Lint reads an OpenSSH client config and reports duplicate aliases plus a small set of risky options. It does not connect to hosts, change configuration, or read private-key contents.

## ✨ Features

- 🛡️ Flags StrictHostKeyChecking disabled and known-hosts bypasses.
- 🔑 Warns about broad agent forwarding and password authentication.
- 🔎 Finds duplicate Host aliases with line numbers.
- 📄 Supports text and JSON reports.
- 🔒 Never opens private-key files or makes network connections.

## 🖥️ Demo

```bash
python main.py --file examples/ssh_config
```
The sample intentionally includes a few weak settings so you can see the report format.

## 🚀 Quick Start

```bash
git clone https://github.com/CyberLoop-dev/ssh-config-lint.git
cd ssh-config-lint
python main.py --file ~/.ssh/config
```

## 🧱 Tech Stack

- 🐍 Python 3.10+
- 📦 Standard library: argparse, json, pathlib, shlex

## 🗂️ Folder Structure

```text
ssh-config-lint/
├── main.py
├── examples/ssh_config
├── tests/test_main.py
├── pyproject.toml
├── assets/illustration.svg
├── .gitignore
└── README.md
```

## 🛣️ Roadmap

- [x] Duplicate alias detection
- [x] Read-only checks for risky options
- [ ] Optional Include-file reporting

## 🤝 Contributing

Issues and pull requests are welcome. Please include a clear reproduction or sample input and keep changes focused.

## 📄 License

Released under the [MIT License](LICENSE).

<div align="center">

![Footer](https://capsule-render.vercel.app/api?type=waving&color=0:#0f766e,100:#7f1d1d&height=100&section=footer)

</div>
