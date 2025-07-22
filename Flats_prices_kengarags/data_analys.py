import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from SQL_quarys import cur,conn
from sklearn.linear_model import LinearRegression

quary = 'SELECT * FROM public.kengarags_prices'
df = pd.read_sql(quary,conn)

df = df[['rooms', 'square_meters', 'floor_', 'total_floors',
       'project', 'type_', 'price', 'price_per_m2', 'created_at']]
df['created_at'] = pd.to_datetime(df['created_at'])
df['year_month'] = df['created_at'].dt.to_period('M')




fig,axes = plt.subplots(2,2, figsize=(12, 8))
ax1,ax2,ax3,ax4 = axes.flatten()
# how prices per square meters have changed
grouped = df.groupby(['rooms','year_month']).mean(numeric_only=True)
grouped = grouped.reset_index()


for room in sorted(grouped['rooms'].unique()):
    data = grouped[grouped['rooms'] == room]
    data['year_month'] = data['year_month'].astype(str)
    ax1.plot(data['year_month'], data['price_per_m2'], label=f'{room} rooms')

ax1.set_xlabel('Month')
ax1.set_ylabel('Price per m²')
ax1.set_title('Average Price per m² by Rooms and Month')
ax1.legend()
ax1.grid(True)



# how prices per square meters have changed per each project

grouped = df.groupby(['year_month', 'project'])
filtered = grouped.filter(lambda x: len(x) >= 5)
filtered = filtered.groupby(['year_month', 'project'])['price_per_m2'].mean().reset_index()



for project in sorted(filtered['project'].unique()):
       if project != '467.':
              data = filtered[filtered['project'] == project]
              data['year_month'] = data['year_month'].astype(str)
              ax2.plot(data['year_month'], data['price_per_m2'], label=f'{project} project')



ax2.set_xlabel('Month')
ax2.set_ylabel('Price per m²')
ax2.set_title('Average Price per m² by Project and Month')
ax2.legend()
ax2.grid(True)

# prices per square meters per each floor
floor_group = df.groupby('floor_')['price_per_m2'].mean().reset_index()

ax3.plot(floor_group['floor_'], floor_group['price_per_m2'], marker='o')
ax3.set_xlabel('floor')
ax3.set_ylabel('price_per_m2')
ax3.set_title('Price per square meters per each floor')
ax3.grid(True)


# Price vs Area
# remove outliers
filtered = df[df['price'] < 200000]
ax4.scatter(filtered['square_meters'], filtered['price'], alpha=0.5)
ax4.set_xlabel('Area (m²)')
ax4.set_ylabel('Price (€)')
ax4.set_title('Price vs Area')
ax4.grid(True)


# MSE model
X = filtered[['square_meters']]  # 2D (n_samples, 1)
y = filtered['price']
model = LinearRegression()
model.fit(X,y)
prediction = model.predict(X)
ax4.plot(filtered['square_meters'], prediction, color='red')


plt.tight_layout()
plt.savefig('flats_price_analysis.png',dpi=300)




