import pandas as pd
import matplotlib.pyplot as plt

# Data Preparstion
df = pd.read_excel('Sales_v1.xlsx')
print(df.columns)
print(df.info())


# Let's sort orders by date
date_index = pd.DatetimeIndex(df['Date'])
df.index = date_index
df = df.sort_index()

# How many units been ordered to each country and how much they spent?
country_units = df[['Country','Units Sold']].groupby('Country').sum()
print('Total units ordered per country')
print(country_units)

country_sales = df[['Country',' Sales']].groupby('Country').sum()
formatted = country_sales[' Sales'].apply(lambda x: f'{x:,.0f}')
print('Total sales per country')
print(formatted)


fig,[ax1,ax2] = plt.subplots(1,2,figsize=(14,7))
ax1:plt.Axes
ax1.pie(country_units['Units Sold'],labels=country_units.index,autopct='%1.2f%%' )
ax1.set_title('Units Sold',color='green')
ax2.pie(country_sales[' Sales'],labels=country_sales.index,autopct='%1.2f%%',colors=['green','red','pink','orange','blue'] )
ax2.set_title('Sales',color='green')


#Which product is the cheapest to manufacturing?
products = df[['Product', 'Manufacturing Price']].drop_duplicates().reset_index(drop=True)
print('Manufacture price')
print(products)

#Which product has more sales?
products_sold = df[['Product', 'Units Sold']].groupby('Product').sum()
print('Total units sold')
print(products_sold)

#which product made more profit?
products_profit = df[['Product', 'Profit']].groupby('Product').sum()
print('Total profit made')
print(products_profit)


fig = plt.figure(figsize=(14, 7))
ax1 = fig.add_subplot([0.05,0.1,0.4,0.35])
ax2 = fig.add_subplot([0.05,0.6,0.4,0.35])
ax3 = fig.add_subplot([0.55,0.1,0.4,0.75])

ax1.bar(products_sold.index, products_sold['Units Sold'], color='skyblue')
ax1.set_title('Units Sold')
ax1.tick_params(axis='x', rotation=45)

ax2.bar(products['Product'], products['Manufacturing Price'], color='lightcoral')
ax2.set_title('Manufacturing Price')
ax2.tick_params(axis='x', rotation=45)

ax3.bar(products_profit.index, products_profit['Profit'], color='mediumseagreen')
ax3.set_title('Profit')
ax3.tick_params(axis='x', rotation=45)
ax3.ticklabel_format(style='plain', axis='y')


#Is any of our products seasonal?
df = df[['Product','Units Sold','Month Name']][df['Year']==2014]
fig,axes = plt.subplots(2,3,figsize=(14, 7))
ax1,ax2,ax3,ax4,ax5,ax6 = axes.flatten()

Velo = df[['Units Sold','Month Name']][df['Product']=='Velo'].groupby('Month Name').sum('Units Sold')
Amarilla = df[['Units Sold','Month Name']][df['Product']=='Amarilla'].groupby('Month Name').sum('Units Sold')
Carretera = df[['Units Sold','Month Name']][df['Product']=='Carretera'].groupby('Month Name').sum('Units Sold')
Montana = df[['Units Sold','Month Name']][df['Product']=='Montana'].groupby('Month Name').sum('Units Sold')
Paseo = df[['Units Sold','Month Name']][df['Product']=='Paseo'].groupby('Month Name').sum('Units Sold')
VTT = df[['Units Sold','Month Name']][df['Product']=='VTT'].groupby('Month Name').sum('Units Sold')

datasets = [Velo, Amarilla, Carretera, Montana, Paseo, VTT]
names = ['Velo', 'Amarilla', 'Carretera', 'Montana', 'Paseo', 'VTT']
for ax, data, name in zip(axes.flatten(), datasets, names):
    ax.plot(data)
    ax.set_title(name,color='red')
    ax.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()


