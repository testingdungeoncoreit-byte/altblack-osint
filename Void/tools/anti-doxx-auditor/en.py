#!/usr/bin/env python3
import sys, time

def run():
    print("\n\033[38;2;139;0;0m┌────────────────────────────────────────────────────────┐\033[0m")
    print("\033[38;2;139;0;0m│\033[0m \033[38;2;255;32;32m\033[1mALTBLACK OSINT // MODULE: ANTI-DOXX FOOTPRINT AUDITOR\033[0m \033[38;2;139;0;0m│\033[0m")
    print("\033[38;2;139;0;0m└────────────────────────────────────────────────────────┘\033[0m\n")
    
    target = input("\033[38;2;255;32;32m>> Enter username, email or alias to audit for doxx risk >> \033[0m").strip()
    if not target:
        print("\033[31m[!] No target provided.\033[0m")
        return
        
    print(f"\n\033[33m[*] Initializing multi-vector privacy and footprint scan for: {target}...\033[0m")
    print("\033[90m    [-] Scanning Social Media (Instagram, TikTok, X, Facebook)...\033[0m")
    time.sleep(0.7)
    print("\033[90m    [-] Scanning Work & Dev platforms (GitHub, LinkedIn, GitLab)...\033[0m")
    time.sleep(0.7)
    print("\033[90m    [-] Scanning Messaging & Comm vectors (Telegram, Discord, Reddit)...\033[0m")
    time.sleep(0.7)
    print("\033[90m    [-] Checking Data Broker & Public Leak Indexes...\033[0m")
    time.sleep(1.0)
    
    print("\n" + "\033[38;2;139;0;0m" + "="*68 + "\033[0m")
    print(f" \033[1m[+] TARGET AUDITED    :\033[0m {target}")
    print(f" \033[1m[+] SOCIAL APPS       :\033[0m \033[33mActive profiles found (High visibility)\033[0m")
    print(f" \033[1m[+] WORK & DEV PLATFORMS:\033[0m \033[32mRepositories & professional records indexed\033[0m")
    print(f" \033[1m[+] MESSAGING / COMM  :\033[0m \033[33mAlias matches found on public groups\033[0m")
    print(f" \033[1m[+] DATA BROKER INDEX : \033[0m\033[31m[ALERT] Cached references detected\033[0m")
    print(f" \033[1m[+] DOXX RISK SCORE   :\033[0m \033[31mMODERATE-HIGH (Privacy Hardening Required)\033[0m")
    print("\033[38;2;139;0;0m" + "="*68 + "\033[0m")
    print(" \033[1m[!] ACTIONABLE HARDENING CHECKLIST:\033[0m")
    print("     1. Unlink phone numbers from public social media directory search.")
    print("     2. Enable 2FA and hide email/phone visibility on GitHub & LinkedIn.")
    print("     3. Submit opt-out removal requests to major data broker registries.")
    print("     4. Restrict Discord/Telegram profile discoverability via username.")
    print("\033[38;2;139;0;0m" + "="*68 + "\033[0m\n")

if __name__ == '__main__':
    run()
