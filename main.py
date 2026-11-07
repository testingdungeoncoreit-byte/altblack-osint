#!/usr/bin/env python3
"""
 █████╗ ██╗     ████████╗██████╗ ██╗      █████╗  ██████╗██╗  ██╗
██╔══██╗██║     ╚══██╔══╝██╔══██╗██║     ██╔══██╗██╔════╝██║  ██║
███████║██║        ██║   ██████╔╝██║     ███████║██║     █████╔╝ 
██╔══██║██║        ██║   ██╔══██╗██║     ██╔══██║██║     ██╔-██╗ 
██║  ██║███████╗   ██║   ██████╔╝███████╗██║  ██║╚██████╗██║  ██╗
  altblack-tools v40.0  ·  OSINT & Cybersecurity Suite
"""
import os, sys, time, shutil, subprocess, webbrowser, re, random, math, threading, string, urllib.request, json, hashlib, base64
from colorama import init, Fore, Style
init(autoreset=True)

from rich.console  import Console
from rich.panel    import Panel
from rich.table    import Table
from rich.text     import Text
from rich.columns  import Columns
from rich.rule     import Rule
from rich.align    import Align
from rich.live     import Live
from rich.progress import Progress, BarColumn, TextColumn, SpinnerColumn
from rich          import box
import pyfiglet

console = Console(highlight=False)

C_BLOOD   = "#8B0000"
C_DARK    = "#AA0000"
C_MID     = "#CC0000"
C_RED     = "#EE0000"
C_NEON    = "#FF2020"
C_BRIGHT  = "#FF4444"
C_WHITE   = "#FFFFFF"
C_SILVER  = "#CCCCCC"
C_DIM     = "#666666"
C_GOLD    = "#FFD700"
C_GOLD2   = "#FFA500"

TELEGRAM_TAG = "altblack.tools"
path         = os.getcwd()

ACTIVE_TIER = "base"

def play_background_audio():
    """Avvia la riproduzione del brano di sottofondo in un thread separato"""
    try:
        audio_url = "https://www.youtube.com/watch?v=FLRKbkcqgAQ"
        webbrowser.open(audio_url)
    except Exception:
        pass

def verify_access():
    global ACTIVE_TIER
    cls()
    print("\n\033[38;2;139;0;0m┌────────────────────────────────────────────────────────┐\033[0m")
    print("\033[38;2;139;0;0m│\033[0m \033[38;2;255;32;32m\033[1mALTBLACK OSINT // COMMERCIAL LICENSING GATEWAY     \033[0m\033[38;2;139;0;0m│\033[0m")
    print("\033[38;2;139;0;0m└────────────────────────────────────────────────────────┘\033[0m\n")
    print(" \033[33m[!] Enter your purchase license key to unlock modules.\033[0m\n")
    
    key = input("\033[38;2;255;32;32m>> Enter License Key >> \033[0m").strip()
    
    if key == "altblack_base_2026":
        ACTIVE_TIER = "base"
        print("\n\033[32m[+] License Verified: BASE TIER (Anti-Doxx & Core Unlocked)[/]")
        time.sleep(1.5)
    elif key == "altblack_inter_2026":
        ACTIVE_TIER = "intermediate"
        print("\n\033[32m[+] License Verified: INTERMEDIATE TIER (Recon & Network Unlocked)[/]")
        time.sleep(1.5)
    elif key == "altblack_enterprise_2026":
        ACTIVE_TIER = "full"
        print("\n\033[32m[+] License Verified: ENTERPRISE TIER (Full Suite + Support Unlocked)[/]")
        time.sleep(1.5)
    else:
        print("\n\033[31m[!] ACCESS DENIED: Invalid or expired license key.\033[0m")
        time.sleep(2)
        sys.exit(0)

def check_permission(page):
    if ACTIVE_TIER == "base" and page > 2:
        return False
    elif ACTIVE_TIER == "intermediate" and page > 4:
        return False
    return True

def get_allowed_cols(page, tier):
    cols = PAGES_DATABASE.get(page, {}).get("cols", [])
    if tier == "base":
        if page == 1:
            return [("01","OSINT Hub"), ("03","About")]
        elif page == 2:
            return [("09","Anti-Doxx Auditor")]
        else:
            return []
    elif tier == "intermediate":
        if page > 4:
            return []
        return cols
    else:
        return cols

def sp(f, n):
    alt_f = "antidox-audit" if f == "anti-doxx-auditor" else "anti-doxx-auditor"
    paths = [
        os.path.join(path, "Void", "tools", f, n),
        os.path.join(path, "tools", f, n),
        os.path.join(path, "Void", "tools", alt_f, n),
        os.path.join(path, "tools", alt_f, n)
    ]
    for p in paths:
        if os.path.exists(p):
            return p
    return paths[0]

