import requests
import bs4
import pandas as pd
import matplotlib.pyplot as plt

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                         ' Chrome/91.0.4472.124 Safari/537.36'}

# Scrapping iphone sales datas from ebay
GB_list = [[256, 'GB'], [512, 'GB'], [1, 'TB']]
prices_dict = {}
for gb in GB_list:
    response = requests.get('https://www.ebay.co.uk/sch/i.html?_from=R40&_nkw=iphone+15+pro+max+&_'
                            'sacat=9355&Brand=Apple&_udlo=600&Model=Apple%2520iPhone%252015%2520Pro%252'
                            '0Max&LH_PrefLoc=1&_ipg=240&LH_Complete=1&LH_Sold=1&LH_ItemCondition=1000&r'
                            f't=nc&Storage%2520Capacity={gb[0]}%2520{gb[1]}&_dcat=9355', headers=headers)

    print(f'Connection status:{response.status_code}')

    soup = bs4.BeautifulSoup(response.text, 'lxml')
    res = soup.find_all('div', {'class': 's-item__details clearfix'})

    prices = []
    for i in res:
        if i.find('span', {'class': 'POSITIVE'}) is not None:
            price = i.find('span', {'class': 'POSITIVE'}).text
            prices.append(float(price.replace('£', '').replace(',', '')))

    prices_dict[f'{gb[0]}{gb[1]}'] = prices


# Making Dataframe from scrapped datas
df = pd.DataFrame(prices_dict)

# Average,min and max iphone price
avg = []
for i in df:
    print(f'Iphone{i} average price:{df[i].mean().round(2)}')
    print(f'Iphone{i} min price:{df[i].min().round(2)}')
    print(f'Iphone{i} max price:{df[i].max().round(2)}')


fig = plt.figure(figsize=(14, 7))
ax1 = fig.add_subplot([0.05, 0.1, 0.4, 0.35])
ax2 = fig.add_subplot([0.05, 0.6, 0.4, 0.35])
ax3 = fig.add_subplot([0.55, 0.1, 0.4, 0.75])

ax1.bar(df.columns, df.mean())
ax2.bar(df.columns, df.min())
ax3.bar(df.columns, df.max())

plt.show()
