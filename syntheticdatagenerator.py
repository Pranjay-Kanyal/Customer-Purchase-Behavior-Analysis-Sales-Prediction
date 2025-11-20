# src/generate_synthetic_data.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_synthetic_retail(n_customers=2000, n_tx=50000, start_date='2024-01-01'):
    np.random.seed(42)
    random.seed(42)
    start = datetime.fromisoformat(start_date)
    customer_ids = [f"C{1000+i}" for i in range(n_customers)]
    product_list = [f"Product_{i}" for i in range(1,201)]  # 200 products
    rows = []
    for i in range(n_tx):
        cust = random.choice(customer_ids)
        invoice_no = f"INV{100000 + i}"
        invoice_date = start + timedelta(days=int(np.random.exponential(scale=90)))
        qty = np.random.poisson(2) + 1
        unit_price = round(np.random.choice(np.linspace(5,200,200)) * (1 + np.random.normal(0,0.05)), 2)
        desc = random.choice(product_list)
        rows.append([cust, invoice_no, invoice_date.strftime("%Y-%m-%d %H:%M:%S"), qty, unit_price, desc])
    df = pd.DataFrame(rows, columns=['CustomerID','InvoiceNo','InvoiceDate','Quantity','UnitPrice','Description'])
    df['Sales'] = df['Quantity'] * df['UnitPrice']
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    return df

if __name__ == "__main__":
    df = generate_synthetic_retail()
    df.to_csv("D:\customer-behavior-project\synthetic_retail.csv", index=False)
    print("Saved data/synthetic_retail.csv (rows: {})".format(len(df)))
