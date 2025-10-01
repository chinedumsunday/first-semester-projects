# Code to generate dictionary summary reports
from utils import total_sold_products, most_sold_product, revenue_per_customer
from utils import orders
import json

def generate_report():
    total_sold = total_sold_products(orders)
    most_sold = most_sold_product(orders)
    rev_per_cust = revenue_per_customer(orders)


    report = {"total_sold": total_sold, "most_sold": most_sold, "revenue_per_customer": rev_per_cust}
    with open('report.json', 'w') as f:
        json.dump(report, f)
    
    print("\n📊 ===== MiniMart Sales Report =====")
    print(f" Total Products Sold: {total_sold}")
    print(f" Most Popular Product: {most_sold}")
    print("\n Revenue per Customer:")
    print("----------------------------------")
    for cust_id, revenue in rev_per_cust.items():
        print(f"👤 Customer {cust_id:<2} | ₦{revenue:,.2f}")

    print("==================================\n")

    
pass