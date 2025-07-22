import time
import numpy as np
import requests
import bs4
import re
import datetime
from SQL_quarys import add_to_database

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Referer': 'https://www.ss.lv/lv/archive',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br'}


for i in range(1,13):

    # one page with flat's advertisments
    response = requests.get(f'https://www.ss.lv/lv/archive/real-estate/flats/riga/kengarags/sell/page{i}.html',headers=headers)
    soup = bs4.BeautifulSoup(response.text,'lxml')

    pattern = re.compile(r'tr_\d+')
    lines = soup.find_all('tr',{'id': pattern})

    for line in lines:

        try:
            # one odvertisment
            new_link = 'https://www.ss.lv' + line.find('a').get('href')
            res = requests.get(new_link,headers=headers)
            soup = bs4.BeautifulSoup(res.text,'lxml')

            address = soup.find('td',{'class':'ads_opt','id':'tdo_11'}).text.replace(' [Karte]','').strip()
            rooms = soup.find('td',{'class':'ads_opt','id':'tdo_1'}).text.strip()
            square_meters = soup.find('td',{'class':'ads_opt','id':'tdo_3'}).text.split()[0].strip()
            floor = soup.find('td',{'class':'ads_opt','id':'tdo_4'}).text.split('/')[0].strip()
            total_floors = soup.find('td', {'class': 'ads_opt', 'id': 'tdo_4'}).text.split('/')[1].strip()
            project = soup.find('td',{'class':'ads_opt','id':'tdo_6'}).text.strip()
            type = soup.find('td', {'class': 'ads_opt', 'id': 'tdo_2'}).text.strip()
            price = (soup.find('td', {'class': 'ads_price', 'id': 'tdo_8'}).text.strip().split('€')[0].
                            replace(' ',''))
            price_per_m2 = (soup.find('td', {'class': 'ads_price', 'id': 'tdo_8'}).text.split('€')[1].
                            replace('(','').strip()).replace(' ','')
            date = soup.find('td', {'class': 'msg_footer', 'align':'right'}).text.split(' ')[1].strip()
            date_obj = datetime.datetime.strptime(date, "%d.%m.%Y")
            formatted_date = date_obj.strftime("%Y-%m-%d")

            add_to_database(address,rooms,square_meters,floor,total_floors,project,type,price,price_per_m2,formatted_date)
        except AttributeError:
            print('AttributeError')
            print(new_link)
            continue

    time.sleep(np.random.rand())

