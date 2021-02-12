import requests
import random
import string
import threading
from itertools import cycle
from colorama import Fore
import os
os.system('color')

with open('proxies.txt', 'r+', encoding='utf-8') as f:
    proxy = cycle(f.read().splitlines())
with open('instacookies.txt', 'r+', encoding='utf-8') as f:
    cookie = cycle(f.read().splitlines())
with open('instaids.txt', 'r+', encoding='utf-8') as f:
    instagramids = cycle(f.read().splitlines())

print(f"""{Fore.RED}
 $$$$$$\   $$$$$$\  $$$$$$$\  $$$$$$$$\ $$$$$$\ $$\   $$\ $$$$$$$$\       $$$$$$$$\  $$$$$$\   $$$$$$\  $$\       $$$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ 
$$  __$$\ $$  __$$\ $$  __$$\ $$  _____|\_$$  _|$$$\  $$ |$$  _____|      \__$$  __|$$  __$$\ $$  __$$\ $$ |      $$  __$$\ $$  __$$\ $$  __$$\ $$ | $$  |
$$ /  \__|$$ /  $$ |$$ |  $$ |$$ |        $$ |  $$$$\ $$ |$$ |               $$ |   $$ /  $$ |$$ /  $$ |$$ |      $$ |  $$ |$$ /  $$ |$$ /  \__|$$ |$$  / 
$$ |      $$ |  $$ |$$ |  $$ |$$$$$\      $$ |  $$ $$\$$ |$$$$$\             $$ |   $$ |  $$ |$$ |  $$ |$$ |      $$$$$$$  |$$$$$$$$ |$$ |      $$$$$  /  
$$ |      $$ |  $$ |$$ |  $$ |$$  __|     $$ |  $$ \$$$$ |$$  __|            $$ |   $$ |  $$ |$$ |  $$ |$$ |      $$  ____/ $$  __$$ |$$ |      $$  $$<   
$$ |  $$\ $$ |  $$ |$$ |  $$ |$$ |        $$ |  $$ |\$$$ |$$ |               $$ |   $$ |  $$ |$$ |  $$ |$$ |      $$ |      $$ |  $$ |$$ |  $$\ $$ |\$$\  
\$$$$$$  | $$$$$$  |$$$$$$$  |$$$$$$$$\ $$$$$$\ $$ | \$$ |$$$$$$$$\          $$ |    $$$$$$  | $$$$$$  |$$$$$$$$\ $$ |      $$ |  $$ |\$$$$$$  |$$ | \$$\ 
 \______/  \______/ \_______/ \________|\______|\__|  \__|\________|         \__|    \______/  \______/ \________|\__|      \__|  \__| \______/ \__|  \__|
version - 0.3.0

[1] Follow Bot
[2] Like Bot
[3] Comment Bot
[4] Comment Like Bot
[5] ID Scraper
[6] Mass Follower 
""")


headers = {
    'x-csrftoken': 'abc',
    'x-instagram-ajax': 'c08befdb032d',
    'x-requested-with': 'XMLHttpRequest',
    'x-ig-app-id': '936619743392459'

}

def follow():
    while True:
        try:
            proxies = {
                'https': 'https://' + next(proxy)
            }
            cookies = {
                'sessionid': next(cookie)
            }
            sendfollow = requests.post(f'https://www.instagram.com/web/friendships/{clientid}/follow/', cookies=cookies, headers=headers, proxies=proxies)

            if sendfollow.status_code == 200:
                print(f'{Fore.GREEN}[ + ] Follow Sent: {clientid}{Fore.RESET}')
            else:
                print(f'{Fore.RED}Error: {sendfollow.status_code}{Fore.RESET}')
        except Exception as err:
            x = 'test'
