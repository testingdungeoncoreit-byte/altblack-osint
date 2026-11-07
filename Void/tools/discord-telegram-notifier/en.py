#!/usr/bin/env python3
import sys, json, urllib.request, time

def run():
    print("\n\033[38;2;139;0;0m┌────────────────────────────────────────────────────────┐\033[0m")
    print("\033[38;2;139;0;0m│\033[0m \033[38;2;255;32;32m\033[1mALTBLACK CYBER // DISCORD THREAT INTEL DROPPER     \033[0m\033[38;2;139;0;0m│\033[0m")
    print("\033[38;2;139;0;0m└────────────────────────────────────────────────────────┘\033[0m\n")
    
    server_id = input("\033[38;2;255;32;32m>> Enter Discord Server ID >> \033[0m").strip()
    if not server_id:
        print("\033[31m[!] Server ID required.\033[0m")
        return
        
    webhook_url = input("\033[38;2;255;32;32m>> Enter Discord Channel Webhook URL >> \033[0m").strip()
    if not webhook_url:
        print("\033[31m[!] Webhook URL required for dispatch.\033[0m")
        return
        
    target = input("\033[38;2;255;32;32m>> Enter Target / Asset Name (e.g. Domain / IP / Alias) >> \033[0m").strip()
    findings = input("\033[38;2;255;32;32m>> Enter Security Findings / Hardening Notes >> \033[0m").strip()
    
    if not target or not findings:
        print("\033[31m[!] Missing target or telemetry data.\033[0m")
        return

    print(f"\n\033[33m[*] Routing telemetry to Discord Server [{server_id}]...\033[0m")
    
    payload = {
        "username": "AltBlack Threat Intel Bot",
        "avatar_url": "https://i.imgur.com/4M34hi2.png",
        "embeds": [
            {
                "title": f"🛡️ CYBER INTEL REPORT // TARGET: {target}",
                "description": f"**Target Asset:** `{target}`\n**Server ID Target:** `{server_id}`\n\n```ini\n[TELEMETRY & FINDINGS]\n{findings}\n```",
                "color": 14155776, # Dark red / Security alert color
                "fields": [
                    {
                        "name": "Framework Status",
                        "value": "Active Recon & Hardening Audit",
                        "inline": True
                    },
                    {
                        "name": "Security Level",
                        "value": "Encrypted Payload",
                        "inline": True
                    }
                ],
                "footer": {
                    "text": "AltBlack OSINT Suite v40.0 · Cyber Defense Division"
                },
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
            }
        ]
    }
    
    try:
        req = urllib.request.Request(
            webhook_url,
            data=json.dumps(payload).encode('utf-8'),
            headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
        )
        with urllib.request.urlopen(req, timeout=5) as response:
            if response.status in [200, 204]:
                print(f"\n\033[32m[+] Threat Intel report successfully dropped to Server ID: {server_id}!\033[0m")
            else:
                print(f"\n\033[31m[!] Discord API returned status: {response.status}\033[0m")
    except Exception as e:
        print(f"\n\033[31m[!] Transmission failed: {e}\033[0m")
        
    print("\n" + "\033[38;2;139;0;0m" + "="*56 + "\033[0m\n")

if __name__ == '__main__':
    run()
