import urllib.request
import time
import os
import random
import ctypes
import webbrowser

URL = "https://raw.githubusercontent.com/Nadota-cmd/a/refs/heads/main/trigger.txt"

def run_prank():
    if os.name == 'nt':
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)
        os.system('chcp 65001 > nul')
        os.system('cls')
    
    user_name = os.getlogin()
  
    logo = r'''
⣿⠏⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡯⢸⣿
⡏⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢸⣿
    '''
    

    if os.name != 'nt':
        print('\033[92m' + logo + '\033[0m')
    else:
        print(logo)

    print(f"\n[ СИСТЕМНОЕ УВЕДОМЛЕНИЕ ]")
    print(f"gривет, {user_name} если видиш это сообщение значит я смог скачать вирус на твой комп, если хочеш удалить вирус то название файла что я скачал ")
    print("__file__")
    print("код больше к слову ниче не делает") 
    time.sleep(5)
    webbrowser.open("https://youtu.be/ed1oX4jtp4k?si=cmQ7-9RiUzwdAnB-")
if os.name == 'nt':
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

print("Агент Pando запущен...")

while True:
    try:
        no_cache_url = f"{URL}?t={random.random()}"
        
        with urllib.request.urlopen(no_cache_url) as response:
            status = response.read().decode('utf-8').strip()
            
        if status == "1":
            run_prank()
            break 
            
    except Exception:
        pass
    
    time.sleep(30)
