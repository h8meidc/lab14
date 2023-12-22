import pandas as pd
import matplotlib.pyplot as plt


file_path = 'populationusaukr.csv'
df = pd.read_csv(file_path)


years = range(2003, 2023)

population_us = df[df['Country Name'] == 'United States'].iloc[:, 4:].values.flatten()
population_ukraine = df[df['Country Name'] == 'Ukraine'].iloc[:, 4:].values.flatten()


plt.figure(figsize=(10, 6))
plt.plot(years, population_us, label='United States', marker='o')
plt.plot(years, population_ukraine, label='Ukraine', marker='o')
plt.xlabel('Рік')
plt.ylabel('Population, total')
plt.title('Динаміка населення')
plt.legend()


plt.xticks(years)

plt.show()


plt.figure(figsize=(10, 6))

plt.bar(years, population_us, width=0.35, label='United States', color='skyblue')
plt.bar(years, population_ukraine, width=0.35, label='Ukraine', color='orange')

plt.xlabel('Рік')
plt.ylabel('Population, total')
plt.title('Стовпчаста діаграма для обох країн')
plt.legend()


plt.xticks(years)

plt.show()
