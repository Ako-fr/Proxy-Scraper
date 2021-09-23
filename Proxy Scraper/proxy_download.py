from requests import get
from pystyle import Colors

style = f"[{Colors.blue}+{Colors.reset}] "
def scrape_socks4():
    url = ['https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all', 'https://www.proxy-list.download/api/v1/get?type=socks4', 'https://www.proxyscan.io/download?type=socks4', 'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt' ]
    for link in url:
        _socks4 = get(link, timeout=5).content.decode().splitlines()
        _socks4 = "\n".join(_socks4)
        with open("socks4.txt", "a") as f:
            f.write(str(_socks4))
    a = len(open("socks4.txt").readlines())
    print(style + "Proxy Download : " + str(a))
    input()

def scrape_socks5():
    url = ['https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&simplified=true', 'https://www.proxy-list.download/api/v1/get?type=socks5', 'https://www.proxyscan.io/download?type=socks5', 'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt']
    for link in url:
        _socks4 = get(link, timeout=5).content.decode().splitlines()
        _socks4 = "\n".join(_socks4)
        with open("socks5.txt", "a") as f:
            f.write(str(_socks4))
    a = len(open("socks5.txt").readlines())
    print(style + "Proxy Download : " + str(a))
    input()
