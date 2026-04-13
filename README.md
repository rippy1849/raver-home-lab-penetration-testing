# 🎧 Raver's Paradise — Intentionally Vulnerable Web App

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Flask](https://img.shields.io/badge/Flask-3.0+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Purpose](https://img.shields.io/badge/Purpose-CTF%20%2F%20Education-red)

> **⚠️ WARNING: This application is intentionally vulnerable. Do not deploy on a public server or any network you do not own and control. For educational and CTF use only.**

---

## Overview

Raver's Paradise is an intentionally vulnerable web application built for security education and CTF training. It simulates a real-world festival website with believable functionality and a layered set of vulnerabilities that increase in complexity — from beginner-friendly SQL injection to a real CVE-based privilege escalation.

Every vulnerability is hidden inside otherwise normal-looking functionality. There are no labels, no hints in the UI, and no guided walkthroughs built into the app itself. Players are expected to approach it the same way a real penetration tester would.

---

## Features

- 🎨 Fully themed neon EDM / rave aesthetic
- 9 flags across 8 vulnerability categories
- Realistic vulnerability chaining — some flags require exploiting multiple vulns in sequence
- Real PHP reverse shell execution via php-cli
- SQLite database — no external services required
- Runs on Windows and Linux via Waitress WSGI server

---

## Vulnerabilities

| Flag | Category |
|------|----------|
| flag1 | SQL Injection — Authentication Bypass |
| flag2 | SQL Injection — Data Exfiltration |
| flag3 | IDOR — Insecure Direct Object Reference |
| flag4 | LFI — Local File Inclusion |
| flag5 | Log Poisoning + RCE |
| flag6 | Unrestricted File Upload + Reverse Shell |
| flag7 | HTTP Verb Tampering |
| flag8 | Easter Egg — Encoding Challenge |
| flag9 | Privilege Escalation — Baron Samedit (CVE-2021-3156) |

---

## Requirements

- Python 3.8+
- php-cli (`sudo apt install php-cli`)
- A Linux environment is strongly recommended (WSL works on Windows)

---

## Installation

**1. Clone the repository:**
```bash
git clone https://github.com/YOUR-USERNAME/ravers-paradise.git
cd ravers-paradise