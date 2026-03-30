import pandas
import pandas as pd
df=pd.read_csv("ITA105_Lab_1.csv")
print("Kích thước dữ liệu:",{df.shape})
print("Thống kê mô tả của các cột số:")
print(df.describe())
print("Giá trị thiếu trong các cột:")
print(df.isnull().sum())
mean_price=df["Price"].mean()
print("mean price:",mean_price)
df["Price"].fillna(mean_price)
mean_stockquantity=df["StockQuantity"].mean()
print("mean stockquantity:",mean_stockquantity)
df["StockQuantity"].fillna(mean_stockquantity)
mode_categoty=df["Category"].mode()[0]
df["Category"]=df["Category"].fillna(mode_categoty)
print(df)

print("Số dòng StockQuantity âm:",len(df[df["StockQuantity"]<0]))
print("Số dòng Price âm:",len([df["Price"]<0]))
df=df[df["StockQuantity"]>=0]
df=df[df["Price"]>0]
print("Kích thước dữ liệu sau khi xử lí giá trị bất hợp lí:",{df.shape})

df=df[(df["Rating"]>=0) & (df["Rating"]<=5)]
print("Kích thước dữ liệu sau khi lọc Rating lỗi:",{df.shape})
print("Giá trị Rating lớn nhất sau khi lọc:",df["Rating"].max())

df["Price_Smoothed"]=df["Price"].rolling(window=5,min_periods=1).mean()


import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
plt.plot(df["Price"],color="lightgray",label="Giá gốc")
plt.plot(df["Price_Smoothed"],color="red",label="Giá làm mượt")
plt.title("Biểu đồ làm mượt dữ liệu")
plt.legend()
plt.show()


df["Category"]=df["Category"].str.lower()
df["Description"]=df["Description"].str.strip()
df["Price"]=df["Price"]*26271
print(df)


