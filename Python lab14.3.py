import json
import matplotlib.pyplot as plt

# Зчитування даних з JSON-файлу
with open('data.json') as json_file:
    data = json.load(json_file)

# Розпаковка даних
teams = [item['Name'] for item in data]
points = [item['Points'] for item in data]

# Побудова кругової діаграми
plt.figure(figsize=(8, 8))
plt.pie(points, labels=teams, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Розподіл очок серед команд')
plt.legend()
plt.show()