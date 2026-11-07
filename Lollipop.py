import os, getpass, warnings, base64, hashlib, time, sys
import CLI_Colors
import cryptography
from cryptography.fernet import Fernet

os.system("cls" if os.name == "nt" else "clear")
print(f"{CLI_Colors.info} LOLLIPOP Encrypter Open Source Project")
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
time.sleep(1)
cn = True
while cn:
    os.system("cls" if os.name == "nt" else "clear")
    print(r"""    __          _____ ____            
   / /   ____  / / (_) __ \____  ____ 
  / /   / __ \/ / / / /_/ / __ \/ __ \
 / /___/ /_/ / / / / ____/ /_/ / /_/ /
/_____/\____/_/_/_/_/    \____/ .___/ 
                             /_/      """)
    print(f"[e] Encrypt    [d] Decrypt    [a] About    [q] Quit    [r] Restart")
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
        print(f"{CLI_Colors.info} Lollipop \nLightweight Encryption/Decryption Program Written in Python\nFully Open Source\nWrote by human on Earth")
        input("Press Enter to continue...")
    elif option == ("q" or "[q]" or "quit"):
        os.system("cls" if os.name == "nt" else "clear")
        cn = False
    elif option == ("r" or "[r]" or "restart"):
        print("Restart in 3")
        time.sleep(1)
        print("Restart in 2")
        time.sleep(1)
        print("Restart in 1")
        time.sleep(1)
        os.execv(sys.executable, [sys.executable] + sys.argv)
    else:
        input(f"{CLI_Colors.error} Invalid Option, Press Enter to continue...")

