# ---------- Importation des modules ----------

import requests
from pystyle import Colors

# ---------- Style du programme ----------

style = f"[{Colors.blue}+{Colors.reset}] "

# Programme pour check les proxies socks 5 ----------

def check_socks5(_proxy: str) -> bool:
    proxy = {"https": f"socks5://{_proxy}"}
    try:
        requests.get("https://google.com/", proxies=proxy, timeout=5)
        v = True
    except:
        v = False
    if v:
        with open("valid_socks5.txt", 'a') as f:
            f.write(_proxy)
    else: pass

def check_socks4(_proxy: str) -> bool:
    proxy = {"https": f"socks4://{_proxy}"}
    try:
        requests.get("https://api.ipify.org/", proxies=proxy, timeout=5)
        v = True
    except:
        v = False
    if v:
        with open("valid_socks4.txt", 'a') as f:
            f.write(_proxy)
    else: pass