import requests
import os
import time
import threading
from random import choice

class Fore:
    RESET   = '\033[39m'
    BLACK   = '\033[90m'
    RED     = '\033[91m'
    GREEN   = '\033[92m'
    YELLOW  = '\033[93m'
    BLUE    = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN    = '\033[96m'
    WHITE   = '\033[97m'
    UI1     = '\033[37m'
    UI2     = '\033[90m'

UI = f'''
{Fore.UI1}                                                  ╦═╗╔═╗╔╗ ╦  ╔═╗═╗ ╦
{Fore.UI2}                                                  ╠╦╝║ ║╠╩╗║  ║ ║╔╩╦╝
{Fore.RED}                                                  ╩╚═╚═╝╚═╝╩═╝╚═╝╩ ╚═{Fore.RESET}
'''

lock = threading.Lock()
followed = 0
failed = 0
retries = 0

class Roblox:
    def BypassXToken(cookie):
        headers={
            'cookie': f'.ROBLOSECURITY={cookie}',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
        }
        r = requests.get('https://www.roblox.com/home', headers=headers)
        if "Roblox.XsrfToken.setToken" in r.text:
            token = r.text.split("Roblox.XsrfToken.setToken('")[1].split("');")[0]
        return token

class Proxy:
    def Follow(cookie, user_id):
        global followed, failed, retries
        try:
            headers={
                'cookie': f'.ROBLOSECURITY={cookie}',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
                'x-csrf-token': Roblox.BypassXToken(cookie)
            }
            r = requests.post(f'https://friends.roblox.com/v1/users/{user_id}/follow', headers=headers, proxies={'https': 'http://%s' % (choice(proxies))}, timeout=4)
            if '"success":true' in r.text:
                print(f'{Fore.GREEN}[{Fore.RESET}SUCCESS{Fore.GREEN}]{Fore.RESET} Followed: {user_id}')
                followed += 1
                os.system(f'title [xRoblox] By Dropout ^| Followed: {followed} ^| Failed: {failed} ^| Retries: {retries}')
            elif 'Authorization has been denied for this request.' in r.text:
                lock.acquire()
                failed += 1
                os.system(f'title [xRoblox] By Dropout ^| Followed: {followed} ^| Failed: {failed} ^| Retries: {retries}')
            elif 'TooManyRequests' in r.text:
                Proxy.Follow(cookie, user_id)
                retries += 1
                os.system(f'title [xRoblox] By Dropout ^| Followed: {followed} ^| Failed: {failed} ^| Retries: {retries}')
            else:
                pass
        except:
            retries += 1
            os.system(f'title [xRoblox] By Dropout ^| Followed: {followed} ^| Failed: {failed} ^| Retries: {retries}')
            Proxy.Follow(cookie, user_id)

class Proxyless:
    def Follow(cookie, user_id):
        global followed, failed, retries
        try:
            headers={
                'cookie': f'.ROBLOSECURITY={cookie}',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
                'x-csrf-token': Roblox.BypassXToken(cookie)
            }
            r = requests.post(f'https://friends.roblox.com/v1/users/{user_id}/follow', headers=headers)
            if '"success":true' in r.text:
                print(f'{Fore.GREEN}[{Fore.RESET}SUCCESS{Fore.GREEN}]{Fore.RESET} Followed: {user_id}')
                followed += 1
                os.system(f'title [xRoblox] By Dropout ^| Followed: {followed} ^| Failed: {failed} ^| Retries: {retries}')
            elif 'Authorization has been denied for this request.' in r.text:
                lock.acquire()
                failed += 1
                os.system(f'title [xRoblox] By Dropout ^| Followed: {followed} ^| Failed: {failed} ^| Retries: {retries}')
            elif 'TooManyRequests' in r.text:
                Proxyless.Follow(cookie, user_id)
                retries += 1
                os.system(f'title [xRoblox] By Dropout ^| Followed: {followed} ^| Failed: {failed} ^| Retries: {retries}')
            else:
                lock.acquire()
                failed += 1
                os.system(f'title [xRoblox] By Dropout ^| Followed: {followed} ^| Failed: {failed} ^| Retries: {retries}')
        except:
            retries += 1
            os.system(f'title [xRoblox] By Dropout ^| Followed: {followed} ^| Failed: {failed} ^| Retries: {retries}')
            Proxyless.Follow(cookie, user_id)

