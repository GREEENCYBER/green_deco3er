#coded by green cyber
#team wolf cyber security
#coeded by iranyan hac3er 
import os
import design
import decoder
import sys
from colorama import Fore as color
from time import sleep
bold = '\033[0m'
endbold = '\033[0m'





# my librarys
####################################################
try:
    from colorama import Fore
except:
    print("Install colorama library: pip install library")
###################################################################



while True:
    try:

        os.system("clear");design.banner();design.menu()
        option = int(input(color.LIGHTRED_EX+"["+color.LIGHTBLUE_EX+"☣"+color.LIGHTRED_EX+"]"+color.CYAN+"/home/"+Fore.GREEN+"YOUR OPTION"+Fore.LIGHTGREEN_EX+"☛☛☛☛☛"))

        if (option == 1):
            os.system('clear');design.banner()
            print(color.WHITE+"Enter Your Text: ")
            user_option = input(color.RED+"\n[*]"+color.RED+"GREEN ENCO3ER"+color.LIGHTYELLOW_EX+'/'+color.LIGHTWHITE_EX+"base64"+color.LIGHTCYAN_EX+'/'+color.LIGHTRED_EX+'>>')
            print(bold+color.WHITE+"Encypted ☑\n")
            os.system(f'echo {user_option} | base64')
            input(bold+color.GREEN+"Press Any key....")
            continue
        elif (option == 2):
            os.system('clear');design.banner()
            print(color.WHITE+"Enter Your Text: ")
            user_option = input(color.RED+"\n[*]"+color.RED+"GREEN ENCO3ER"+color.LIGHTYELLOW_EX+'/'+color.LIGHTWHITE_EX+"hex"+color.LIGHTCYAN_EX+'/'+color.LIGHTRED_EX+'>>')
            print(bold+color.WHITE+"Encypted ☑\n")
            os.system(f'echo {user_option} | xxd -p')
            input(bold+color.GREEN+"Press Any key....")
            continue  
        elif (option == 3):
            os.system('clear');design.banner()
            print(color.WHITE+"Enter Your Text: ")
            user_option = input(color.RED+"\n[*]"+color.RED+"GREEN ENCO3ER"+color.LIGHTYELLOW_EX+'/'+color.LIGHTWHITE_EX+"Rot13"+color.LIGHTCYAN_EX+'/'+color.LIGHTRED_EX+'>>')
            print(bold+color.WHITE+"Encypted ☑\n")
            os.system(f"echo {user_option} | tr 'A-Za-z' 'N-ZA-Mn-za-m'")
            input(bold+color.GREEN+"Press Any key....")
            continue  
        elif (option == 4):
            os.system('clear');design.banner();design.decoder_menu()
            option = int(input(color.LIGHTRED_EX+"["+color.LIGHTBLUE_EX+"☣"+color.LIGHTRED_EX+"]"+color.CYAN+"/decoder/"+Fore.GREEN+"YOUR OPTION"+Fore.LIGHTGREEN_EX+"☛☛☛☛☛"))
            decoder.decoder_menu(option)
            continue

        elif (option == 0):
            print("Thank for use GREEN ENCO3ER :)")

            sleep(2)
            sys.exit()
        else:
            print("invalid optin:(")
            sleep(3)
            sys.exit()







    except:
        sys.exit()