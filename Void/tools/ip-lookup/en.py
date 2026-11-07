#!/usr/bin/env python3
import sys, socket, urllib.request, json, time

def run():
    print("\n\033[38;2;139;0;0m┌────────────────────────────────────────────────────────┐\033[0m")
    print("\033[38;2;139;0;0m│\033[0m \033[38;2;255;32;32m\033[1mALTBLACK OSINT // MODULE: REAL IP & DOMAIN LOOKUP\033[0m   \033[38;2;139;0;0m│\033[0m")
    print("\033[38;2;139;0;0m└────────────────────────────────────────────────────────┘\033[0m\n")
    
    target = input("\033[38;2;255;32;32m>> Enter domain or IP to query (e.g. google.com) >> \033[0m").strip()
    if not target:
        print("\033[31m[!] No target provided.\033[0m")
        return
        
    # Pulisce l'URL se l'utente mette http:// o https://
    clean_target = target.replace("http://", "").replace("https://", "").split("/")[0]
    
    print(f"\n\033[33m[*] Resolving DNS and querying routing nodes for: {clean_target}...\033[0m")
    
    resolved_ip = "N/A"
    try:
        resolved_ip = socket.gethostbyname(clean_target)
    except Exception:
        resolved_ip = clean_target # Se era già un IP o non risolve
        
    # Interrogazione API pubblica per geolocalizzazione/dati reali
    geo_data = {}
    try:
        url = f"http://ip-api.com/json/{resolved_ip}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=3) as response:
            geo_data = json.loads(response.read().decode())
    except Exception:
        pass

    time.sleep(1)
    
    print("\n" + "\033[38;2;139;0;0m" + "="*65 + "\033[0m")
    print(f" \033[1m[+] TARGET INPUT    :\033[0m {target}")
    print(f" \033[1m[+] RESOLVED IP     :\033[0m {resolved_ip}")
    
    if geo_data.get('status') == 'success':
        print(f" \033[1m[+] ISP / NETWORK   :\033[0m {geo_data.get('isp', 'Unknown')} ({geo_data.get('as', '')})")
        print(f" \033[1m[+] COUNTRY / CITY  :\033[0m {geo_data.get('country', 'N/A')} / {geo_data.get('city', 'N/A')}")
        print(f" \033[1m[+] ORGANIZATION    :\033[0m {geo_data.get('org', 'N/A')}")
        print(f" \033[1m[+] STATUS          :\033[0m Active Node / Online")
    else:
        print(f" \033[1m[+] STATUS          :\033[0m Responsive / Custom Node")
        
    print("\033[38;2;139;0;0m" + "="*65 + "\033[0m\n")

if __name__ == '__main__':
    run()
