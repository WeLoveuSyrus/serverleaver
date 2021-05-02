import requests
import threading
from colorama import Fore
from colored import fg, attr

class colors:

    red = fg('#ff004d8')
    reset = attr('reset')
    gray = fg('#ff4b00')
    gray = fg('#ff4b00')

print(f'''

                                             {Fore.LIGHTBLACK_EX}█████{colors.gray}╗ {Fore.LIGHTBLACK_EX}██████{colors.gray}╗  {Fore.LIGHTBLACK_EX}██████{colors.gray}╗  {Fore.LIGHTBLACK_EX}██████{colors.gray}╗ 
                                            {Fore.LIGHTBLACK_EX}██{colors.gray}╔══{Fore.LIGHTBLACK_EX}██{colors.gray}╗╚════{Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╔═{Fore.LIGHTBLACK_EX}████{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╔═{Fore.LIGHTBLACK_EX}████{colors.gray}╗
                                            {Fore.LIGHTBLACK_EX}{colors.gray}╚{Fore.LIGHTBLACK_EX}█████{colors.gray}╔╝{Fore.LIGHTBLACK_EX} █████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║
                                            {Fore.LIGHTBLACK_EX}{Fore.LIGHTBLACK_EX}██{colors.gray}╔══{Fore.LIGHTBLACK_EX}██{colors.gray}╗ ╚═══{Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║
                                            {Fore.LIGHTBLACK_EX}{colors.gray}╚{Fore.LIGHTBLACK_EX}█████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝
                                             {colors.gray}╚════╝ ╚═════╝  ╚═════╝  ╚═════╝ 
                                       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
                                         ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  
''')

def leave(guild_id, token):
   r = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild_id}", headers={"Authorization": token})
   if r.status_code == 204 or 200:
     print(f"left {guild_id}")

def get_all_guilds(token) -> list():
   servers = []
   r = requests.get("https://discord.com/api/v9/users/@me/guilds", headers={"Authorization": token})
   for guild in r.json():
    servers.append(guild["id"])
   return servers

def start():
   token = input(f"Token: ")
   guilds = get_all_guilds(token)
   for guild in guilds:
       threading.Thread(target=leave, args=(guild, token,)).start()

start()