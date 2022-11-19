import pandas as pd
import requests as req
import xlrd
from bs4 import BeautifulSoup
import re

link='https://quote.rbc.ru/tag/currency'
def un(l):
    a=[]
    for i in l:
        i=i.replace('"','').replace('>','').replace(' ','')
        if 'png' not in i and 'jpg' not in i:
            if i not in a:
                a.append(i)
    return a
def un_2(l):
    a=[]
    for i in l:
        i=i.replace('"','').replace('>','').replace(' ','')
        if '810x405_crop' not in i:
            a.append(i)
    return a

def goParse(lik):
    times,names,links, photos = [],[],[],[]
    res = req.get(lik)
    html = BeautifulSoup(res.text, 'lxml')
    times= html.find_all('span', class_="q-item__date__text")
    names = html.find_all('span', class_="q-item__title js-rm-central-column-item-text")
    links = html.find_all('a', class_="q-item__link")
    photos = html.find_all('img', class_="g-image q-item__image js-rm-central-column-item-image")
    df=pd.DataFrame()
    for i, time in enumerate(times):
        times[i]=time.text
    for i, name in enumerate(names):
        names[i]=name.text
    df['время']= times
    df['название']=names
    df['ссылка']=un(list(re.findall(r'(https?://[^\s]+)', str(links))))
    df['фотография']=un_2(list(re.findall(r'(https?://[^\s]+)', str(photos))))
    for i in range(0,len(df['время'])):
        df['время'][i]=str(df['время'][i]).replace(" ","").replace("\n","")
        df['название'][i] = str(df['название'][i]).replace("\n", "").lstrip()
    return df


print(goParse(link))