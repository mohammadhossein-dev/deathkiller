from colorama import Fore
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')

def banner():
    msg_banner = """
    ████████▄     ▄████████    ▄████████     ███        ▄█    █▄       ▄█   ▄█▄  ▄█   ▄█        ▄█          ▄████████    ▄████████ 
    ███   ▀███   ███    ███   ███    ███ ▀█████████▄   ███    ███     ███ ▄███▀ ███  ███       ███         ███    ███   ███    ███ 
    ███    ███   ███    █▀    ███    ███    ▀███▀▀██   ███    ███     ███▐██▀   ███▌ ███       ███         ███    █▀    ███    ███ 
    ███    ███  ▄███▄▄▄       ███    ███     ███   ▀  ▄███▄▄▄▄███▄▄  ▄█████▀    ███▌ ███       ███        ▄███▄▄▄      ▄███▄▄▄▄██▀ 
    ███    ███ ▀▀███▀▀▀     ▀███████████     ███     ▀▀███▀▀▀▀███▀  ▀▀█████▄    ███▌ ███       ███       ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
    ███    ███   ███    █▄    ███    ███     ███       ███    ███     ███▐██▄   ███  ███       ███         ███    █▄  ▀███████████ 
    ███   ▄███   ███    ███   ███    ███     ███       ███    ███     ███ ▀███▄ ███  ███▌    ▄ ███▌    ▄   ███    ███   ███    ███ 
    ████████▀    ██████████   ███    █▀     ▄████▀     ███    █▀      ███   ▀█▀ █▀   █████▄▄██ █████▄▄██   ██████████   ███    ███ 
                                                                    ▀              ▀         ▀                        ███    ███ 
    v1.0                                                                
    """
    msg_credit = r"""
                            /|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\
                           |  Developed By Mohammad Hossein, mohammadhossein.dev@gmail.com |
                            \|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||/
    """

    clear()
    print(Fore.RED+msg_banner+Fore.RESET)
    print(Fore.LIGHTGREEN_EX+msg_credit+Fore.RESET)
