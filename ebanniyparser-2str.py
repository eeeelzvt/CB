import pandas as pd
import requests as req
import xlrd
from bs4 import BeautifulSoup


link='https://quote.rbc.ru/tag/currency'

def goParse(lik):
    times,names,links, photos = [],[],[],[]
    res = req.get(lik)
    html = BeautifulSoup(res.text, 'lxml')
    times= html.find_all('span',class_="q-item__date__text")
    names = html.find_all('span', class_="q-item__title js-rm-central-column-item-text")
   # link_ = html.find_all('a', class_="q-item__link")
    ph = html.find_all('img', class_="g-image q-item__image js-rm-central-column-item-image")
    df=pd.DataFrame()
    for i, time in enumerate(times):
        times[i]=time.text
    for i, name in enumerate(names):
        names[i]=name.text
   # for i in link_:
   #     links.append(i['href'])
    for s in ph:
        photos.append(s['srcset'])
    links=list(set(links))
    photos=list(set(photos))
    df['время']= times
    df['название']=names
   # df['ссылка']=links
    #df['фотография']=photos
    for i in range(0,len(df['время'])):
        df['время'][i]=str(df['время'][i]).replace(" ","").replace("\n","")
        df['название'][i] = str(df['название'][i]).replace("\n", "").lstrip()
    return photos
print(goParse(link))