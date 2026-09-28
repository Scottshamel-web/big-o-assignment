products = [
    {"name": "Laptop", "price": 999.99, "category": "electronics", "in_stock": True},
    {"name": "Python Book", "price": 39.99, "category": "books", "in_stock": True},
    {"name": "Headphones", "price": 149.99, "category": "electronics", "in_stock": False},
    {"name": "Desk Lamp", "price": 29.99, "category": "home", "in_stock": True},
    {"name": "AI Textbook", "price": 89.99, "category": "books", "in_stock": True},
    {"name": "Monitor", "price": 349.99, "category": "electronics", "in_stock": True},
    {"name": "Notebook", "price": 4.99, "category": "office", "in_stock": True},
    {"name": "Keyboard", "price": 79.99, "category": "electronics", "in_stock": False},
]


# 1. Get all in-stock products
in_stock_products = list(
    filter(lambda product: product["in_stock"], products)
)

print("1. In-stock products:")
print(in_stock_products)


# 2. Add a discounted_price field with 10% off
# Creates new dictionaries without modifying the originals
discounted_products = list(
    map(
        lambda product: {
            **product,
            "discounted_price": round(product["price"] * 0.90, 2)
        },
        products
    )
)

print("\n2. Products with discounted prices:")
print(discounted_products)


# 3. Get electronics under $200
electronics_under_200 = list(
    filter(
        lambda product:
            product["category"] == "electronics"
            and product["price"] < 200,
        products
    )
)

print("\n3. Electronics under $200:")
print(electronics_under_200)


# 4. Sort products by price, lowest first
sorted_by_price = sorted(
    products,
    key=lambda product: product["price"]
)

print("\n4. Products sorted by price:")
print(sorted_by_price)


# 5. Calculate total value of all in-stock products
total_in_stock_value = sum(
    product["price"]
    for product in products
    if product["in_stock"]
)

print("\n5. Total value of in-stock products:")
print(round(total_in_stock_value, 2))


# 6. Group products by category
categories = {
    product["category"]
    for product in products
}

grouped_by_category = {
    category: [
        product
        for product in products
        if product["category"] == category
    ]
    for category in categories
}

print("\n6. Products grouped by category:")
print(grouped_by_category)


# Verify original data was not modified
print("\nOriginal products:")
print(products)