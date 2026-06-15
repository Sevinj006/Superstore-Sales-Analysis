import pandas as pd 
df= pd.read_excel("superstoredataset.xlsx")

#AVERAGE DELIVERY DAYS
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

df["Delivery Days"] = (df["Ship Date"] - df["Order Date"]).dt.days

df["Delivery Days"].mean()

print("Average Delivery Days:", df["Delivery Days"].mean())


#Number of unprofitable orders
df[df["Profit"] < 0]
print("Number of unprofitable orders:", len(df[df["Profit"] < 0]))

#Total profit by category found
df.groupby("Category")["Profit"] \
  .sum() \
  .sort_values(ascending=False)
print("Total profit by category:")
print(df.groupby("Category")["Profit"].sum().sort_values(ascending=False))

#top 10 customers 
df.groupby("Customer Name")["Sales"] \
  .sum() \
  .sort_values(ascending=False) \
  .head(10)
print("Top 10 customers by sales:")
print(df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(10))