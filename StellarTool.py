#made by Pollulloo
from time import sleep
import os
import subprocess
import sys
import shutil
import getpass
from pystyle import Colors, Colorate, Center 
from colorama import init, Fore, Style
import requests
from bs4 import BeautifulSoup
import time
import threading
import nmap
import base64
import re
import webbrowser
import random
import string
import sqlite3
import json
import random
from datetime import datetime, timedelta
import string
import tkinter as tk
from tkinter import messagebox
import ipaddress
init(autoreset=True) 

os.system('cls' if os.name == 'nt' else 'clear') 
os.system(                        '               title                                      Stellar Tools v1.1             ' if os.name == 'nt' else '')  

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

banner = '''
  ██████ ▄▄▄█████▓▓█████  ██▓     ██▓    ▄▄▄       ██▀███     ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ 
▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██▒    ▓██▒   ▒████▄    ▓██ ▒ ██▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ 
░ ▓██▄   ▒ ▓██░ ▒░▒███   ▒██░    ▒██░   ▒██  ▀█▄  ▓██ ░▄█ ▒   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   
  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██░    ▒██░   ░██▄▄▄▄██ ▒██▀▀█▄     ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒
▒██████▒▒  ▒██▒ ░ ░▒████▒░██████▒░██████▒▓█   ▓██▒░██▓ ▒██▒     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒░▓  ░░ ▒░▓  ░▒▒   ▓▒█░░ ▒▓ ░▒▓░     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
░ ░▒  ░ ░    ░     ░ ░  ░░ ░ ▒  ░░ ░ ▒  ░ ▒   ▒▒ ░  ░▒ ░ ▒░       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
░  ░  ░    ░         ░     ░ ░     ░ ░    ░   ▒     ░░   ░      ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  
      ░              ░  ░    ░  ░    ░  ░     ░  ░   ░                     ░ ░      ░ ░      ░  ░      ░  
                                                                                                          '''

menu_text = '''
     (1)Ip LookUp     │      (5)Tut doxing 
     (2)GitHub        │      (6)Discord Spammer
     (3)Credits       │      (7)Webhook Spammer
     (4)Nitro gen     │      (8)DoxBin
     (10) Coming soon │      (9)Ip Pinger
        '''           

def print_banner(banner):
    lines = banner.splitlines()
    colored_lines = [Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(line)) for line in lines]
    for line in colored_lines:
        print(line)
        sleep(0.10)

def print_menu():
    line = Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(menu_text))
    print(line)

