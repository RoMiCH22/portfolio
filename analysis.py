#Пример 2: Анализ данных с использованием Pandas
import pandas as pd
import matplotlib.pyplot as plt

# Загружаем данные
data = pd.read_csv('data/dataset.csv')

# Статистики
print(data.describe())

# Визуализируем данные
data['column_name'].plot(kind='bar')
plt.show()
