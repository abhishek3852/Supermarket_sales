import pandas as pd
import matplotlib as mtl
import numpy as np
import seaborn as se

a = pd.read_csv(r"C:\Users\ACER\OneDrive\Desktop\sales_supermarket.csv")
print(a.info())

sales_category = a.groupby(["category","sub_category"])["sales"].sum().sort_values(ascending= False)
print(sales_category)

max_Sales = max(sales_category)
filter_max_sales = list(filter (lambda x: x== max_Sales, sales_category))
print(filter_max_sales)

customer_total_spending = a.groupby(["customer_name","city","category"])["sales"].sum()
most_sales = customer_total_spending.idxmax()
most_sales_value = customer_total_spending.max()
print(f'THe customer with most sales:{most_sales},THe value of his sales: {most_sales_value}')

buying_frequency = a.groupby(["customer_name","category"])["order_date"].count()
most_product_bought = buying_frequency.idxmax()
most_count = buying_frequency.max()
print(f'THe most order item bought: {most_product_bought}, Number of times it brought{most_count}')

profit_margin = a.groupby(["category", "sub_category"])["profit"].sum()

# Find the most profitable product (sub-category)
most_profitable_product = profit_margin.idxmax()
most_profitable_value = profit_margin.max()

print(f"Most Profitable Product: {most_profitable_product}, Profit: {most_profitable_value}")

average_frequency_order = a.groupby("customer_name")["order_id"].count()
average_sales = a.groupby("customer_name")["sales"].sum()
average_order = average_sales/average_frequency_order
print(f" THe average sales per customer is:{average_order}")

total_orders = a["order_id"].count()
total_customer = a["customer_name"].nunique()
Order_per_customer = total_orders/total_customer
print(f"The total orders per customer is {Order_per_customer}")

product_per_order = a.groupby("order_id")["sub_category"].count().mean()
print(f"The average number of products per order is: {product_per_order}")

profit_total = a["profit"].sum()
print(profit_total)

profit_category = a.groupby(["category","sub_category"])["profit"].sum()
sales_category = a.groupby(["category","sub_category"])["sales"].sum()
profit_margins = (profit_category/sales_category)*100
print(f"The profit margin per product is :{profit_margins}")

profit_margin = a.groupby(["category", "sub_category"])["profit"].sum()
least_profitable_product = profit_margin.idxmin()
least_profitable_value = profit_margin.min()
print(f"least Profitable Product: {least_profitable_product}, Profit: {least_profitable_value}")

order_trend = a.groupby(["region","city"])["order_id"].count()
print(order_trend)