def option1():

    clear_screen()
    header = '''
 ██████╗ ███████╗ ██████╗     ██╗      ██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗ 
██╔════╝ ██╔════╝██╔═══██╗    ██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║   ██║██╔══██╗
██║  ███╗█████╗  ██║   ██║    ██║     ██║   ██║██║   ██║█████╔╝ ██║   ██║██████╔╝
██║   ██║██╔══╝  ██║   ██║    ██║     ██║   ██║██║   ██║██╔═██╗ ██║   ██║██╔═══╝ 
╚██████╔╝███████╗╚██████╔╝    ███████╗╚██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██║     
 ╚═════╝ ╚══════╝ ╚═════╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝     
                                                                                 
    '''
    print(Colorate.Horizontal(Colors.purple_to_blue, header))
    
    prompt = Colorate.Horizontal(Colors.purple_to_blue, "Enter the IP address: ")
    ip_address = input(prompt).strip()
    if not ip_address:
        ip_address = requests.get('https://api.ipify.org').text
    
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        response.raise_for_status()
        data = response.json()
        
        info = f'''
╔══════════════════════════════════════════════════════════╗
║ IP Address: {data.get('ip', 'N/A'):<45}║
║ Hostname: {data.get('hostname', 'N/A'):<46} ║
║ City: {data.get('city', 'N/A'):<50} ║
║ Region: {data.get('region', 'N/A'):<48} ║
║ Country: {data.get('country', 'N/A'):<47} ║
║ Location: {data.get('loc', 'N/A'):<46} ║
╚══════════════════════════════════════════════════════════╝
        '''
        colored_info = Colorate.Horizontal(Colors.purple_to_blue, info)
        print(colored_info)
    except requests.RequestException as e:
        print(Colorate.Horizontal(Colors.purple_to_blue, f"Error: {str(e)}"))
    input("\nPress Enter to return to the main menu...")
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def option5():
    guide_text = '''
Doxxing A Name
---------------------
Using the target’s name is also very helpful. If you have their name then you can possibly find out where they live, what their number is, relatives, etc., which could really be beneficial in a dox. We’re going to be searching the targets on Whitepages and other sites, as a lot of people don’t think to remove their information on Whitepages or simply don’t know how. Their ignorance will be their mistake.

First, go to one of these sites below:
- http://10digits.us (Really good)
- http://thatsthem.com (Also really good)
- http://www.yellowpages.com (Good for just last name and location)
- http://www.whitepages.com (Average)
- http://www.ussearch.com/ (Average)
- http://www.pipl.com/
- http://www.canada411.ca/ (Canadian People)
- http://www.peekyou.com/united_kingdom (UK People)
- http://webmii.com/ (UK People)
- http://www.ratsit.se/BC/SearchPerson.aspx (Swedish People)
- http://www.dgs.dk (Danish People)
- https://find-person-germany.com/ (German People)
- https://www.goyellow.de/ (German People)

Tip: You can probably find a lookup in your area by searching Google for "(enter country here) lookup sites)" and try as many as you can to see which one gives you the best results. The ones I listed are usually accurate and work for the areas they say they’re in. The ones without a specific country beside them are for the US primarily.

Now, we’re going to be using 10digits in the demonstration as it’s my favorite. Make sure you’re on the name tab and enter their first and last name in the first box. In the box on the right, enter their city and state or their zip code. If you want their city and state but have their zip code, there’s a section teaching that below too. Now when you’ve filled out the boxes, press the Search icon, and it’ll display whatever results it finds. I suggest searching through all that pop up if there aren’t too many to see which one is correct. Use this search for example - http://10digits.us/n/Susan_Banks/location/San_Diego%252C_California

There are three results. Click +More on the first one and you’ll receive her address. How hard was that? It’s actually one of the easiest things when doxing.

We can search our target’s number just as we did with the target’s name. There are many sites to use and I’ll list my favorites. I prefer to use 10digits.us as it’s always brought me the best results and never let me down.

First, go to one of the sites below:
- http://www.10digits.us
- http://www.reversemobile.com/index.php
- http://thatsthem.com
- http://www.numberway.com
- http://www.phonenumber.com
- http://www.fonefinder.net
- http://www.whitepages.com
- http://www.pipl.com/
- http://www.canada411.ca/ (Canadian People)
- https://www.goyellow.de/ (German People)
- http://www.dgs.dk (Danish People)

I’m demonstrating 10digits in this example but you can use whatever site you want. Now that we’re on 10digits, click on the Phone button, input their number, and press the Search icon. It’ll display results just like the name search did. You can get the owner’s name, address, state, etc., with just a search.

Tip: Most of the time if it displays multiple results it’s for two adults living in the house.
'''

    colored_text = Colorate.Horizontal(Colors.purple_to_blue, guide_text)
    print(colored_text)
    input("\nPress Enter to return to the previous menu...")

def option2():
 
    guide_text = '''
  /$$$$$$  /$$   /$$     /$$   /$$           /$$      
 /$$__  $$|__/  | $$    | $$  | $$          | $$      
| $$  \__/ /$$ /$$$$$$  | $$  | $$ /$$   /$$| $$$$$$$ 
| $$ /$$$$| $$|_  $$_/  | $$$$$$$$| $$  | $$| $$__  $$
| $$|_  $$| $$  | $$    | $$__  $$| $$  | $$| $$  \ $$
| $$  \ $$| $$  | $$ /$$| $$  | $$| $$  | $$| $$  | $$
|  $$$$$$/| $$  |  $$$$/| $$  | $$|  $$$$$$/| $$$$$$$/
 \______/ |__/   \___/  |__/  |__/ \______/ |_______/



My GitHub : https://github.com/mxssacro
'''

    colored_text = Colorate.Horizontal(Colors.purple_to_blue, guide_text)
    print(colored_text)
    input("\nPress Enter to return to the previous menu...")

