import requests
import bs4
import pandas as pd
import matplotlib.pyplot as plt

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Referer': 'https://www.ebay.co.uk/',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br'
}
# Scrapping iphone sales datas from ebay
GB_list = [['256', 'GB'], [512, 'GB'], [1, 'TB']]
prices_dict = {}
for gb in GB_list:
    response = requests.get('https://www.ebay.co.uk/sch/i.html?_from=R40&_nkw=iphone+15+pro+max&_'
                            'sacat=0&_oaa=1&Model=Apple%2520iPhone%252015%2520Pro%2520Max&LH_Sold=1&LH_'
                            f'Complete=1&_udlo=600&rt=nc&Storage%2520Capacity={gb[0]}%2520{gb[1]}&_dcat=9355', headers=headers)



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

# Bar plot for mean values
ax1.bar(df.columns, df.mean(), color='skyblue', edgecolor='black')
ax1.set_title('Average Values')
ax1.set_ylabel('Mean')
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Bar plot for minimum values
ax2.bar(df.columns, df.min(), color='lightgreen', edgecolor='black')
ax2.set_title('Minimum Values')
ax2.set_ylabel('Min')
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Bar plot for maximum values
ax3.bar(df.columns, df.max(), color='salmon', edgecolor='black')
ax3.set_title('Maximum Values')
ax3.set_ylabel('Max')
ax3.grid(axis='y', linestyle='--', alpha=0.7)

# General plot styling
plt.tight_layout()
plt.show()
