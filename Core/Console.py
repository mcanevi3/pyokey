from colorama import Fore, Style

def print_color(string:str,color:str):
    if color=="r":
        print(Fore.RED + string + Style.RESET_ALL)
    elif color=="g":
        print(Fore.GREEN + string + Style.RESET_ALL)
    elif color=="b":
        print(Fore.BLUE + string + Style.RESET_ALL)
    elif color=="k":
        print(Fore.BLACK + string + Style.RESET_ALL)
    elif color=="y":
        print(Fore.YELLOW + string + Style.RESET_ALL)
    else:    
        print(string + Style.RESET_ALL)
