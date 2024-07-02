# CODED BY - @akasakasddff

import os,sys,json,time,string,rich
import requests,bs4,fake_useragent
from fake_useragent import UserAgent
from rich import print_json as json
from bs4 import BeautifulSoup

r="\033[1;31m"
g='\x1b[38;5;40m'
g1='\x1b[38;5;41m'
g2='\x1b[38;5;42m'
g3='\x1b[38;5;43m'
g4='\x1b[38;5;44m'

LGO=f"""\n{g}\t
 \n{g3}\t █████  ██   ██  █████  ███████ ██   ██ 
\n{g3}\t ██   ██ ██  ██  ██   ██ ██      ██   ██ 
\n{g3}\t ███████ █████   ███████ ███████ ███████ 
\n{g3}\t ██   ██ ██  ██  ██   ██      ██ ██   ██ 
\n{g3}\t ██   ██ ██   ██ ██   ██ ███████ ██   ██ 
                                        
     

deta={
    "coded_by": "@akasakasddff",
    "channel": "@akasakasddff",
    "script": "tiktok_downloader",
    "type": "without_watermark"
    }
    
class DARK_LMNx999:
    os.system('xdg-open https://t.me/akasakasddff')
    os.system("clear");print(LGO)
    print(22*f'{g}-{g4}-');json(data=deta);print(22*f'{g}-{g4}-')
    link = input(f"{g}</>{g3} Enter Video Link{g2} : ")
    pass

session = requests.Session()
user_agent = UserAgent().random
lmnxload = f"q={link}&lang=en"
url = "https://savetik.co/api/ajaxSearch"

headers = {
    'User-Agent': user_agent,
    'Content-Type': "application/x-www-form-urlencoded",
    'sec-ch-ua': "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
    'dnt': "1",
    'sec-ch-ua-mobile': "?1",
    'x-requested-with': "XMLHttpRequest",
    'sec-ch-ua-platform': "\"Android\"",
    'origin': "https://savetik.co",
    'sec-fetch-site': "same-origin",
    'sec-fetch-mode': "cors",
    'sec-fetch-dest': "empty",
    'referer': "https://savetik.co/en2",
    'accept-language': "ar,en-US;q=0.9,en;q=0.8"
}

try:LMNxRES = session.post(url, data=lmnxload, headers=headers)
except Exception as lmx:
    print(22*f'{g}-{g4}-');print(f'{g}</> {r}Error : {lmx}')
    print(22*f'{g}-{g4}-');sys.exit()
    
if LMNxRES.status_code == 200:
    try:
        data = LMNxRES.json()
        soup = BeautifulSoup(data['data'], 'html.parser')
        links = soup.find_all('a', class_='tik-button-dl')
        if len(links) >= 2:
            link = links[1]['href']
            print(22*f'{g}-{g4}-');print(f'{g}</> {g2}DOWNLOAD LINK {r}-{g3} ',link)
        else:
            print(22*f'{g}-{g4}-');print(f"{g}</> {r}Error - Invalid TikTok Video Link !")
            print(22*f'{g}-{g4}-');sys.exit()
    except json.JSONDecodeError as e:
        print(22*f'{g}-{g4}-');print(f"{g}</> {r}Error - Something Went Wrong : {e}")
        print(22*f'{g}-{g4}-');sys.exit()
else:
    print(22*f'{g}-{g4}-');print(f"{g}</> {r}Error - {LMNxRES.status_code}")
    print(22*f'{g}-{g4}-');sys.exit()