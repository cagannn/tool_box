import argparse
import os
import colorama
from colorama import Fore, Back, Style
from pyfiglet import Figlet
import random
import time

    
parser = argparse.ArgumentParser(prog='Tool Box')
parser.add_argument('-w', '--wiyp', action="store", dest="wiyp", help="'-w help' for more information")
parser.add_argument('-l', '--lists', action="store", dest="lists", help="Listing type of attacks")
args = parser.parse_args()
wiyp=str(args.wiyp)
lists=str(args.lists)
colorama.init()

def logo():
    os.system("clear")
    font_list=["banner","slant","emboss","smbraille","pagga","future"]
    random.shuffle(font_list)
    for i in range(0,len(font_list)):
        f = Figlet(font=font_list[i])
        print(f.renderText('Tool Box'))
        time.sleep(0.5)
        os.system("clear")
    
    
if wiyp=="help":
    print("[+]Web discover(wd) param is include nmap, enum4linux, dirb optional(wpscan..)")
    print("[+]Web attack(na) param is include hydra")
    print("[+]Network discover(nd) param is include wireshark, netdiscover, aircrack-ng")
    print("[+]Bash attack (ba) include binwalk, steghide, john the ripper")


if wiyp=="wd":
    logo()
    attack_ip=str(input("[+]Ip:"))
    attack_type=[]
    print("Enter number of scan types:")
    print("[1]Syn scan\n[2]Which servis is working on open ports\n[3]Fast scan\n[4]Scan all ports\n[9]Start scan")
    nmap_scan=str(input(""))
    if len(nmap_scan)==0:
        print("Tek")
    else:
        a=True
        nmap_attack=[]
        command="nmap"
        say1=0
        say2=0
        say3=0
        say4=0
        while(a):
            attack_type=int(input())
            nmap_attack.append(attack_type)
            
            if attack_type==9:
                a=False
            for i in nmap_attack:
                
                if i == 1:
                    if say1==0:
                        command=command+" "+"-sS"
                        say1=say1+1
                    else:
                        continue
                if i==2:
                    if say2==0:
                        command=command+" "+"-sV"+" "+"-sC"
                        say2=say2+1
                    else:
                        continue
                if i==3:
                    if say3==0:
                        command=command+" "+"-F"
                        say3=say3+1
                    else:
                        continue
                if i==4:
                    if say4==0:
                        command=command+" "+"-p"
                        say4=say4+1
                    else:
                        continue
        print(command+" "+attack_ip)
        os.system(command+" "+attack_ip)
        dirb_scan_want=input("Do you want to dirb scan?(y/n)")
        
        if dirb_scan_want=="y":
            ssl=input("Has this ip ssl?(y/n)")
            if ssl=="y":
                print("dirb https://"+attack_ip+"/")
                os.system("dirb https://"+attack_ip+"/")
            elif ssl=="n":
                print("dirb http://"+attack_ip+"/")
                os.system("dirb https://"+attack_ip+"/")
        enum_scan=input("Do you want to enum4linux scan?(y/n)")
        if enum_scan=="y":
            print("enum4linux -a"+" "+attack_ip)
            os.system("enum4linux -a"+" "+attack_ip)

elif wiyp=="nd":
    logo()
    print("netdiscover")
    os.system("netdiscover")
    print("wireshark")
    os.system("wireshark")
elif wiyp=="ba":
    logo()
    file_type=input("Enter file extension (ex:zip,jpg...)")
    file_loc=input("Enter that file you want to attacks location:")
    print("binwalk -e"+" "+file_loc+" "+"--run-as=root")
    os.system("binwalk -e"+" "+file_loc+" "+"--run-as=root")
    print("steghide extract -sf"+" "+file_loc)
    os.system("steghide extract -sf"+" "+file_loc)
    print(file_type+"2john"+" "+file_loc+">"+ "hash_it")
    os.system(file_type+"2john"+" "+file_loc+" "+">"+" "+"hash_it")
    


if lists=="help":
    print("")
