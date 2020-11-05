import requests
import sys
import urllib3
urllib3.disable_warnings()
import re
from colorama import Fore
proxy={"http":"127.0.0.1:8080","https":"127.0.0.1:8080"}
def banner(name):
 print("-"*50)
 print(name)
 print("-"*50)
def basic(url,data,headers,base_req,scode):
 r=requests.session()
 op=r.post(url,data=data,headers=headers,verify=False)
 if scode==op.status_code:
  if len(base_req.content)==len(op.content):
    print(Fore.RED+"[+] HEUSTRICS DETECT:HOST HEADER BY ARBITRY HEADER INNJECTION"+Fore.RESET)
    if re.findall("zyperx",op.text):
      print(Fore.RED+"[+] REDIRECTION/ABSOULUTE URL DETECTED"+Fore.RESET)
    else:
      print(Fore.GREEN+"[-] ABSOLUTE URL/REDIRECT"+Fore.RESET)
  banner("[+]Headers")
  dom=url.split('/')[2]
  for i in zip(headers.keys(),headers.values()):
   if dom in i[1] or "zyperx" in i[1]:
  	print(i[0]+": "+i[1])

  print("_"*70)

 else:
   print("[-]HHI NOT POSSIBLE VIA ARBITARY HEADER")
   dom=url.split('/')[2]
   for i in zip(headers.keys(),headers.values()):
    if dom in i[1] or "zyperx" in i[1]:
    	print(i[0]+": "+i[1])
 
 print("\n")

def arbitary_hostheader(url,data,headers,base_req,scode):
 banner(Fore.CYAN+"[+]Arbitarty Header Check"+Fore.RESET)
 headers['Host']="zyperx.com"
 basic(url,data,headers,base_req,scode)
 
def flawed_validation(url,data,headers,base_req,scode):
  banner(Fore.CYAN+"[+]Flawed Validation Check"+Fore.RESET)
  dom=url.split('/')[2]
  payload=[]
  payload.append("zyperx-"+dom)
  payload.append("zyperx.com/."+dom)
  for i in payload:
    headers['Host']=i
    basic(url,data,headers,base_req,scode)

def duplicate_header(url,data,headers,base_req,scode):
  banner(Fore.CYAN+"[+]Duplicate Headers"+Fore.RESET)
  # dom=url.split('/')[2]
  # headers['Host']="zyperx.com"
  # headers = [(k, v) for k, v in headers.items()]
  # headers.append(("Host",dom))
  # basic(url,data,headers,base_req,scode)

  # for i in payload:
  #   headers['Host']=i
  #   basic(url,data,headers,base_req,scode)
  print("[-] Feature has to be implemented =( ")

def line_wrapping(url,data,headers,base_req,scode):
  banner(Fore.CYAN+"[+]Line Wrapping"+Fore.RESET)
  print("[-] Feature has to be implemented =( ")

def supply_absolute_url(url,data,headers,base_req,scode):
  banner(Fore.CYAN+"[+]Line Wrapping"+Fore.RESET)
  print("[-] Feature has to be implemented =( ")

if __name__=="__main__":
 r=requests.session()
 if len(sys.argv)<2:
  print("Usage: hostheader.py Request-Body")
  print("[+]Warning it will not work for multipart")
 else:
  f=open(str(sys.argv[1])).read()
  dom=re.findall("Host:(.*?)\n",f)[0].replace(' ','').replace('\r','')
  uri=re.findall("[HTTPOST]{4} (.*?) HTTP",f)[0].replace('\r','')
  if "https" in f:
   schema="https://"
  else:
   schema="http://"
  url=schema+dom+uri
  headers={}
  for i in f.split('\n'):
   if ":" in i:
     i=i.split(': ')
     headers[i[0]]=i[1].replace(' ','').replace('\r','')
  data=f.split()[-1]
  base_req=r.post(url,data=data,headers=headers)
  scode=base_req.status_code
  arbitary_hostheader(url,data,headers,base_req,scode)
  flawed_validation(url,data,headers,base_req,scode)
  duplicate_header(url,data,headers,base_req,scode)
  line_wrapping(url,data,headers,base_req,scode)