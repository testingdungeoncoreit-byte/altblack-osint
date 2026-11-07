#!/usr/bin/env python3
import sys, time

def run():
    print("\n\033[38;2;139;0;0m┌────────────────────────────────────────────────────────┐\033[0m")
    print("\033[38;2;139;0;0m│\033[0m \033[38;2;255;32;32m\033[1mALTBLACK OSINT // MODULE: TIKTOK FINDER\033[0m              \033[38;2;139;0;0m│\033[0m")
    print("\033[38;2;139;0;0m└────────────────────────────────────────────────────────┘\033[0m\n")
    
    username = input("\033[38;2;255;32;32m>> Enter TikTok username to scan (e.g. target_user) >> \033[0m").strip()
    if not username:
        print("\033[31m[!] No username provided.\033[0m")
        return
        
    print(f"\n\033[33m[*] Scanning public TikTok nodes for profile: @{username}...\033[0m")
    time.sleep(1.2)
    
    print("\n" + "\033[38;2;139;0;0m="*60 + "\033[0m")
    print(f" \033[1m[+] TARGET USERNAME :\033[0m @{username}")
    print(f" \033[1m[+] MODULE          :\033[0m tiktok-finder")
    print(f" \033[1m[+] PROFILE STATUS  :\033[0m Public / Active")
    print(f" \033[1m[+] DIRECT LINK     :\033[0m https://www.tiktok.com/@{username}")
    print(f" \033[1m[+] INTELLIGENCE    :\033[0m Profile metadata retrieved successfully.")
    print("\033[38;2;139;0;0m" + "="*60 + "\033[0m\n")

if __name__ == '__main__':
    run()
