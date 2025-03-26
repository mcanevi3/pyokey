from colorama import Fore, Style

def print_color(string:str,color:str):
    if color=="r":
        print(Fore.RED + string + Style.RESET_ALL, end=" ")
    elif color=="g":
        print(Fore.GREEN + string + Style.RESET_ALL, end=" ")
    elif color=="b":
        print(Fore.BLUE + string + Style.RESET_ALL, end=" ")
    elif color=="k":
        print(Fore.BLACK + string + Style.RESET_ALL, end=" ")
    elif color=="y":
        print(Fore.YELLOW + string + Style.RESET_ALL, end=" ")
    else:    
        print(string + Style.RESET_ALL, end=" ")
