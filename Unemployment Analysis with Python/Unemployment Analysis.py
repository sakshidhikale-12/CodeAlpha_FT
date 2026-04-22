import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Unemployment in India.csv")
print("First 5 rows:")
print(df.head())
df.columns = df.columns.str.strip()

df.rename(columns={
    'Estimated Unemployment Rate (%)': 'Unemployment_Rate',
    'Estimated Employed': 'Employed',
    'Estimated Labour Participation Rate (%)': 'Labour_Rate'
}, inplace=True)


print("\n missing values:")
print(df.isnull().sum())


df.dropna(inplace=True)

df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)


df['Month'] = df['Date'].dt.month

plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Unemployment_Rate'])
plt.title("unemployment trend over time")
plt.xlabel("Date")
plt.ylabel("unemployment rate")
plt.xticks(rotation=45)
plt.show()


plt.figure(figsize=(12,5))
sns.barplot(x='Region', y='Unemployment_Rate', data=df)
plt.title("unemployment by state")
plt.xticks(rotation=90)
plt.show()


covid_df = df[df['Date'].dt.year == 2020]

plt.figure(figsize=(10,5))
plt.plot(covid_df['Date'], covid_df['Unemployment_Rate'])
plt.title("COVID impact on unemployment 2020")
plt.xticks(rotation=45)
plt.show()


plt.figure(figsize=(6,4))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation btween Features")
plt.show()