def commentbot():
    while True:
        try:
            proxies = {
                'https': 'https://' + next(proxy)
            }
            cookies = {
                'sessionid': next(cookie)
            }
            data = {
                'comment_text': msg
            }
            sendcomment = requests.post(f'https://www.instagram.com/web/comments/{commentid}/add/', cookies=cookies, headers=headers, proxies=proxies, data=data)
            if sendcomment.status_code == 200:
                print(f'{Fore.GREEN}[ + ] Comment Sent: {commentid}{Fore.RESET}')
            else:
                print(f"{Fore.RED}[ - ] Error: {sendcomment.status_code}{Fore.RESET}")
        except Exception as err:
            x = 'test'
def likebot():
    while True:
        try:
            proxies = {
                'https': 'https://' + next(proxy)
            }
            cookies = {
                'sessionid': next(cookie)
            }


            sendlike = requests.post(f'https://www.instagram.com/web/likes/{postid}/like/',cookies=cookies, headers=headers, proxies=proxies)
            if sendlike.status_code == 200:
                print(f'{Fore.GREEN}[ + ] Like Sent: {postid}{Fore.RESET}')
            else:
                print(f"{Fore.RED}[ - ] Error: {sendlike.status_code}{Fore.RESET}")
        except Exception as err:
            x = 'test'
def commentlikebot():
    while True:
        try:
            proxies = {
                'https': 'https://' + next(proxy)
            }
            cookies = {
                'sessionid': next(cookie)
            }

            sendcommentlike = requests.post(f'https://www.instagram.com/web/comments/like/{commentid1}/')
            if sendcommentlike.status_code == 200:
                print(f'{Fore.GREEN}[ + ] Like Sent: {commentid1}{Fore.RESET}')
            else:
                print(f"{Fore.RED}[ - ] Error: {sendcommentlike.status_code}{Fore.RESET}")
        except Exception as err:
            x = 'test'
def idscraper():
    while True:
        try:
            proxies = {
                'https': 'https://' + next(proxy)
            }
            cookies = {
                'sessionid': next(cookie)
            }

            length = 10

            randomid = ''.join((random.choice(string.digits)) for i in range(length))

            testid = requests.get(f'https://i.instagram.com/api/v1/users/{randomid}/info/', headers=headers, cookies=cookies, proxies=proxies)
            if testid.status_code == 200:
                print(f'{Fore.GREEN} ID Found: {randomid}{Fore.RESET}')
                with open('instaids.txt', 'a') as f:
                    f.write(randomid + '\n')
        except Exception as err:
            x = 'test'
def massfollow():
    while True:
        try:
            proxies = {
                'https': 'https://' + next(proxy)
            }
            cookies = {
                'sessionid': next(cookie)
            }
            scrapedid = next(instagramids)
            followmass = requests.post(f'https://www.instagram.com/web/friendships/{scrapedid}/follow/', cookies=cookies, headers=headers, proxies=proxies)

            if followmass.status_code == 200:
                print(f'{Fore.GREEN}[ + ] Follow Sent: {scrapedid}{Fore.RESET}')
            else:
                print(f'{Fore.RED}Error: {followmass.status_code}{Fore.RESET}')
        except Exception as err:
            x = 'test'
choice = input(f'>>>> {Fore.RESET}')







if choice == '1':
    clientid = input('Enter a clientID: ')
    threads = int(input('Threads: '))
    for i in range(threads):
        t1 = threading.Thread(target=follow).start()
if choice == '2':
    postid = input('Enter a postID: ')
    threads = int(input('Threads: '))
    for i in range(threads):
        t1 = threading.Thread(target=likebot).start()
if choice == '3':
    commentid = input('Enter a videoID: ')
    msg = input('Enter a MSG to comment: ')
    threads = int(input('Threads: '))
    for i in range(threads):
        t1 = threading.Thread(target=commentbot).start()
if choice == '4':
    commentid1 = input('Enter a commentID: ')
    threads = int(input('Threads: '))
    for i in range(threads):
        t1 = threading.Thread(target=commentlikebot).start()
if choice == '5':
    threads = int(input('Threads: '))
    for i in range(threads):
        t1 = threading.Thread(target=idscraper).start()
if choice == '6':
    threads = int(input('Threads: '))
    for i in range(threads):
        t1 = threading.Thread(target=massfollow).start()


