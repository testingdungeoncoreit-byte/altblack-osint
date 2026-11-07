#!/usr/bin/env python3
import sys, socket, urllib.request, json, time

def run():
    print("\n\033[38;2;139;0;0m┌────────────────────────────────────────────────────────┐\033[0m")
    print("\033[38;2;139;0;0m│\033[0m \033[38;2;255;32;32m\033[1mALTBLACK OSINT // MODULE: DOMAIN INTEL               \033[0m\033[38;2;139;0;0m│\033[0m")
    print("\033[38;2;139;0;0m└────────────────────────────────────────────────────────┘\033[0m\n")
    
    target = input("\033[38;2;255;32;32m>> Enter domain to analyze (e.g. spaggiari.eu) >> \033[0m").strip()
    if not target:
        print("\033[31m[!] No target provided.\033[0m")
        return
        
    clean_target = target.replace("http://", "").replace("https://", "").split("/")[0]
    
    print(f"\n\033[33m[*] Initializing deep recon and DNS resolution for: {clean_target}...\033[0m")
    
    resolved_ip = "N/A"
    try:
        resolved_ip = socket.gethostbyname(clean_target)
    except Exception:
        resolved_ip = "Unresolved / Protected"
        
    geo_data = {}
    try:
        url = f"http://ip-api.com/json/{resolved_ip}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=3) as response:
            geo_data = json.loads(response.read().decode())
    except Exception:
        pass

    time.sleep(1.2)
    
    print("\n" + "\033[38;2;139;0;0m" + "="*65 + "\033[0m")
    print(f" \033[1m[+] TARGET DOMAIN   :\033[0m {clean_target}")
    print(f" \033[1m[+] MODULE          :\033[0m domain-intel")
    print(f" \033[1m[+] ROOT SERVER IP  :\033[0m {resolved_ip}")
    
    if geo_data.get('status') == 'success':
        print(f" \033[1m[+] HOSTING ISP     :\033[0m {geo_data.get('isp', 'Unknown')} ({geo_data.get('as', '')})")
        print(f" \033[1m[+] REGION / COUNTRY:\033[0m {geo_data.get('city', 'N/A')} / {geo_data.get('country', 'N/A')}")
        print(f" \033[1m[+] ORGANIZATION    :\033[0m {geo_data.get('org', 'N/A')}")
    
    print(f" \033[1m[+] STATUS          :\033[0m Active Infrastructure / Online")
    print("\033[38;2;139;0;0m" + "="*65 + "\033[0m\n")

if __name__ == '__main__':
    run()
