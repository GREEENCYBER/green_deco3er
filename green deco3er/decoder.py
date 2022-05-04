import sys
from colorama import Fore as color
import os
from time import sleep
import design
bold = '\033[0m'
endbold = '\033[0m'
#librarys imported
#################################
def decoder_menu(user_inp):
    if (user_inp == 1):
        os.system("clear");design.banner()
        print(color.WHITE+"Enter your encription text in base64: ")
        user_option = input(color.RED+"\n[*]"+color.RED+"GREEN ENCO3ER"+color.LIGHTYELLOW_EX+'/'+color.LIGHTWHITE_EX+"Base64 Deceript "+color.LIGHTCYAN_EX+'/'+color.LIGHTRED_EX+'>>')
        os.system(f'echo {user_option} | base64 -d')
        input('\n press any key.....'+endbold)
    elif (user_inp == 2):
            os.system('clear');design.banner()
            print(color.WHITE+"Enter Your  ENcripted in hex: ")
            user_option = input(color.RED+"\n[*]"+color.RED+"GREEN ENCO3ER"+color.LIGHTYELLOW_EX+'/'+color.LIGHTWHITE_EX+"hex deceriped"+color.LIGHTCYAN_EX+'/'+color.LIGHTRED_EX+'>>')
            print(bold+color.WHITE+"Encypted ☑\n")
            os.system(f'echo {user_option} | xxd -p -r')
            input('\n press any kay....'+endbold)
            
    elif (user_inp == 3):
            os.system('clear');design.banner()
            print(color.WHITE+"Enter Your Emcripted  Text in Rot13: ")
            user_option = input(color.RED+"\n[*]"+color.RED+"GREEN ENCO3ER"+color.LIGHTYELLOW_EX+'/'+color.LIGHTWHITE_EX+"Rot13 f"+color.LIGHTCYAN_EX+'/'+color.LIGHTRED_EX+'>>')
            print(bold+color.WHITE+"Encypted ☑\n")
            os.system(f"echo {user_option} | tr 'A-Za-z' 'N-ZA-Mn-za-m'")
            input('\n press any key....'+endbold)
    elif (user_inp == 0):
        pass

    else:
        print("print bad input....")
        sleep(2)
        sys.exit()