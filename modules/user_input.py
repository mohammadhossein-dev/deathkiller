from colorama import Fore

target_url = ""
requests_count = 1

def get_user_input():
    global target_url
    target_url = input(Fore.GREEN+"[!] "+Fore.CYAN+"Please Enter the target URL => "+Fore.RED).strip()
    while target_url == "" or target_url == " " or target_url is None:
        target_url = input(Fore.GREEN + "[!] " + Fore.CYAN + "Please Enter the target URL => " + Fore.RED).strip()
    if target_url.startswith("http://") or target_url.startswith("https://"):
        pass
    else:
        print(Fore.RED+"[*] "+Fore.LIGHTRED_EX+"Please Enter the target URL with http:// or https:// and try again"+Fore.RESET)
        print(Fore.RED+"[*] "+Fore.LIGHTRED_EX+"Exiting the app ..."+Fore.RESET)
        exit()

    try :
        global requests_count
        requests_count = input(Fore.GREEN+"[!] "+Fore.CYAN+"How many requests do you want to send to "+Fore.LIGHTRED_EX+target_url+Fore.CYAN+" (>0) => "+Fore.RED).strip()
        while requests_count is None or int(requests_count) <= 0:
            requests_count = input(Fore.GREEN + "[!] " + Fore.CYAN + "How many requests do you want to send to " + Fore.LIGHTRED_EX + target_url + Fore.CYAN + " => " + Fore.RED).strip()

        requests_count = int(requests_count)
    except:
        print(Fore.RED+"[*] Please Enter a valid number which is bigger than 0!")
        print(Fore.RED+"[*] Exiting the app ..."+Fore.RESET)
        exit()
