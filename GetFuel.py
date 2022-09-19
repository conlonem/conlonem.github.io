import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel('price_history_checks_august2022.xlsx')
data=data.loc[data['FuelCode'] == 'E10']
data['PriceUpdatedDate']=pd.to_datetime(data['PriceUpdatedDate'])
data['PriceDate']=data['PriceUpdatedDate'].dt.date
data = data[data['PriceUpdatedDate'].dt.strftime('%Y-%m-%d') == "2022-01-08"]
data = data.loc[(data['Postcode'] >= 2287) & (data['Postcode'] <= 2322)]
data=data.dropna()
print(data)
data.plot(x ='ServiceStationName', y='Price', kind='bar')
plt.show()