# Utility functions for data conversion and filtering
orders = [
    {"customer_id": 1, "product": "Rice", "quantity": 2, "price": 1200},
    {"customer_id": 2, "product": "Beans", "quantity": 1, "price": 800},
    {"customer_id": 3, "product": "Yam", "quantity": 3, "price": 1500},
    {"customer_id": 1, "product": "Palm Oil", "quantity": 1, "price": 1000},
    {"customer_id": 4, "product": "Bread", "quantity": 2, "price": 700},
    {"customer_id": 5, "product": "Eggs", "quantity": 12, "price": 100},
    {"customer_id": 2, "product": "Spaghetti", "quantity": 4, "price": 500},
    {"customer_id": 3, "product": "Tomatoes", "quantity": 6, "price": 200},
    {"customer_id": 6, "product": "Fish", "quantity": 2, "price": 2500},
    {"customer_id": 7, "product": "Chicken", "quantity": 1, "price": 3500},
    {"customer_id": 1, "product": "Maggi", "quantity": 10, "price": 50},
    {"customer_id": 8, "product": "Peppers", "quantity": 5, "price": 100},
    {"customer_id": 9, "product": "Milk", "quantity": 2, "price": 1200},
    {"customer_id": 4, "product": "Sugar", "quantity": 1, "price": 700},
    {"customer_id": 2, "product": "Groundnut Oil", "quantity": 1, "price": 2500},
    {"customer_id": 10, "product": "Indomie", "quantity": 5, "price": 150},
    {"customer_id": 5, "product": "Bread", "quantity": 1, "price": 700},
    {"customer_id": 3, "product": "Rice", "quantity": 1, "price": 1200},
    {"customer_id": 6, "product": "Soft Drink", "quantity": 6, "price": 200},
    {"customer_id": 1, "product": "Yoghurt", "quantity": 2, "price": 500},
]

def view_orders():
    print(orders)
pass


def calculate_order_total(order):
    return sum(item['price'] * item['quantity'] for item in order['items'])
pass

def convert_currency(price):
    rate = 1490
    dollar_price = price / rate
    return dollar_price
pass

def apply_discouunt(order):
    if order['quantity'] > 50 | order['price'] > 500000:
        order['price'] = order['price'] * 0.9
        return order
    return order
pass

def filter_large_orders(order, top):
    if order['price'] * order['quantity'] > top:
        return True 
    else:
        return False
pass

def total_sold_products(orders):
    total_sold = sum(order['quantity'] for order in orders)
    return total_sold
pass


def most_sold_product(orders):
    product_sales = {}
    for order in orders:
        product = order['product']
        quantity = order['quantity']
        if product in product_sales:
            product_sales[product] += quantity
        else:
            product_sales[product] = quantity
    most_sold = max(product_sales, key=product_sales.get)
    return most_sold
pass


def revenue_per_customer(order):
    revenue = {}
    for order in orders:
        cust_id = order['customer_id']
        total = float(order['price']) * int(order['quantity'])
        revenue[cust_id] = revenue.get(cust_id, 0) + total
    return revenue
pass 



# def generate_report():
#     total_sold = total_sold_products(orders)
#     most_sold = most_sold_product(orders)
#     rev_per_cust = revenue_per_customer(orders)

#     report = {"total_sold: ": total_sold, "most_sold: ": most_sold, "revenue_per_customer ": rev_per_cust}