def Main():
    global followed, failed, retries
    os.system('cls & title [Roblox] By Dropout ^| Main Menu')
    print(UI + f'''
        {Fore.RED} ╔═════════════════════════════════╗╔═════════════════════════════════╗╔═════════════════════════════════╗
        {Fore.RED} ║{Fore.RED}[{Fore.RESET}1{Fore.RED}]{Fore.RESET} Follow Bot                  {Fore.RED} ║║{Fore.RED}[{Fore.RESET}5{Fore.RED}]{Fore.RESET} Comming Soon                {Fore.RED} ║║{Fore.RED}[{Fore.RESET}9 {Fore.RED}]{Fore.RESET} Comming Soon               {Fore.RED} ║
        {Fore.RED} ║{Fore.RED}[{Fore.RESET}2{Fore.RED}]{Fore.RESET} Comming Soon                {Fore.RED} ║║{Fore.RED}[{Fore.RESET}6{Fore.RED}]{Fore.RESET} Comming Soon                {Fore.RED} ║║{Fore.RED}[{Fore.RESET}10{Fore.RED}]{Fore.RESET} Comming Soon               {Fore.RED} ║
        {Fore.RED} ║{Fore.RED}[{Fore.RESET}3{Fore.RED}]{Fore.RESET} Comming Soon                {Fore.RED} ║║{Fore.RED}[{Fore.RESET}7{Fore.RED}]{Fore.RESET} Comming Soon                {Fore.RED} ║║{Fore.RED}[{Fore.RESET}11{Fore.RED}]{Fore.RESET} Comming Soon               {Fore.RED} ║
        {Fore.RED} ║{Fore.RED}[{Fore.RESET}4{Fore.RED}]{Fore.RESET} Comming Soon                {Fore.RED} ║║{Fore.RED}[{Fore.RESET}8{Fore.RED}]{Fore.RESET} Comming Soon                {Fore.RED} ║║{Fore.RED}[{Fore.RESET}12{Fore.RED}]{Fore.RESET} Exit                       {Fore.RED} ║
        {Fore.RED} ╚═════════════════════════════════╝╚═════════════════════════════════╝╚═════════════════════════════════╝
''')
    option = input(f'{Fore.RED}>{Fore.RESET} ')
    if option == '1':
        followed = 0
        failed = 0
        retries = 0
        os.system('cls & title [Roblox] By Dropout ^| Follow Bot')
        num = 0
        user_id = input(UI + f'{Fore.RED}>{Fore.RESET} User ID{Fore.RED}:{Fore.RESET} ')
        os.system('cls & title [Roblox] By Dropout ^| Follow Bot')
        proxy_choice = input(UI + f'{Fore.RED}[{Fore.RESET}1{Fore.RED}]{Fore.RESET} Proxyless\n{Fore.RED}[{Fore.RESET}2{Fore.RED}]{Fore.RESET} Proxys From API\n\n{Fore.RED}>{Fore.RESET} ')
        if proxy_choice == '1':
            print()
            while True:
                try:
                    if threading.active_count() <= len(cookies):
                        threading.Thread(target=Proxyless.Follow, args=(cookies[num], user_id)).start()
                        num += 1
                except IndexError:
                    break
            print(f'\n{Fore.RED}>{Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] To Return To The Main Menu. . .')
            os.system('pause >NUL')
            Main()
        elif proxy_choice == '2':
            print()
            while True:
                try:
                    if threading.active_count() <= len(cookies):
                        threading.Thread(target=Proxy.Follow, args=(cookies[num], user_id)).start()
                        num += 1
                except IndexError:
                    break
            print(f'\n{Fore.RED}>{Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] To Return To The Main Menu. . .')
            os.system('pause >NUL')
            Main()

if __name__ == "__main__":
    proxies = []
    os.system('cls & title [Roblox] By Dropout ^| Loading Proxies. . .')
    print(UI + f'[{Fore.RED}Roblox{Fore.RESET}] Loading Proxies. . .')
    all_proxies = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=1000&country=all&ssl=all&anonymity=all').text
    for proxy in all_proxies.splitlines():
        proxies.append(proxy)
    cookies = []
    os.system('cls & title [Roblox] By Dropout ^| Loading Cookies. . .')
    print(UI + f'[{Fore.RED}Roblox{Fore.RESET}] Loading Cookies. . .')
    with open('Cookies.txt', "r") as RobloxSecurity: 
        for line in RobloxSecurity:
            cookie = line.replace('\n', '')
            cookies.append(cookie)
    time.sleep(1)
    Main()
