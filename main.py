from zipfile import ZipFile
import os
from colorama import Fore, init
from colorama import Fore, Style
import threading
import os.path

lock = threading.Lock()
sent = 0
init(convert=True)
clear = lambda: os.system('cls')

def getBanner():
    clear()
    banner = f'''{Fore.YELLOW}
        ██████╗ ██████╗ ██╗   ██╗████████╗███████╗    ███████╗ ██████╗ ██████╗  ██████╗███████╗
        ██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝    ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝
        ██████╔╝██████╔╝██║   ██║   ██║   █████╗      █████╗  ██║   ██║██████╔╝██║     █████╗  
        ██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝      ██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝  
        ██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗    ██║     ╚██████╔╝██║  ██║╚██████╗███████╗
        ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝ 
                                    {Fore.RESET}dev: Gabriel Lima
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    [{Fore.YELLOW}1{Fore.RESET}] Arquivo .zip
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'''
    return banner

def start_menu():
    print(getBanner())
    print(f'[{Fore.YELLOW}>{Fore.RESET}] Digite sua opção', end=''); choice = str(input(':  '))
    if choice == '1':
        archive_zip()
    else:
        clear()
        start_menu()

def archive_zip():
    print(f'[{Fore.YELLOW}>{Fore.RESET}] Insira o diretório do arquivo {Fore.YELLOW}.zip{Fore.RESET}', end=''); directory_path = str(input(':  '))
    print(f'[{Fore.YELLOW}>{Fore.RESET}] Insira o diretório da wordlist {Fore.YELLOW}.txt{Fore.RESET}', end=''); directory_wordlist = str(input(':  '))
    if os.path.isfile(directory_path):
        pass
    else:
        print(f'[{Fore.RED}-{Fore.RESET}] {Fore.RED}Arquivo .zip não encontrado{Fore.RESET}')
    if os.path.isfile(directory_wordlist):
        pass
    else:
        print(f'[{Fore.RED}-{Fore.RESET}] {Fore.RED}Arquivo .txt não encontrado{Fore.RESET}')

    if os.path.isfile(directory_path) and os.path.isfile(directory_wordlist):
        def brute_zip():
            global sent
            with open(f"{directory_wordlist}", encoding="utf8") as f:
                passes = f.readlines()
                for line in passes:
                    str_pwd = line.split("\n")[0]
                    try:
                        with ZipFile(directory_path) as zipObj:
                            zipObj.extractall(pwd=bytes(str_pwd, 'utf-8'))
                            print(f'''
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    {Fore.GREEN}Tentativas      Senha
    {Fore.RESET}    {sent}          {Fore.RESET}{str_pwd}

    O arquvio já foi extraido!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━''', end='')
                            input()
                            start_menu()
                    except:
                        lock.acquire()
                        sent += 1
                        print(f'[{Fore.GREEN}+{Fore.RESET}] Efetuando tentativas | %s' % (sent))
                        lock.release()
                        pass
        threads = threading.Thread(target=brute_zip)
        threads.start()
    else:
        input()
        start_menu()

if __name__ == "__main__":
    start_menu()