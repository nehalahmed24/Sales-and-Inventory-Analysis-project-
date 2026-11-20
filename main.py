import pandas as pd
print("SALES.CSV")
sales_df=pd.read_csv("data/sales.csv")
print(sales_df)
print("Display the first 5 rows ")
print(sales_df.head(5))
print("Display the shape")
print(sales_df.shape) 
print("Display column name")
print(sales_df.columns)
print("Display the data type")
print(sales_df.dtypes)
print("Display the data set information")
sales_df.info()
print("Display statistical information")
print(sales_df.describe())
print("Missing value in sale data set")
print(sales_df.isnull().sum())
print("Duplicates value")
print(sales_df.duplicated().sum())
print("convert date into date time")
sales_df['Date'] = pd.to_datetime(sales_df["Date"])
print(sales_df.dtypes)
print("create a column of month")
sales_df['Month'] = sales_df["Date"].dt.month
print(sales_df)
print("create a column of year")
sales_df['year'] = sales_df["Date"].dt.year
print(sales_df)


print("\nCUSTOMER.CSV")

customer_df = pd.read_csv("data/customer.csv") 
print(customer_df)
print("Display the first 5 rows ")
print(customer_df.head(5))
print("Display the shape")
print(customer_df.shape) 
print("Display column name")
print(customer_df.columns)
print("Display the data type")
print(customer_df.dtypes)
print("Display the data set information")
customer_df.info()
print("Display statistical information")
print(customer_df.describe())
print("Missing value in customer data set")
print(customer_df.isnull().sum())
print("Duplicates value")
print(customer_df.duplicated().sum())

print("\nINVENTORY.CSV")

inventory_df = pd.read_csv("data/inventory.csv")
print(inventory_df)
print("Display the first 5 rows ")
print(inventory_df.head(5))
print("Display the shape")
print(inventory_df.shape) 
print("Display column name")
print(inventory_df.columns)
print("Display the data type")
print(inventory_df.dtypes)
print("Display the data set information")
inventory_df.info()
print("Display statistical information")
print(inventory_df.describe())
print("Missing value in inventory data set")
print(inventory_df.isnull().sum())
print("Duplicates value")
print(inventory_df.duplicated().sum())

print("\nPRODUCT.CSV")

product_df = pd.read_csv("data/product.csv")
print(product_df)
print("Display the first 5 rows ")
print(product_df.head(5))
print("Display the shape")
print(product_df.shape) 
print("Display column name")
print(product_df.columns)
print("Display the data type")
print(product_df.dtypes)
print("Display the data set information")
product_df.info()
print("Display statistical information")
print(product_df.describe())
print("Missing value in product data set")
print(product_df.isnull().sum())
print("Duplicates value")
print(product_df.duplicated().sum())

merged_df = pd.merge(
    sales_df,
    customer_df, 
    on="Customer_ID"
)

print(merged_df)


final_df = pd.merge(
    merged_df,
    product_df,
    on="Product_ID"
)
print(final_df)


final_df["revenue"] = final_df["Quantity"] * final_df["Selling_Price"]
print(final_df)

final_df['Profit'] = final_df["Quantity"] * (final_df["Selling_Price"] - final_df["Cost_Price"])
print(final_df)
print("Total Revenue")
df=final_df["revenue"].sum()
print(df)

print("Total Profit")
df_profit=final_df["Profit"].sum()
print(df_profit)

print("Grouped of products")
group = final_df.groupby("Product_Name")["Quantity"].sum()
print(group)

print("Highest Quantity Value")
group = final_df.groupby("Product_Name")["Quantity"].sum()
print(group.max())

print("Name the product")
group = final_df.groupby("Product_Name")["Quantity"].sum()
print(group.idxmax())

print("City's highest revenue")
group = final_df.groupby("Month")["revenue"].sum()
print(group.idxmax())

print("Product generates highest profit")
group = final_df.groupby("Product_Name")["Profit"].sum()
print(group.idxmax())

inventory_merged_df= pd.merge(
    inventory_df,
    final_df,
    on="Product_ID"
)
print(inventory_merged_df)

print(inventory_merged_df["Current_Stock"] < inventory_merged_df["Reorder_Level"])

print(inventory_merged_df[inventory_merged_df["Current_Stock"] < inventory_merged_df["Reorder_Level"]])

print("remove duplicate columns")
print(inventory_merged_df[inventory_merged_df["Current_Stock"] < inventory_merged_df["Reorder_Level"]].drop_duplicates(subset=["Current_Stock","Reorder_Level"]))

inventory_merged_df["Shortage"] = (inventory_merged_df["Reorder_Level"] - inventory_merged_df["Current_Stock"])
print(inventory_merged_df)

print(inventory_merged_df["Current_Stock"]<=inventory_merged_df["Reorder_Level"])

print(inventory_merged_df[inventory_merged_df["Current_Stock"]<=inventory_merged_df["Reorder_Level"]])

subset = inventory_merged_df[(inventory_merged_df["Current_Stock"]<=inventory_merged_df["Reorder_Level"])
].drop_duplicates(subset=["Product_ID"])[["Product_ID", "Product_Name", "Current_Stock", "Reorder_Level"]]
print(subset)

# create inventory column in inventory_merged_df data frame

print("Total inventory value")
inventory_merged_df["Inventory_Value"] = (
    inventory_merged_df["Current_Stock"] * inventory_merged_df["Cost_Price"]
)

inventory_value = inventory_merged_df.drop_duplicates(
    subset=["Product_ID"]
)["Inventory_Value"].sum()

print(inventory_value)

print("Revenue")
print(final_df["revenue"].sum())

print("Total Gross profit")
print(final_df["Profit"].sum())

print("Total sales order ")
print(final_df ["Order_ID"].count() )

inventory_merged_df.to_excel("business_summary.xlsx",index=False)