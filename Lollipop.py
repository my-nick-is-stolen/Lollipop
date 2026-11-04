import sys, os, time, getpass, warnings, base64, hashlib
from time import sleep

import cryptography
from cryptography.fernet import Fernet
os.system("")

os.system("cls" if os.name == "nt" else "clear")
try:
    import CLI_Colors
except:
   for i in range(10, 0, -1):
       print(f"\033[41;37m\033[2J\033[H\nFATAL\nResource CLI_Colors.py not found\nRestart in {i}s...\n" + (" " * 80 + "\n") * 50, end="", flush=True)
       time.sleep(1)
   print("\033[0m\033[2J\033[H", end="")
   os.execv(sys.executable, [sys.executable] + sys.argv)
os.system("cls" if os.name == "nt" else "clear")
print(f"{CLI_Colors.info} LOLLIPOP TEST VERSION 1")
def get_cipher(password: str):
    key_bytes = hashlib.sha256(password.encode()).digest()
    fernet_key = base64.urlsafe_b64encode(key_bytes)
    return Fernet(fernet_key)
print(f"{CLI_Colors.info} Initialized Cipher")
print(r"""                                                                                            
                                              .....................                         
                                         ....//...................\\....                    
                                      ..//....=====================....\\..                 
                                   ..//..===============================..\\..              
                                 .//..============..========...============..\\.            
                                //.==========.===````======`` ``==..==========.\\.          
                              .//=========.=` `===..========...==````=.=========.\\         
                             //.=========` `=.====================..=` =.=========\\        
                            //=========.==.===========================.= \=========\\       
                           `//========/ `====================.==========\ `=========\\      
                   .....   //========` /====================` `=.========.===========\\     
                 .//...\\.//=================================.=` \==========.=========\`    
                `/.=====.\.`========`.`=========================\ \========` `========``    
                ``========.=========`.`==========================` `========.=========``    
                ``=========.=====================================`.`==================``    
                ``========` `========` \====================================.=========``    
                `\====================\ `=======================/ `========` `========``    
                 \\========` `=========.===.==================.= /==========.=========/`    
                  \\========.==.==========` `=..==========..=` =.====================//     
                   \\=========` \==========.=````========````=.=========.===========//      
                    \\=========\ `============..==========..==========.= `=========//       
                     \\=========.==:=.=============================.=` =.=========//        
                      \\.===========` `==.======================.=` `=.=========.//         
                       .\\.==========.==` `====.....==.....====` `=.==========.//.          
                         .\\..===========.====``   ````   ``====.===========.//.            
                           ..\\..==============.....==.....==============..//.              
                              ..\\...================================...//..                
                                 ...\\.....====================.....//...                   
                                     .....\\..................//.....                       
                                           ....................                             
                                                                                            
                                                                                            
                                                                                            
                                                                                            
                                                                                            
                                                                                            
                                                                                            
                                                                                            
                                                                                            
""")
sleep(1)
cn = True
while cn:
    os.system("cls" if os.name == "nt" else "clear")
    print(r"""    __          _____ ____            
   / /   ____  / / (_) __ \____  ____ 
  / /   / __ \/ / / / /_/ / __ \/ __ \
 / /___/ /_/ / / / / ____/ /_/ / /_/ /
/_____/\____/_/_/_/_/    \____/ .___/ 
                             /_/      """)
    print(f"[e] Encrypt    [d] Decrypt    [a] About    [q] Quit")
    option = input("Chose an option...    ").lower().strip()
    if option == ("e" or "[e]" or "encrypt"):
        warnings.filterwarnings("error", category=getpass.GetPassWarning)
        try:
            key = getpass.getpass("Enter an Encryption Key...    ")
        except getpass.GetPassWarning:
            print(f"{CLI_Colors.warning} Key is going to be visible")
            key = input("Enter an Encryption Key...    ")
        cipher = get_cipher(key)
        message = input("Enter a Message to Encrypt...    ")
        encrypted = cipher.encrypt(message.encode())
        print(f"Encrypted Message:    {encrypted.decode()}")
        input("Press Enter to continue...")
    elif option == ("d" or "[d]" or "decrypt"):
        warnings.filterwarnings("error", category=getpass.GetPassWarning)
        try:
            key = getpass.getpass("Enter an Encryption Key...    ")
        except getpass.GetPassWarning:
            print(f"{CLI_Colors.warning} Key is going to be visible")
            key = input("Enter an Encryption Key...    ")
        dl = True
        while dl:
            try:
                cipher = get_cipher(key)

                message = input("Enter a Message to Decrypt...    ")
                decrypted = cipher.decrypt(message)
                print(f"Decrypted Message:    {decrypted.decode()}")
                dl = False
            except cryptography.fernet.InvalidToken:
                print(f"\n{CLI_Colors.error} Key is Invalid")
        input("Press Enter to continue...")
    elif option == ("a" or "[a]" or "about"):
        print(f"{CLI_Colors.info} Lollipop v1\nLightweight Encryption/Decryption Program Written in Python\nDesigned for Maximum Compatibility\nWrote by human on Earth")
        input("Press Enter to continue...")
    elif option == ("q" or "[q]" or "quit"):
        cn = False
    else:
        input(f"{CLI_Colors.error} Invalid Option, Press Enter to continue...")

