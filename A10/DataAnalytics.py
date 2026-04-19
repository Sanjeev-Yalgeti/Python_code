import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import '/Automobile_data.xlsx' as dataset
df=pd.read_excel('Automobile_data.xlsx')
#Print first 5
print("First 5\n",df.head())
#last 5
print("Last 5\n",df.tail())
#clean empty values
df.dropna(inplace=True)
#to csv
df.to_csv("Automobile_cleaned.csv", index=False)
#find most expensive car comapny name
expensive=np.max(df["price"])
exp_company=df[df["price"]==expensive]["company"]
print("Most expensive Car Company Name\n",exp_company)
#Print Toyota details
print("All Toyota Car Details\n",df[df["company"]=="toyota"])
#Count Total cars per comapny
counts=df["company"].value_counts()
print("Total cars per company\n",counts)
#Each company highest price
highest_price = df.loc[df.groupby("company")["price"].idxmax()]
print("\nHighest price car of each company:\n", highest_price)
# 7. Average mileage of each company
avg_mileage = df.groupby("company")["average-mileage"].mean()
print("Average mileage opf each company\n",avg_mileage)
#bar graph
avg_price=df.groupby("company")["price"].mean()
avg_price.plot(kind="bar")
plt.title("Average Price by Company")
plt.xlabel("Company")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.show()

#histogram
plt.hist(df["average-mileage"],bins=10)
plt.title("Mileage Distribution")
plt.show()