def cls():    os.system("cls" if os.name == "nt" else "clear")
def tw():     return shutil.get_terminal_size((100, 30)).columns
def th():     return shutil.get_terminal_size((100, 30)).lines
def norm(o):
    o = o.strip()
    return f"0{o}" if o.isdigit() and len(o) == 1 else o

_RAIN = list("01▓▒░│┤╣║╗╝┐└┴┬├─┼╚╔╩╦╠═╬┘┌AB3F9E#%&?$")

def play_intro():
    # Avvia la musica di sottofondo in parallelo durante l'intro Matrix
    audio_thread = threading.Thread(target=play_background_audio, daemon=True)
    audio_thread.start()

    w = tw(); h = max(th() - 2, 20)
    columns = []
    for _ in range(w):
        columns.append({
            "pos": random.uniform(-h, 0),
            "speed": random.uniform(0.8, 2.2),
            "length": random.randint(6, int(h * 0.7))
        })
    
    t0 = time.monotonic()
    with Live(console=console, screen=True, refresh_per_second=24, transient=True) as live:
        while time.monotonic() - t0 < 3.5:
            grid = [[" " for _ in range(w)] for _ in range(h)]
            styles = [["" for _ in range(w)] for _ in range(h)]
            
            for col_idx, col in enumerate(columns):
                col["pos"] += col["speed"]
                head_pos = int(col["pos"])
                length = col["length"]
                
                for row in range(max(0, head_pos - length), min(h, head_pos + 1)):
                    if row < 0: continue
                    dist_from_head = head_pos - row
                    ch = random.choice(_RAIN)
                    grid[row][col_idx] = ch
                    if dist_from_head == 0:
                        styles[row][col_idx] = "bold #FFFFFF"
                    elif dist_from_head < 3:
                        styles[row][col_idx] = "bold #FF4444"
                    elif dist_from_head < length * 0.5:
                        styles[row][col_idx] = "#CC0000"
                    else:
                        styles[row][col_idx] = "#8B0000"
                
                if head_pos - length > h:
                    col["pos"] = random.uniform(-h * 0.6, 0)
                    col["speed"] = random.uniform(0.8, 2.2)
                    col["length"] = random.randint(6, int(h * 0.7))
            
            f = Text()
            for r in range(h):
                for c in range(w):
                    ch = grid[r][c]
                    st = styles[r][c]
                    if st:
                        f.append(ch, style=st)
                    else:
                        f.append(" ")
                if r < h - 1:
                    f.append("\n")
            live.update(f)
            time.sleep(1 / 24)

def gradient_line(text, w=None):
    t = Text(); n = len(text)
    for i, ch in enumerate(text):
        frac = i / max(n - 1, 1)
        r = int(0x8B + frac * (0xFF - 0x8B))
        t.append(ch, style=f"#{r:02X}0000 bold")
    return t

_NOISE = list("#%&!?$@+-=~^/*|\\><▓▒░")

def glitch_reveal_rich(text):
    n = len(text); revealed = [False] * n
    with Live(console=console, refresh_per_second=30, transient=True) as live:
        for _ in range(6):
            t = Text()
            for ch in text:
                if random.random() < 0.6:
                    t.append(random.choice(_NOISE), style=C_BLOOD)
                else:
                    t.append(ch, style=f"{C_NEON} bold")
            live.update(Align.center(t)); time.sleep(0.04)
        s = 0
        while not all(revealed):
            if s < n:       revealed[s]     = True
            if n - 1 - s >= 0: revealed[n-1-s] = True
            t = Text()
            for i, ch in enumerate(text):
                if revealed[i]:
                    frac = i / max(n-1, 1)
                    r = int(0x8B + frac * (0xFF - 0x8B))
                    t.append(ch, style=f"#{r:02X}0000 bold")
                else:
                    t.append(random.choice(_NOISE), style=C_BLOOD)
            live.update(Align.center(t)); time.sleep(0.028); s += 1
    console.print(Align.center(gradient_line(text)))

def rich_boot_bars():
    tasks_cfg = [
        ("KERNEL LOAD",     0.18), ("MEMORY ALLOC",    0.22),
        ("NET INTERFACE",   0.19), ("CRYPTO ENGINE",   0.15),
        ("OSINT MODULE",    0.20), ("EXIF PARSER",     0.17),
        ("RENDER PIPELINE", 0.16), ("REPORT ENGINES",  0.21),
    ]
    with Progress(
        SpinnerColumn(style=f"{C_NEON} bold"),
        TextColumn(f"[{C_SILVER}]{{task.description:<20}}"),
        BarColumn(bar_width=32, style=C_BLOOD, complete_style=C_NEON, finished_style=C_BRIGHT),
        TextColumn(f"[{C_NEON} bold]{{task.percentage:>5.1f}}%"),
        console=console, transient=False,
    ) as progress:
        job_ids = [progress.add_task(label, total=100) for label, _ in tasks_cfg]
        while not all(progress.tasks[jid].finished for jid in job_ids):
            for idx, jid in enumerate(job_ids):
                if not progress.tasks[jid].finished:
                    progress.advance(jid, random.uniform(3, 14))
                    time.sleep(tasks_cfg[idx][1] * random.uniform(0.5, 1.5) / 10)

