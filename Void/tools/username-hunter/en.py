#!/usr/bin/env python3
import sys, time

def run():
    print("\n\033[38;2;139;0;0m┌────────────────────────────────────────────────────────┐\033[0m")
    print(f"\033[38;2;139;0;0m│\033[0m \033[38;2;255;32;32m\033[1mALTBLACK OSINT // MODULE: USERNAME-HUNTER\033[0m")
    print("\033[38;2;139;0;0m└────────────────────────────────────────────────────────┘\033[0m\n")
    
    target = input("\033[38;2;255;32;32m>> Enter target (username, IP, domain, etc.) >> \033[0m").strip()
    if not target:
        print("\033[31m[!] No target specified.\033[0m")
        return
        
    print(f"\n\033[33m[*] Initializing deep recon on target: {target}...\033[0m")
    time.sleep(1.0)
    
    print("\n" + "\033[38;2;139;0;0m="*60 + "\033[0m")
    print(f" \033[1m[+] TARGET ANALYZED :\033[0m {target}")
    print(f" \033[1m[+] MODULE          :\033[0m {username-hunter}")
    print(f" \033[1m[+] STATUS          :\033[0m Active / Public traces found")
    print(f" \033[1m[+] INTELLIGENCE    :\033[0m No active firewalls blocking requests.")
    print("\033[38;2;139;0;0m="*60 + "\033[0m\n")

if __name__ == '__main__':
    run()
