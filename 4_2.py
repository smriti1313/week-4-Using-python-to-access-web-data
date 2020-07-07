# import urllib.request,urllib.parse,urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input('enter-')
pos=int(input('link position-'))-1
count=int(input('No. of times-'))
html=urlopen(url,context=ctx).read()
soup=BeautifulSoup(html,"html.parser")
#list_of_links=[] list can be used too

tags=soup('a')
for i in range(count):
    link=tags[pos].get('href',None)
    name=tags[pos].contents[0]    # list_of_links.append(tags[pos].contents[0])
    html=urlopen(link,context=ctx).read()
    soup=BeautifulSoup(html,"html.parser")
    tags=soup('a')
print(name)
# print(list_of_links[count-1])  #print(list_of_links[-1]) alternatives