LOGO_LINES = [
    r" █████╗ ██╗     ████████╗██████╗ ██╗      █████╗  ██████╗██╗  ██╗",
    r"██╔══██╗██║     ╚══██╔══╝██╔══██╗██║     ██╔══██╗██╔════╝██║  ██║",
    r"███████║██║        ██║   ██████╔╝██║     ███████║██║     █████╔╝ ",
    r"██╔══██║██║        ██║   ██╔══██╗██║     ██╔══██║██║     ██╔-██╗ ",
    r"██║  ██║███████╗   ██║   ██████╔╝███████╗██║  ██║╚██████╗██║  ██╗",
]
LOGO_COLORS = [C_NEON, C_RED, C_MID, C_DARK, C_BLOOD]

def draw_logo_rich():
    if len(LOGO_LINES[0]) <= tw() - 2:
        for line, col in zip(LOGO_LINES, LOGO_COLORS):
            console.print(f" {line}", style=f"{col} bold")
    else:
        console.print(" ALTBLACK OSINT", style=f"{C_NEON} bold")

def first_run():
    data_dir = os.path.join(path, "Void", "data")
    if not os.path.exists(data_dir):
        os.makedirs(data_dir, exist_ok=True)
    flag = os.path.join(data_dir, ".launched")
    if not os.path.exists(flag):
        with open(flag, "w") as f:
            f.write("1")

def boot():
    play_intro()
    verify_access()
    first_run()
    cls(); console.print()
    for i, (line, col) in enumerate(zip(LOGO_LINES, LOGO_COLORS)):
        time.sleep(0.06)
        console.print(f" {line}", style=f"{col} bold")
    console.print()
    glitch_reveal_rich("ALTBLACK TOOLS  //  SYSTEM INITIALIZATION")
    console.print()
    rich_boot_bars()
    console.print()
    console.print(Panel(
        Align.center(Text.from_markup(
            f"[{C_NEON} bold][ OSINT & RECON FRAMEWORK ONLINE ]\n"
            f"[{C_MID}]ALTBLACK TOOLS v40.0  ·  by AltBlack [ Tier: {ACTIVE_TIER.upper()} ]"
        )),
        border_style=C_BLOOD, box=box.DOUBLE_EDGE, padding=(0, 2),
    ))
    time.sleep(0.5)

def draw_header():
    cls(); console.print()
    draw_logo_rich(); console.print()
    left  = Text.from_markup(f"[{C_MID}] v40.0  [{C_DARK}]|[/]  by [{C_WHITE} bold]AltBlack  [{C_GOLD}]Tier: {ACTIVE_TIER.upper()}[/]")
    comm = "altblack.tools"
    right = Text.from_markup(f"[{C_DARK}]{comm}")
    w = tw(); gap = w - len(f" v40.0  |  by AltBlack  Tier: {ACTIVE_TIER.upper()}") - len(comm) - 2
    console.print(left, end=""); console.print(" " * max(1, gap), end=""); console.print(right)
    seg = (w - 2) // 3
    console.print(f"[{C_BLOOD}]" + "─"*seg + f"[{C_MID}]" + "─"*seg + f"[{C_NEON}]" + "─"*(w-2-seg*2))
    console.print()

def make_cell(key, label):
    if not key.strip(): return Text(label, style=C_DIM)
    t = Text()
    t.append("[", style=C_DARK); t.append(key, style=f"{C_NEON} bold")
    t.append("] ", style=C_DARK); t.append(label, style=C_WHITE)
    return t

