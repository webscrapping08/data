
from requests_html  import  HTMLSession
from bs4 import BeautifulSoup
import requests
from csv import writer

import pandas as pd

from requests_html  import  HTMLSession

url= 'https://pppreport.org/location/AK'

s =HTMLSession()
r=s.get(url)

p = r.html.xpath('//*[@class="panel-body"]',first=True)

   
for i in p.absolute_links:
    url2 = i
    r3=s.get(url2)
    p2 = r3.html.xpath('//*[@class="panel-body"]',first=True)
    
    with open('finish.csv','w',encoding='utf8',newline='') as f:
        thewriter = writer(f)
        header = ['Business_Name','Address','Jobs_Retained','Date_Approved']
        thewriter.writerow(header)
    
        for i2 in p2.absolute_links:
            url2 = i2
            r3=requests.get(url2)
            soap =BeautifulSoup(r3.text,'html.parser')
            tablel= soap.find('div',class_='panel-body')

            #for ten in tablel.find_all('td'):
            #    print(ten)

            try:
                Business_Name = tablel.find_all('td')[3].text.strip()
                #rangee = tablel.find_all('td')[1].text.strip()
                Address = tablel.find_all('td')[5].text.strip()
                #NAICS = tablel.find_all('td')[7].text.strip()
                #typee = tablel.find_all('td')[9].text.strip()
                #race = tablel.find_all('td')[11].text.strip()
                #Gender = tablel.find_all('td')[13].text.strip()
                #Veteran = tablel.find_all('td')[15].text.strip()
                Jobs_Retained = tablel.find_all('td')[17].text.strip()
                Date_Approved = tablel.find_all('td')[19].text.strip()
                #Lender = tablel.find_all('td')[21].text.strip()
                #CD = tablel.find_all('td')[23].text.strip()
            except:
                Business_Name = None
                Address = None
                Jobs_Retained=None
                Date_Approved=None
                



            info = ([Business_Name,Address,Jobs_Retained,Date_Approved])

            thewriter.writerow(info)