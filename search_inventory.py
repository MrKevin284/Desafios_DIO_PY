def search_products_by_price(min_price):
    found_products = []
    for product_name, product_info in inventory.items():
        if product_info["price"] >= min_price:
            found_products.append((product_info["id"], product_name))
    return found_products

inventory = {
    "Product A": {
        "id": 1,
        "price": 10.0,
        "quantity": 10
    },
    "Product B": {
        "id": 2,
        "price": 15.0,
        "quantity": 20
    },
    "Product C": {
        "id": 3,
        "price": 8.0,
        "quantity": 15
    }
}

min_price = float(input())
found_products = search_products_by_price(min_price)

if found_products:
    print("Products Found:")
    for product in found_products:
        print(f"{product[0]} - {product[1]}")
else:
    print("No product found.")