def option3():

    guide_text = '''
 ▄▄· ▄▄▄  ▄▄▄ .·▄▄▄▄  ▪  ▄▄▄▄▄.▄▄ · 
▐█ ▌▪▀▄ █·▀▄.▀·██▪ ██ ██ •██  ▐█ ▀. 
██ ▄▄▐▀▀▄ ▐▀▀▪▄▐█· ▐█▌▐█· ▐█.▪▄▀▀▀█▄
▐███▌▐█•█▌▐█▄▄▌██. ██ ▐█▌ ▐█▌·▐█▄▪▐█
·▀▀▀ .▀  ▀ ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀  ▀▀▀▀ 



Credits : Discord @r4nd0mn1
          Telegram @Sparlaree
          Server Discord : https://discord.gg/xRyJeCVv
    
    '''
    
    colored_text = Colorate.Horizontal(Colors.purple_to_blue, guide_text)
    print(colored_text)
    input("\nPress Enter to return to the previous menu...")

def option7():

    
    clear_screen()
    header = '''

██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗    ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝    ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝     ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗     ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗    ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║  
                                                                                 
    '''
    print(Colorate.Horizontal(Colors.purple_to_blue, header))
    
    webhook = input(Colorate.Horizontal(Colors.purple_to_blue, 'Enter the webhook URL: '))

    try:
        response = requests.head(webhook)
        if response.status_code != 200:
            raise ValueError('Invalid webhook URL')
    except:
        print(Colorate.Horizontal(Colors.purple_to_blue, '''
        ERROR : The webhook probably might not be real or not working.
        '''))
        input("Press Enter to return to the menu...")
        return

    message = input(Colorate.Horizontal(Colors.red_to_blue, 'Enter the message to send: '))
    count = int(input(Colorate.Horizontal(Colors.red_to_blue, 'Enter the number of times to send the message: ')))

    print(Colorate.Horizontal(Colors.purple_to_blue, '''
    Connecting to the webhook.. 
    '''))

    for i in range(1, count + 1):
        try:
            response = requests.post(webhook, json={"content": message})
            if response.status_code != 204:
                raise ValueError('Failed to connect to the webhook')
            print(Colorate.Horizontal(Colors.purple_to_blue, f'[!] Connection up. Sending message... {i}/{count}'))
        except:
            print(Colorate.Horizontal(Colors.purple_to_blue, '''
            Error: Failed to connect to the webhook. The webhook might not be real.
            '''))
            input("Press Enter to return to the menu...")
            return

    print(Colorate.Horizontal(Colors.red_to_blue, '''
    Message sent sucesfully!!
    '''))

    input("Press Enter to return")


def option6():
    clear_screen()  
    

    banner = """
  ┌───────────────────────────────────────────────────────┐                                                          
  │  ██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗  │    
  │  ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗ │    
  │  ██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║ │    
  │  ██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║ │    
  │  ██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝ │    
  │  ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝  │     
┌─┘───────────────────────────────────────────────────────┘─────────┐                                                             
│  ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗    │
│  ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗   │
│  ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝   │
│  ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗   │
│  ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║   │
│  ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝   │
└───────────────────────────────────────────────────────────────────┘                                                              
    """

    print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(banner)))

    token = input('Enter Token: ')
    channel_id = input('Enter Channel ID: ')
    message_content = input('Enter Message: ')
    repeat_count = int(input('Enter Repeat Count (How many times): '))

    def spammer():
        url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
        headers = {'Authorization': token}
        payload = {'content': message_content}

        for _ in range(repeat_count):
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 204:
                print(f'Message sent successfully!')
            else:
                print(f'Failed to send message. Status code: {response.status_code}')

    thread = threading.Thread(target=spammer)
    thread.start()
    thread.join()
        
    colored_info = Colorate.Horizontal(Colors.purple_to_blue, spammer)
    print(colored_info)
    print(Colorate.Horizontal(Colors.purple_to_blue, f"Error"))
    input("\nPress Enter to return to the main menu...")
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_nitro_code():

    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
    return f'https://discord.gift/{code}'

