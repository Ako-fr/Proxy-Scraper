#   ---------- Importation des fichiers ----------


from check_socks import check_socks4, check_socks5
from proxy_download import scrape_socks4, scrape_socks5; scrape_socks5



#   ---------- Importation des modules ----------

from os import system, name
try:
    
    from pystyle import Colorate, Colors, Center, Write
    from threading import Thread
    from time import sleep
except:
    print("[!] Des modules ne sont pas installer, appuyez sur 'entrer' pour les installer.")
    input()
    system("pip install -r requirements.txt")


#    ---------- Liste des sites pour scrape les proxies ----------

socksQ = ['socks4', 'socks5']
sock = ['https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all', 'https://www.proxy-list.download/api/v1/get?type=socks4', 'https://www.proxyscan.io/download?type=socks4', 'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt' ], ['http://spys.me/proxy.txt","%ip%:%port% '], ["http://www.httptunnel.ge/ProxyListForFree.aspx"," target=\"_new\">%ip%:%port%</a>"], ["https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.json", "\"ip\":\"%ip%\",\"port\":\"%port%\","], ["https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list", '"host": "%ip%".*?"country": "(.*?){2}",.*?"port": %port%'], ['https://www.freeproxychecker.com/result/socks4_proxies.txt', "%ip%:%port%"], ['https://www.my-proxy.com/free-socks-4-proxy.html', '%ip%:%port%'], 
socks = ['https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&simplified=true', 'https://www.proxy-list.download/api/v1/get?type=socks5', 'https://www.proxyscan.io/download?type=socks5', 'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt'], ['http://spys.me/proxy.txt","%ip%:%port% '], ["http://www.httptunnel.ge/ProxyListForFree.aspx"," target=\"_new\">%ip%:%port%</a>"], ["https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.json", "\"ip\":\"%ip%\",\"port\":\"%port%\","], ["https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt", '%ip%:%port% (.*?){2}-.-S \\+'], ["https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt", "%ip%:%port%"], ['https://www.my-proxy.com/free-socks-5-proxy.html','%ip%:%port%'],


#   ---------- Ascii art du programme ----------

style = f"[{Colors.blue}+{Colors.reset}] "

main_banner = """
   _____                                  _____                     
  / ____|                                |  __ \                    
 | (___   ___ _ __ __ _ _ __   ___ _ __  | |__) | __ _____  ___   _ 
  \___ \ / __| '__/ _` | '_ \ / _ \ '__| |  ___/ '__/ _ \ \/ / | | |
  ____) | (__| | | (_| | |_) |  __/ |    | |   | | | (_) >  <| |_| |
 |_____/ \___|_|  \__,_| .__/ \___|_|    |_|   |_|  \___/_/\_\\\__, |
                       | |                                     __/ |  Devlopped by Ako
                       |_|                                    |___/   github.com/Ako-fr
                       
                    
            ╔═════════════════════════════════════════════════════════╗
            ║                                                         ║
            ║               [1] - Installation Proxy                  ║
            ║               [2] - Verification Proxy                  ║
            ║               [q] - Quitter le programme                ║
            ║                                                         ║
            ╚═════════════════════════════════════════════════════════╝


"""

dl_banner = """
                     _____                       _____                      _                 _           
                    |  __ \                     |  __ \                    | |               | |          
                    | |__) | __ _____  ___   _  | |  | | _____      ___ __ | | ___   __ _  __| | ___ _ __ 
                    |  ___/ '__/ _ \ \/ / | | | | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
                    | |   | | | (_) >  <| |_| | | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
                    |_|   |_|  \___/_/\_\\\__, | |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   
                                         __/ |                                                           
                                        |___/                                                                                 
                        
                            ╔═════════════════════════════════════════════════════════╗
                            ║                                                         ║
                            ║               [1] - Installation Socks 4                ║
                            ║               [2] - Installation Socks 5                ║
                            ║               [b] - Retourner au menu                   ║
                            ║               [q] - Quitter le programme                ║
                            ║                                                         ║
                            ╚═════════════════════════════════════════════════════════╝                                                     



"""

checker_banner =  """
                     _____                        _____ _               _             
                    |  __ \                      / ____| |             | |            
                    | |__) | __ _____  ___   _  | |    | |__   ___  ___| | _____ _ __ 
                    |  ___/ '__/ _ \ \/ / | | | | |    | '_ \ / _ \/ __| |/ / _ \ '__|
                    | |   | | | (_) >  <| |_| | | |____| | | |  __/ (__|   <  __/ |   
                    |_|   |_|  \___/_/\_\\\__, |  \_____|_| |_|\___|\___|_|\_\___|_|   
                                         __/ |                                       
                                        |___/   https://github.com/Ako-fr   
                                        
                                        
                                    
                            ╔═════════════════════════════════════════════════════════╗
                            ║                                                         ║
                            ║               [1] - Verification Socks 4                ║
                            ║               [2] - Verification Socks 5                ║
                            ║               [b] - Retourner au menu                   ║
                            ║               [q] - Quitter le programme                ║
                            ║                                                         ║
                            ╚═════════════════════════════════════════════════════════╝                                   



"""


#   ---------- Programme ----------

def cls():
    system("cls" if name == 'nt' else "clear")

def main():
    cls()
    print(Colorate.Vertical(Colors.red_to_blue, Center.XCenter(main_banner)))
    
    question = Write.Input("[>] Que voulez-vous faire : ", Colors.white,interval=0.01)
    
    
    def download(): # ---------- Programme pour dowload les proxies ----------
        
        print(Colorate.Vertical(Colors.red_to_blue, Center.XCenter(dl_banner)))
        proxies = Write.Input("[>] Que voulez-vous faire : ", Colors.white ,interval=0.01)
        if proxies == "1":
            scrape_socks4()
            cls()
            download()
        elif proxies == "2":
            scrape_socks5()
            cls()
            download()
        elif proxies == "b":
            cls()
            main()
        elif proxies == 'q':
            exit()
        else: 
            input("[*] Impossible de parvenir a votre demande.")
            cls()
            download()
        
        
        
    def checking(): # ---------- Menu pour check les proxies ----------
        
        print(Colorate.Vertical(Colors.red_to_blue, Center.XCenter(checker_banner)))
        q = Write.Input("[>] Que voulez-vous faire : ", Colors.white ,interval=0.01)
        
        
        if q == '1':
            proxies = open("socks4.txt", "r").readlines()
            for proxy in proxies:
                Thread(target=check_socks4, args=[proxy]).start()
                sleep(0.1)
            a = len(open("valid_socks4.txt").readlines())
            print(style + "Proxy Online : " + str(a))
            input()
            check_socks4()
            cls()
            checking()
            
        elif q == '2':
            proxies = open("socks5.txt", "r").readlines()
            for proxy in proxies:
                Thread(target=check_socks5, args=[proxy]).start()
                sleep(0.1)
            a = len(open("valid_socks5.txt").readlines())
            print(style + "Proxy Online : " + str(a))
            input()
            check_socks5()
            cls()
            checking()
            
        elif q == 'b':
            cls()
            main()
        elif q == 'q':
            exit()
        else:
            input("[*] Impossible de parvenir a votre demande.")
            cls()
            checking()
            
            
#   ---------- Menu pour ce deplacer dans le main ----------

    if question == '1':
        cls()
        download()
    elif question == '2':
        cls()
        checking()
    elif question == 'q':
        exit()
    else:
        input("[*] Impossible de parvenir a votre demande.")
        cls()
        main()
main() 