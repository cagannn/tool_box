import argparse
import os
import colorama
from colorama import Fore, Back, Style, init
from pyfiglet import Figlet
import random
import time
import subprocess,sys
    
parser = argparse.ArgumentParser(prog='Tool Box')
parser.add_argument('-w', '--wiyp', action="store", dest="wiyp", help="'-w help' for more information")
parser.add_argument('-l', '--lists', action="store", dest="lists", help="Listing type of attacks")
args = parser.parse_args()
wiyp=str(args.wiyp)
lists=str(args.lists)
colorama.init()
hexadecimals={
"png":"89504E470D0A1A0A",
"jpg or jpeg":"FFD8FFDB",
 "jpg or jpeg":"FFD8FFE000104A4649460001",
}
init(autoreset=True)
def logo():
    os.system("clear")
    font_list=["banner","slant","emboss","smbraille","pagga","future"]
    random.shuffle(font_list)
    for i in range(0,len(font_list)):
        f = Figlet(font=font_list[i])
        print(f.renderText('Tool Box'))
        time.sleep(0.5)
        os.system("clear")
def HexView(fileloc):
    hex_file=str(fileloc)
    try:
        with open(hex_file, 'rb') as in_file:
            while True:
                hexdata = in_file.read(16).hex()     
                if len(hexdata) == 0:                
                    break
                return hexdata.upper()       
    except FileNotFoundError:
        return 0
    
if wiyp=="help":
    print("[+]Web discover(wd) param is include nmap, enum4linux, dirb optional(wpscan..)")
    print("[+]Web attack(na) param is include hydra")
    print("[+]Network discover(nd) param is include wireshark, netdiscover, aircrack-ng")
    print("[+]Bash attack (ba) include binwalk, steghide, john the ripper")
    print("[+]Open metasploit(msf)")
    print("[+]Searching esploits(msfs)")


if wiyp=="wd":
    logo()
    attack_ip=str(input("[+]Ip:"))
    attack_type=[]
    documentation=input("Do you want nmap documentation(y/n)?")
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
        os.system(command+" "+attack_ip+" "+"> nmap_documentation.txt")
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
    cmd_binwalk="binwalk -e "+file_loc+"--run-as=root"
    try:
        binwalk=subprocess.check_output(cmd_binwalk,shell=True)
        binwalk=binwalk.decode("utf-8")
    
    except:
        print(Fore.RED + "Something wrong for binwalk\n")
    cmd_steghide ="steghide extract -sf "+file_loc
    try:
        steghide =subprocess.check_output(cmd_steghide, shell=True)
        steghide=steghide.decode("utf-8") 
    except:
        print(Fore.RED + "Something wrong for steghide\n")
    cmd_john=file_type+"2john"+" "+file_loc+" > hash_it"
    try:
        john=subprocess.check_output(cmd_john, shell=True)
        john=john.decode("utf-8")
    except:
        print(Fore.RED + "Something wrong for john \n")
    hexdata=HexView(file_loc)
    correct_hex=""
    if hexdata==0:
        print(Fore.RED +"No such file or dic "+file_loc)
    else:
        for i in hexdata:
            correct_hex=correct_hex+i
        try:
            correct_count=0
            for j,k in hexadecimals.items():
                t=len(k)
                if correct_hex[0:t]==k:
                    correct_count=1
                    break
            if correct_count==1:
                print(Fore.GREEN+"Correct type " + j)

        except KeyError :
            print(Fore.RED +"error")
    
        
elif wiyp=="msf":
    os.system("msfconsole")
elif wiyp=="msfs":
    search_exploit=input("[+]Enter your exploit for search:")
    os.system("searchploit"+" "+search_exploit)
   


    

if lists=="help":
    print("")
