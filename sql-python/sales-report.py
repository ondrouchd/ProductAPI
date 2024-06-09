import pandas as pd
import matplotlib.pyplot as plt

# read the sales data
df = pd.read_csv('assets/sales_data.csv')

# basic statistics
total_orders = len(df)
total_revenue = df['total_price'].sum()
average_price_per_unit = df['price_per_unit'].mean()

# chart the total revenue by month
df['order_date'] = pd.to_datetime(df['order_date'])
df['month'] = df['order_date'].dt.to_period('M')
monthly_orders = df.groupby('month').size()
monthly_orders.plot(kind='bar', title='Total Orders by Month')
plt.xlabel('Month')
plt.ylabel('Total Orders')
plt.show()

# top sellinbg products and catrgories
top_product = df.groupby('product')['quantity'].sum().idxmax()
top_category = df.groupby('category')['quantity'].sum().idxmax()

# generate the report
with open('assets/report.txt', 'w') as f:
    f.write(f'Total Orders: {total_orders}\n')
    f.write(f'Total Revenue: {total_revenue}\n')
    f.write(f'Average Price Per Unit: {average_price_per_unit:.2f}\n')
    f.write(f'Top Selling Product: {top_product}\n')
    f.write(f'Top Selling Category: {top_category}\n')	