def option4():
    clear_screen()

    banner = '''
███╗   ██╗██╗████████╗██████╗  ██████╗      ██████╗ ██████╗ ██████╗ ███████╗
████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗    ██╔════╝██╔═══██╗██╔══██╗██╔════╝
██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║    ██║     ██║   ██║██║  ██║█████╗  
██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║    ██║     ██║   ██║██║  ██║██╔══╝  
██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝    ╚██████╗╚██████╔╝██████╔╝███████╗
╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝      ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
'''

    print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(banner)))

    try:
        num_codes = int(input("Enter the number of Nitro codes to generate: "))
        for _ in range(num_codes):
            nitro_code = generate_nitro_code() 
            print(Fore.LIGHTBLUE_EX+ nitro_code)
        print(Fore.LIGHTBLUE_EX + "-" + "-" * 35 + "-")
    except Exception as e:
        print(f"An error occurred: {e}")
    input("Press Enter to return ")

def option8():
    clear_screen()

    banner = '''
                                                                                                                                                                                                                                                                      
 ██████████      ███████    █████ █████ ███████████  █████ ██████   █████
░░███░░░░███   ███░░░░░███ ░░███ ░░███ ░░███░░░░░███░░███ ░░██████ ░░███ 
 ░███   ░░███ ███     ░░███ ░░███ ███   ░███    ░███ ░███  ░███░███ ░███ 
 ░███    ░███░███      ░███  ░░█████    ░██████████  ░███  ░███░░███░███ 
 ░███    ░███░███      ░███   ███░███   ░███░░░░░███ ░███  ░███ ░░██████ 
 ░███    ███ ░░███     ███   ███ ░░███  ░███    ░███ ░███  ░███  ░░█████ 
 ██████████   ░░░███████░   █████ █████ ███████████  █████ █████  ░░█████
░░░░░░░░░░      ░░░░░░░    ░░░░░ ░░░░░ ░░░░░░░░░░░  ░░░░░ ░░░░░    ░░░░░ 

   '''
    
    print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(banner)))
    print(Colorate.Horizontal(Colors.purple_to_blue, f"doxbin link: https://doxbin.com/"))
    input("Press Enter to return ") 

def option9():
    clear_screen()

    banner = '''

 █████ ███████████                                                      
░░███ ░░███░░░░░███                                                     
 ░███  ░███    ░███                                                     
 ░███  ░██████████                                                      
 ░███  ░███░░░░░░                                                       
 ░███  ░███                                                             
 █████ █████                                                            
░░░░░ ░░░░░                                                             
                                                                        
 ███████████  █████ ██████   █████   █████████  ██████████ ███████████  
░░███░░░░░███░░███ ░░██████ ░░███   ███░░░░░███░░███░░░░░█░░███░░░░░███ 
 ░███    ░███ ░███  ░███░███ ░███  ███     ░░░  ░███  █ ░  ░███    ░███ 
 ░██████████  ░███  ░███░░███░███ ░███          ░██████    ░██████████  
 ░███░░░░░░   ░███  ░███ ░░██████ ░███    █████ ░███░░█    ░███░░░░░███ 
 ░███         ░███  ░███  ░░█████ ░░███  ░░███  ░███ ░   █ ░███    ░███ 
 █████        █████ █████  ░░█████ ░░█████████  ██████████ █████   █████
░░░░░        ░░░░░ ░░░░░    ░░░░░   ░░░░░░░░░  ░░░░░░░░░░ ░░░░░   ░░░░░ 




 '''
    print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(banner)))
    print(Colorate.Horizontal(Colors.purple_to_blue, f"ip pinger on github (ip pinger.py): https://github.com/mxssacro/juicy-tool-v1.1"))
    input("Press Enter to return ")

def main():
    while True:
        clear_screen()
        print_banner(banner)
        print_menu()
        choice = input(Colorate.Horizontal(Colors.blue_to_purple, "\n\n» "))

        if choice == "1":
            option1()
        elif choice == "2":
            option2()
        elif choice == "3":
            option3()
        elif choice == "4":
            option4()
        elif choice == "5":
            option5()
        elif choice == "6":
            option6()
        elif choice == "7":
            option7()
        elif choice == "8":
            option8()
        elif choice == "9":
            option9()
        else:
            print("Invalid choice.")
            input("Press Enter to continue")
if __name__ == "__main__":
    main()