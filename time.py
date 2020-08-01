import requests
from bs4 import BeautifulSoup

city_name=input()
r=requests.get("https://google.com/search?q="+city_name+"Time")
response=r.content
#print(response)
soup=BeautifulSoup(response,"html.parser")
rows=soup.find_all('div',{'class':'BNeawe iBp4i AP7Wnd'})
for row in rows:
    try:
        print(row.find('div').text)
    except AttributeError:
        print("")
    

