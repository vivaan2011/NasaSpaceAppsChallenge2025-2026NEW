from matplotlib import pyplot as plt
import pandas as pd
import joblib
import numpy
import pickle

kepler_set = pd.read_csv('kepler_new.csv')

df = pd.DataFrame(kepler_set, columns =['kepler_name','koi_disposition','koi_pdisposition','koi_period','koi_duration','koi_depth'])
df = df.dropna()

sorted_name_df = df.sort_values(by=['kepler_name'])


print(sorted_name_df)

sorted_period = df.sort_values(ascending=False,by=['koi_period'])
sorted_period

orb_period = sorted_period.head(10)
orb_period

name = orb_period['kepler_name']
period = orb_period['koi_period']

plt.xlabel("Kepler Planet Name")
plt.xticks(rotation='vertical')
plt.ylabel("Orbital Period")


label = name
value = period 
plt.bar(label, value,width=0.5, color=('black','yellow','green','pink','blue')) #bar-graph

plt.savefig("bar.png")
plt.figure(figsize=(10,6))
scatter = plt.scatter(
    sorted_name_df['koi_period'],
    sorted_name_df['koi_duration'],
    c=sorted_name_df['koi_disposition'].map({'CONFIRMED':1,'CANDIDATE':2,'FALSE POSITIVE':0}),
    alpha=0.7, cmap='viridis', s=50
)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Orbital Period (days)')
plt.ylabel('Planet Radius (Earth radii)')
plt.colorbar(scatter, label='Disposition')
plt.title('Planet Radius vs Orbital Period')
plt.show()

sorted_name_df.to_csv('output_pandas.csv', index=False)