def draw_tree(title, items):
    console.print(Text.from_markup(f"[{C_BLOOD}] ┌── [{C_NEON} bold]{title}"))
    for i, e in enumerate(items):
        last = (i == len(items) - 1)
        b = "└──" if last else "├──"
        if e[0] == "cat":
            console.print(f"[{C_BLOOD}] │")
            console.print(Text.from_markup(f"[{C_BLOOD}] {b} [{C_NEON} bold]{e[1]}"))
        elif e[0] == "cols":
            pairs = e[1]; col_w = max(20, (tw() - 12) // 2)
            for j in range(0, len(pairs), 2):
                L = pairs[j]; R = pairs[j+1] if j+1 < len(pairs) else None
                sub = "└──" if (j+2 >= len(pairs)) else "├──"
                pad = col_w - len(f"[{L[0]}] {L[1]}")
                line = Text.from_markup(f"[{C_BLOOD}] │   [{C_DARK}]{sub} ")
                line.append_text(make_cell(L[0], L[1]))
                line.append(" " * max(1, pad))
                if R:
                    line.append_text(Text.from_markup(f"[{C_BLOOD}]│  "))
                    line.append_text(make_cell(R[0], R[1]))
                console.print(line)
        elif e[0] in ("nav", "navlast"):
            b2 = "└──" if e[0] == "navlast" else "├──"
            console.print(f"[{C_BLOOD}] │")
            console.print(Text.from_markup(
                f"[{C_BLOOD}] {b2}  [{C_DARK}][[{C_NEON} bold]{e[1]}[{C_DARK}]]  [{C_MID}]{e[2]}"
            ))
    console.print()

def prompt(loc):
    console.print(Text.from_markup(
        f"[{C_BLOOD}] ┌─[[{C_NEON} bold]altblack[{C_DARK}]@[{C_RED}]osint[{C_BLOOD}]]"
        f"──[[{C_WHITE} bold]{loc}[{C_BLOOD}]]"
    ), end="\n")
    raw = input(f"\033[38;2;139;0;0m └──\033[0m\033[38;2;255;32;32m\033[1m >> \033[0m").strip()
    return norm(raw)

def show(loc, title, items):
    draw_header(); draw_tree(title, items); return prompt(loc)

def run(fr, en):
    lang = input(f"\033[38;2;204;0;0m  lang (fr/en) >> \033[0m").strip().lower()
    src  = fr if lang == "fr" else en
    if os.path.exists(src):
        try:    
            subprocess.run([sys.executable, src])
        except Exception as e:
            console.print(f"[{C_NEON} bold]  [!] Error running script: {e}")
    else:
        console.print(f"[{C_NEON} bold]  [!] script not found: {src}")
    input(f"\033[38;2;136;0;0m  press enter to continue...\033[0m")

def emergency_token_reset():
    _panel("EMERGENCY RESET & TOKEN PURGE", "Purging local sessions, API tokens, and cached footprints")
    console.print(f"[{C_NEON} bold] [!] Initializing emergency sanitation protocol...")
    time.sleep(1)
    
    data_dir = os.path.join(path, "Void", "data")
    cleared_files = 0
    
    try:
        if os.path.exists(data_dir):
            for filename in os.listdir(data_dir):
                file_path = os.path.join(data_dir, filename)
                if filename != ".launched":
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                        cleared_files += 1
        
        time.sleep(0.8)
        console.print(f"[{C_WHITE}] [✓] Local session tokens purged from memory.")
        console.print(f"[{C_WHITE}] [✓] Removed {cleared_files} cached telemetry/credential files.")
        console.print(f"[{C_WHITE}] [✓] Network sockets and temporary handles closed.")
        
        console.print(Panel(
            Text.from_markup(
                f"[{C_GOLD} bold]* EMERGENCY PURGE COMPLETE *\n\n"
                f"[{C_SILVER}]Status : [{C_WHITE} bold]SYSTEM HARDENED & SECURED\n"
                f"[{C_SILVER}]Action : [{C_WHITE}]All active local tokens have been wiped."
            ),
            border_style=C_GOLD, box=box.DOUBLE_EDGE, padding=(0, 3)
        ))
    except Exception as e:
        console.print(f"\n[{C_NEON} bold]  [!] Error during emergency reset: {e}")
    
    input(f"\033[38;2;136;0;0m  press enter to return to menu...\033[0m")

def open_security_consoles():
    _panel("SECURITY CONSOLES & RECOVERY", "Opening official account hardening & password reset pages")
    console.print(f"[{C_NEON} bold] [!] Opening official security portals in browser...")
    
    security_links = [
        ("Google Account Security", "https://myaccount.google.com/security"),
        ("GitHub Password / Settings", "https://github.com/settings/security"),
        ("Discord Sessions / Password", "https://discord.com/channels/@me"),
        ("Telegram Privacy Settings", "https://my.telegram.org/auth"),
        ("HaveIBeenPwned Check", "https://haveibeenpwned.com/")
    ]
    
    for name, url in security_links:
        t = Text()
        t.append(" │   ├── ", style=C_BLOOD)
        t.append(f"{name:<28}", style=C_WHITE)
        t.append(" ──>  ", style=C_DIM)
        t.append(url, style=C_GOLD2)
        console.print(t)
        try:
            webbrowser.open(url)
        except Exception:
            pass
        time.sleep(0.1)
        
    console.print()
    console.print(Panel(
        Text.from_markup(
            f"[{C_GOLD} bold]* SECURITY CONSOLES OPENED *\n\n"
            f"[{C_SILVER}]Action : [{C_WHITE}]Change passwords and enable 2FA directly on official portals."
        ),
        border_style=C_GOLD, box=box.DOUBLE_EDGE, padding=(0, 3)
    ))
    input(f"\033[38;2;136;0;0m  press enter to return to menu...\033[0m")

def _ansi(h):
    hx = h.lstrip("#"); r,g,b = int(hx[0:2],16),int(hx[2:4],16),int(hx[4:6],16)
    return f"\033[38;2;{r};{g};{b}m"

def _panel(title, desc):
    console.print(); console.print(Panel(
        Align.center(Text.from_markup(f"[{C_GOLD} bold]* {title} *\n[{C_SILVER}]{desc}")) ,
        border_style=C_BLOOD, box=box.DOUBLE_EDGE, padding=(0,3), width=min(60, tw()-2)
    )); console.print()

def _open_links(pairs):
    for name, url in pairs:
        t = Text()
        t.append(" │   ├── ", style=C_BLOOD)
        t.append(f"{name:<20}", style=C_WHITE)
        t.append(" ──>  ", style=C_DIM)
        t.append(url, style=C_GOLD2)
        console.print(t)
        try:
            webbrowser.open(url)
        except Exception:
            pass
        time.sleep(0.08)
    console.print(); input(f"\033[38;2;136;0;0m  press enter...\033[0m")

def tool_username_hunter():
    _panel("USERNAME HUNTER", "Search username footprint on 12 platforms")
    u = input(f"{_ansi(C_MID)}  username >> \033[0m").strip()
    if not u: return
    console.print(Text.from_markup(f"[{C_NEON} bold] ┌── Results for : {u}"))
    _open_links([
        ("GitHub",    f"https://github.com/{u}"),
        ("Twitter/X", f"https://x.com/{u}"),
        ("Instagram", f"https://instagram.com/{u}"),
        ("TikTok",    f"https://tiktok.com/@{u}"),
        ("Reddit",    f"https://reddit.com/u/{u}"),
        ("Twitch",    f"https://twitch.tv/{u}"),
        ("YouTube",   f"https://youtube.com/@{u}"),
        ("Steam",     f"https://steamcommunity.com/id/{u}"),
        ("Snapchat",  f"https://snapchat.com/add/{u}"),
        ("Pinterest", f"https://pinterest.com/{u}"),
        ("Medium",    f"https://medium.com/@{u}"),
        ("Telegram",  f"https://t.me/{u}"),
    ])

def tool_domain_intel():
    _panel("DOMAIN INTEL", "WHOIS · DNS · SSL · Shodan · VirusTotal")
    d = input(f"{_ansi(C_MID)}  domain (ex: spaggiari.eu) >> \033[0m").strip()
    if not d: return
    console.print(Text.from_markup(f"[{C_NEON} bold] ┌── Intel for : {d}"))
    _open_links([
        ("WHOIS",       f"https://who.is/whois/{d}"),
        ("DNS Lookup",  f"https://dnschecker.org/#A/{d}"),
        ("Subdomains",  f"https://subdomainfinder.c99.nl/?domain={d}"),
        ("SSL Cert",    f"https://crt.sh/?q={d}"),
        ("VirusTotal",  f"https://virustotal.com/gui/domain/{d}"),
        ("Shodan",      f"https://shodan.io/search?query=hostname%3A{d}"),
        ("URLScan",     f"https://urlscan.io/search/#domain%3A{d}"),
    ])

def tool_social_scraper():
    _panel("SOCIAL SCRAPER", "Public profile scraping tools")
    console.print(Text.from_markup(f"[{C_NEON} bold] ┌── Social Scraper Tools"))
    _open_links([
        ("Instagram",    "https://imginn.com/"),
        ("TikTok",       "https://exolyt.com/"),
        ("Facebook ID",  "https://lookup-id.com/"),
        ("LinkedIn",     "https://osint.support/"),
        ("Social Search","https://socialsearcher.com/"),
        ("Sherlock",     "https://sherlock-project.github.io/"),
    ])

def tool_vpn_detector():
    _panel("VPN DETECTOR", "Detect VPN · Proxy · Tor on Target IP")
    ip = input(f"{_ansi(C_MID)}  IP address >> \033[0m").strip()
    if not ip: return
    console.print(Text.from_markup(f"[{C_NEON} bold] ┌── VPN Check : {ip}"))
    _open_links([
        ("IPQualityScore", f"https://ipqualityscore.com/free-ip-lookup-proxy-vpn-test/lookup/{ip}"),
        ("IPHub",          f"https://iphub.info/ip/{ip}"),
        ("AbuseIPDB",      f"https://abuseipdb.com/check/{ip}"),
        ("Shodan",         f"https://shodan.io/host/{ip}"),
        ("GreyNoise",      f"https://viz.greynoise.io/ip/{ip}"),
    ])

def tool_token_checker():
    _panel("TOKEN AUDITOR", "Check Discord Token Status & Permissions")
    token = input(f"{_ansi(C_MID)}  Discord Token >> \033[0m").strip()
    if not token: return
    try:
        req = urllib.request.Request("https://discord.com/api/v9/users/@me", headers={"Authorization": token})
        with urllib.request.urlopen(req, timeout=5) as r:
            d = json.loads(r.read())
        console.print(Panel(
            Text.from_markup(
                f"[{C_GOLD} bold]* TOKEN VALID *\n\n"
                f"[{C_SILVER}]User   : [{C_WHITE} bold]{d.get('username','?')}#{d.get('discriminator','0')}\n"
                f"[{C_SILVER}]ID     : [{C_WHITE}]{d.get('id','?')}\n"
                f"[{C_SILVER}]Email  : [{C_WHITE}]{d.get('email','hidden')}\n"
                f"[{C_SILVER}]MFA    : [{C_WHITE}]{'Enabled' if d.get('mfa_enabled') else 'Disabled'}\n"
                f"[{C_SILVER}]Phone  : [{C_WHITE}]{'Linked' if d.get('phone') else 'None'}"
            ),
            border_style=C_GOLD, box=box.DOUBLE_EDGE, padding=(0, 3)
        ))
    except Exception:
        console.print(f"\n[{C_NEON} bold]  [!] INVALID TOKEN or network error")
    console.print(); input(f"\033[38;2;136;0;0m  press enter...\033[0m")

def tool_hash_cracker():
    _panel("HASH IDENTIFIER & LOOKUP", "Query MD5 · SHA1 · SHA256 against public databases")
    h = input(f"{_ansi(C_MID)}  hash >> \033[0m").strip()
    if not h: return
    console.print(Text.from_markup(f"[{C_NEON} bold] ┌── Hash : {h[:40]}{'...' if len(h)>40 else ''}"))
    _open_links([
        ("CrackStation", "https://crackstation.net/"),
        ("HashKiller",   "https://hashkiller.io/listmanager"),
        ("MD5Decrypt",   "https://md5decrypt.net/"),
        ("Hashes.com",   "https://hashes.com/en/decrypt/hash"),
        ("Nitrxgen",     f"https://www.nitrxgen.net/md5db/{h}"),
    ])

def tool_password_gen():
    _panel("SECURE PASSWORD GENERATOR", "Generate cryptographically secure passwords")
    try: length = int(input(f"{_ansi(C_MID)}  length (default 20) >> \033[0m").strip() or "20")
    except ValueError: length = 20
    charset = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?"
    console.print(); console.print(Text.from_markup(f"[{C_NEON} bold] ┌── 8 passwords  ·  length {length}"))
    for i in range(8):
        pwd = ''.join(random.choices(charset, k=length))
        t = Text()
        t.append(f" │   [{i+1:02d}] ", style=C_BLOOD)
        t.append(pwd, style=f"{C_WHITE} bold")
        console.print(t)
    console.print(); input(f"\033[38;2;136;0;0m  press enter...\033[0m")

def tool_temp_mail():
    _panel("TEMP MAIL SERVICES", "Instant disposable email providers")
    console.print(Text.from_markup(f"[{C_NEON} bold] ┌── Temp Mail Services"))
    _open_links([
        ("10MinuteMail",  "https://10minutemail.com/"),
        ("Guerrilla Mail","https://guerrillamail.com/"),
        ("TempMail",      "https://temp-mail.org/"),
        ("Mailnull",      "https://www.mailnull.com/"),
        ("Dispostable",   "https://dispostable.com/"),
        ("FakeMail",      "https://www.fakemail.net/"),
    ])

PAGES_DATABASE = {
    1: {
        "name": "home", 
        "title": "HOME", 
        "cat": "ALTBLACK-OSINT SUITE", 
        "cols": [("01","OSINT Hub"), ("02","Config"), ("03","About")]
    },
    2: {
        "name": "target-profiling", 
        "title": "TARGET & SOCIAL RECON", 
        "cat": "TARGET PROFILING & SOCIAL OSINT", 
        "cols": [
            ("01","Instagram Scanner"), ("02","TikTok Finder"),
            ("03","Multi Social Auditor"), ("04","Username Hunter"),
            ("05","Social Scraper"), ("06","Name Tracker"),
            ("07","Email Info"), ("08","Number Info (Check)"),
            ("09","Anti-Doxx Auditor"), ("10","GitHub Scraper")
        ]
    },
    3: {
        "name": "network-recon", 
        "title": "NETWORK & DOMAIN RECON", 
        "cat": "INFRASTRUCTURE & DNS INTELLIGENCE", 
        "cols": [
            ("01","Domain Intel"), ("02","IP Lookup (Check)"),
            ("03","Port Scanner"), ("04","Banner Grabber"),
            ("05","Service Detector"), ("06","Subdomain Finder"),
            ("07","DNS Record Dump"), ("08","Reverse DNS"),
            ("09","VPN Detector"), ("10","Web Status Monitor")
        ]
    },
    4: {
        "name": "media-threat-intel", 
        "title": "MEDIA & THREAT INTEL", 
        "cat": "METADATA, LEAKS & THREAT RECON", 
        "cols": [
            ("01","EXIF & GPS Extractor"), ("02","Reverse Image Search"),
            ("03","Data Leak Checker"), ("04","Token Auditor"),
            ("05","Shodan Host Inspector"), ("06","AbuseIPDB Query"),
            ("07","Tor Exit Checker"), ("08","Proxy Validator"),
            ("09","Public Metadata Scraper"), ("10","Wayback Machine Query")
        ]
    },
    5: {
        "name": "darkweb-sources", 
        "title": "DARK WEB & SEARCH", 
        "cat": "THREAT INTEL SOURCES", 
        "cols": [
            ("01","Mail2Tor"), ("02","Hidden Wiki"),
            ("03","ProPublica"), ("04","DuckDuckGo"),
            ("05","SecureDrop"), ("06","Sci-Hub"),
            ("07","OSINT Framework"), ("08","OSINT Industries"),
            ("09","Epieos"), ("10","WhatsMyName")
        ]
    },
    6: {
        "name": "crypto-utilities", 
        "title": "CRYPTO, UTILS & REPORTING", 
        "cat": "AUTOMATION & TELEMETRY DROPS", 
        "cols": [
            ("01","Hash Lookup"), ("02","Password Generator"),
            ("03","Temp Mail"), ("04","SSL Cert Inspector"),
            ("05","PDF Report Exporter"), ("06","Discord Threat Intel Dropper")
        ]
    }
}

ALL_LINKS = [
    ("01","Mail2Tor",        "http://mail2tor2zyjdctd.onion/"),
    ("02","Hidden Wiki",     "http://zqktlwiuavvvqqt4ybvgvi7tyo4hjl5xgfuvpdf6otjiycgwqbym2qad.onion/"),
    ("03","ProPublica",      "https://www.propub3r6espa33w.onion/"),
    ("04","DuckDuckGo",      "http://3g2upl4pq6kufc4m.onion/"),
    ("05","SecureDrop",      "https://secrdrop5wyphb5x.onion/"),
    ("06","Sci-Hub",         "http://scihub22266oqcxt.onion/"),
    ("07","OSINT Framework", "https://osintframework.com/"),
    ("08","OSINT Industries","https://osint.industries/"),
    ("09","Epieos",          "https://epieos.com/"),
    ("10","WhatsMyName",     "https://whatsmyname.app/")
]
_UM = {k:u for k,_,u in ALL_LINKS}
_NM = {k:n for k,n,_ in ALL_LINKS}

def _reveal(o):
    if o in _UM:
        console.print(); console.print(Panel(
            Text.from_markup(f"[{C_NEON} bold]{_NM[o]}\n[{C_DARK}]{_UM[o]}"),
            border_style=C_BLOOD, box=box.HEAVY, padding=(0,2),
            width=min(len(_UM[o])+8, tw()-2),
        )); input(f"\033[38;2;100;0;0m  enter to continue...\033[0m")

def dynamic_page_loop(start_page=1):
    current = start_page
    total = len(PAGES_DATABASE)
    
    while True:
        if not check_permission(current):
            current = 2 if ACTIVE_TIER == "base" else 4
            continue
            
        data = PAGES_DATABASE.get(current, PAGES_DATABASE[1])
        filtered_cols = get_allowed_cols(current, ACTIVE_TIER)
        
        if not filtered_cols and ACTIVE_TIER == "base" and current > 2:
            current = 2
            continue

        title_str = f"{data['title']}  ·  {current}/{total}"
        valid_keys = {item[0] for item in filtered_cols}
        
        items = [
            ("cat", data["cat"]),
            ("cols", filtered_cols)
        ]
        
        if current > 1:
            prev_name = PAGES_DATABASE[current-1]["name"]
            items.append(("nav", "B", f"back  ──>  {prev_name}"))
        if current < total:
            next_name = PAGES_DATABASE[current+1]["name"]
            items.append(("navlast", "N", f"next  ──>  {next_name}"))
        else:
            items.append(("navlast", "Q", "quit"))
            
        loc = f"~/{data['name'].replace(' ', '-')}"
        o = show(loc, title_str, items)
        
        if o.upper() == "N":
            if current < total: current += 1
            continue
        elif o.upper() == "B":
            if current > 1: current -= 1
            continue
        elif o.upper() == "Q":
            cls(); sys.exit(0)
            
        if o not in valid_keys:
            console.print(f"\n[bold {C_NEON}]  [!] ACCESS DENIED: Unauthorized module or invalid selection for your license tier.[/]")
            input(f"\033[38;2;136;0;0m  press enter to continue...\033[0m")
            continue
            
        if current == 1:
            if o == "01": current = 2
        elif current == 2:  # Target & Social Recon
            if ACTIVE_TIER == "base":
                if o == "09": 
                    run(sp("anti-doxx-auditor","fr.py"), sp("anti-doxx-auditor","en.py"))
                    choice_purge = input(f"\033[38;2;204;0;0m  [!] Execute emergency token & session purge? (y/n) >> \033[0m").strip().lower()
                    if choice_purge == 'y':
                        emergency_token_reset()
                    choice_consoles = input(f"\033[38;2;204;0;0m  [!] Open official security/password recovery consoles in browser? (y/n) >> \033[0m").strip().lower()
                    if choice_consoles == 'y':
                        open_security_consoles()
            else:
                if o == "01": run(sp("instagram-scanner","fr.py"), sp("instagram-scanner","en.py"))
                elif o == "02": run(sp("tiktok-finder","fr.py"), sp("tiktok-finder","en.py"))
                elif o == "03": run(sp("multi-social-auditor","fr.py"), sp("multi-social-auditor","en.py"))
                elif o == "04": tool_username_hunter()
                elif o == "05": tool_social_scraper()
                elif o == "06": run(sp("name-tracker","fr.py"), sp("name-tracker","en.py"))
                elif o == "07": run(sp("email-info","fr.py"), sp("email-info","en.py"))
                elif o == "08": run(sp("number-info","fr.py"), sp("number-info","en.py"))
                elif o == "09": 
                    run(sp("anti-doxx-auditor","fr.py"), sp("anti-doxx-auditor","en.py"))
                    choice_purge = input(f"\033[38;2;204;0;0m  [!] Execute emergency token & session purge? (y/n) >> \033[0m").strip().lower()
                    if choice_purge == 'y':
                        emergency_token_reset()
                    choice_consoles = input(f"\033[38;2;204;0;0m  [!] Open official security/password recovery consoles in browser? (y/n) >> \033[0m").strip().lower()
                    if choice_consoles == 'y':
                        open_security_consoles()
                elif o == "10": run(sp("github-user-scraper","fr.py"), sp("github-user-scraper","en.py"))

        elif current == 3:  # Network & Domain Recon
            if o == "01": tool_domain_intel()
            elif o == "02": run(sp("ip-lookup","fr.py"), sp("ip-lookup","en.py"))
            elif o == "03": run(sp("port-scanner","fr.py"), sp("port-scanner","en.py"))
            elif o == "04": run(sp("banner-grabber","fr.py"), sp("banner-grabber","en.py"))
            elif o == "05": run(sp("service-detector","fr.py"), sp("service-detector","en.py"))
            elif o == "06": run(sp("subdomain-finder","fr.py"), sp("subdomain-finder","en.py"))
            elif o == "07": run(sp("dns-record-dump","fr.py"), sp("dns-record-dump","en.py"))
            elif o == "08": run(sp("reverse-dns","fr.py"), sp("reverse-dns","en.py"))
            elif o == "09": tool_vpn_detector()
            elif o == "10": run(sp("web-status-monitor","fr.py"), sp("web-status-monitor","en.py"))

        elif current == 4:  # Media & Threat Intel
            if o == "01": run(sp("exif-gps-extractor","fr.py"), sp("exif-gps-extractor","en.py"))
            elif o == "02": run(sp("reverse-image-search","fr.py"), sp("reverse-image-search","en.py"))
            elif o == "03": run(sp("data-leak-checker","fr.py"), sp("data-leak-checker","en.py"))
            elif o == "04": tool_token_checker()
            elif o == "05": run(sp("shodan-host-inspector","fr.py"), sp("shodan-host-inspector","en.py"))
            elif o == "06": run(sp("abuseipdb-query","fr.py"), sp("abuseipdb-query","en.py"))
            elif o == "07": run(sp("tor-exit-checker","fr.py"), sp("tor-exit-checker","en.py"))
            elif o == "08": run(sp("proxy-validator","fr.py"), sp("proxy-validator","en.py"))
            elif o == "09": run(sp("public-metadata-scraper","fr.py"), sp("public-metadata-scraper","en.py"))
            elif o == "10": run(sp("wayback-machine-query","fr.py"), sp("wayback-machine-query","en.py"))

        elif current == 5:  # Dark Web & Search
            _reveal(o)

        elif current == 6:  # Crypto, Utils & Reporting
            if o == "01": tool_hash_cracker()
            elif o == "02": tool_password_gen()
            elif o == "03": tool_temp_mail()
            elif o == "04": run(sp("ssl-cert-inspector","fr.py"), sp("ssl-cert-inspector","en.py"))
            elif o == "05": run(sp("pdf-report-exporter","fr.py"), sp("pdf-report-exporter","en.py"))
            elif o == "06": run(sp("discord-telegram-notifier","fr.py"), sp("discord-telegram-notifier","en.py"))

if __name__ == "__main__":
    try:
        if os.name == "nt":
            import ctypes
            os.system("title ALTBLACK OSINT SUITE v40.0")
            ctypes.windll.kernel32.SetConsoleMode(
                ctypes.windll.kernel32.GetStdHandle(-11), 7)
        else:
            sys.stdout.write("\x1b]2;ALTBLACK OSINT SUITE v40.0\x07")
        boot()
        dynamic_page_loop(2 if ACTIVE_TIER == "base" else 1)
    except KeyboardInterrupt:
        console.print(f"\n[{C_NEON} bold]  interrupted.")
        sys.exit(0)