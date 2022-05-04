from colorama import Fore as color
from time import sleep
bold = '\033[0m'
endbold = '\033[0m'

def banner():
    print(color.RED+"""
                                                        ______              
                                                       (_____ \             
  ____  ____ _____ _____ ____     _____ ____   ____ ___ _____) )_____  ____ 
 / _  |/ ___) ___ | ___ |  _ \   | ___ |  _ \ / ___) _ (_____ (| ___ |/ ___)
( (_| | |   | ____| ____| | | |  | ____| | | ( (__| |_| |____) ) ____| |    
 \___ |_|   |_____)_____)_| |_|  |_____)_| |_|\____)___(______/|_____)_|    
(_____|                                                                     
 
    """)


    print(bold+color.BLUE+"""
                                                                            
      ⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖
      ☣ coded by greencyber                ☣
      ☣ team: wolf cyber security          ☣
      ☣ instagrame: greeen_cyber           ☣
      ☣ team.ins: wilf_cyber_security_team ☣
      ⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖⚖
    
    """+endbold)
    sleep(2)

def menu():
    print(bold+color.RED+"[1]" +color.BLUE+"Base64")
    print(color.CYAN+"**************************")
    sleep(.4)
    print(bold+color.RED+"[2]" +color.BLUE+"HEX")
    print(color.CYAN+"**************************")
    sleep(.4)
    print(bold+color.RED+"[3]" +color.BLUE+"Rox13")
    print(color.CYAN+"**************************")
    sleep(.4)
    print(bold+color.RED+"[4]" +color.BLUE+"Decoder")
    print(color.CYAN+"**************************")
    sleep(.4)
    print(bold+color.RED+"[0]" +color.BLUE+"exit"+endbold)

def decoder_menu():
     print(bold+color.RED+"[1]" + color.BLUE+"base64")
     print(color.CYAN+"**************************")
     sleep(.4)
     print(bold+color.RED+"[2]" +color.BLUE+"HEX")
     print(color.CYAN+"**************************")
     sleep(.4)
     print(bold+color.RED+"[3]" +color.BLUE+"Rox13")
     print(color.CYAN+"**************************")
     sleep(.4)
     print(bold+color.RED+"[0]" +color.BLUE+"back"+endbold)
