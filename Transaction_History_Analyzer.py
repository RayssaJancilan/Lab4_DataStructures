LAST_NAME = "Jancilan"
SEED_NUM = 8
FAVORITE_ARTIST = "Rico Blanco"

customers = ["C1", "C2", "C3", "C4", "C5"]

products = [
    "NOTEBOOK",
    "PEN",
    "USB",
    "HEADPHONES",
    "CALCULATOR"
]

prices = {
    "NOTEBOOK": 50,
    "PEN": 15,
    "USB": 250,
    "HEADPHONES": 500,
    "CALCULATOR": 350
}

def character_value(text, index):
    character = text[index % len(text)]
    return ord(character)


def generate_quantity(index, product_index):
    combined = (
        character_value(LAST_NAME, index)
        + character_value(FAVORITE_ARTIST, product_index)
        + SEED_NUM
        + index
        + product_index
    )
    return (combined % 5) + 1


transactions = []

for i in range(10):
    customer = customers[i % len(customers)]
    product_index = (i + SEED_NUM) % len(products)
    product = products[product_index]

    quantity = generate_quantity(i, product_index)
    unit_price = prices[product]
    total = quantity * unit_price

    transaction = {
        "transaction_id": f"T{i + 1}",
        "customer": customer,
        "product": product,
        "quantity": quantity,
        "unit_price": unit_price,
        "total": total
    }

    transactions.append(transaction)



print("=" * 65)
print("TRANSACTION DATA ORGANIZER")
print("=" * 65)

print("\nSTUDENT INPUTS")
print("Last Name:", LAST_NAME)
print("Seed Number:", SEED_NUM)
print("Favorite Artist:", FAVORITE_ARTIST)

print("\nGENERATED TRANSACTION RECORDS")
print("-" * 65)

for transaction in transactions:
    print(
        f"{transaction['transaction_id']} | "
        f"Customer: {transaction['customer']} | "
        f"Product: {transaction['product']} | "
        f"Quantity: {transaction['quantity']} | "
        f"Unit Price: PHP {transaction['unit_price']:.2f} | "
        f"Total: PHP {transaction['total']:.2f}"
    )



repeated_transaction = transactions[0].copy()
repeated_transaction["transaction_id"] = "T11"
transactions.append(repeated_transaction)

print("\nREPEATED TRANSACTION CHECK")
print("-" * 65)

seen = {}
duplicate_count = 0

for transaction in transactions:
    key = (
        transaction["customer"],
        transaction["product"],
        transaction["quantity"],
        transaction["unit_price"],
        transaction["total"]
    )

    if key in seen:
        duplicate_count += 1
        print(
            f"Repeated purchase: {transaction['transaction_id']} "
            f"matches the purchase details of {seen[key]}"
        )
    else:
        seen[key] = transaction["transaction_id"]

print("Repeated purchase records detected:", duplicate_count)
print("Total transaction records:", len(transactions))



print("\nTRANSACTION VALUES")
print("-" * 65)

for transaction in transactions:
    transaction["total"] = (
        transaction["quantity"] * transaction["unit_price"]
    )

    print(
        transaction["transaction_id"],
        "- PHP",
        f"{transaction['total']:.2f}"
    )



print("\nCUSTOMER SUMMARIES")
print("-" * 65)

customer_summary = {}

for customer in customers:
    customer_summary[customer] = {
        "transactions": 0,
        "items": 0,
        "spending": 0
    }

for transaction in transactions:
    customer = transaction["customer"]

    customer_summary[customer]["transactions"] += 1
    customer_summary[customer]["items"] += transaction["quantity"]
    customer_summary[customer]["spending"] += transaction["total"]

for customer, summary in customer_summary.items():
    print(
        f"{customer}: "
        f"Transactions = {summary['transactions']}, "
        f"Items = {summary['items']}, "
        f"Total Spending = PHP {summary['spending']:.2f}"
    )



print("\nPRODUCT SUMMARIES")
print("-" * 65)

product_summary = {}

for product in products:
    product_summary[product] = {
        "transactions": 0,
        "quantity_sold": 0,
        "revenue": 0
    }

for transaction in transactions:
    product = transaction["product"]

    product_summary[product]["transactions"] += 1
    product_summary[product]["quantity_sold"] += transaction["quantity"]
    product_summary[product]["revenue"] += transaction["total"]

for product, summary in product_summary.items():
    print(
        f"{product}: "
        f"Transactions = {summary['transactions']}, "
        f"Quantity Sold = {summary['quantity_sold']}, "
        f"Revenue = PHP {summary['revenue']:.2f}"
    )



print("\nORDERED RESULTS: HIGHEST TRANSACTION VALUE FIRST")
print("-" * 65)

ordered_transactions = sorted(
    transactions,
    key=lambda transaction: transaction["total"],
    reverse=True
)

for transaction in ordered_transactions:
    print(
        f"{transaction['transaction_id']} | "
        f"{transaction['customer']} | "
        f"{transaction['product']} | "
        f"PHP {transaction['total']:.2f}"
    )



total_records = len(transactions)
total_revenue = sum(t["total"] for t in transactions)
total_items = sum(t["quantity"] for t in transactions)

average_transaction = (
    total_revenue / total_records if total_records else 0
)

highest_transaction = max(
    transactions,
    key=lambda transaction: transaction["total"]
)

lowest_transaction = min(
    transactions,
    key=lambda transaction: transaction["total"]
)

top_customer = max(
    customer_summary,
    key=lambda customer: customer_summary[customer]["spending"]
)

top_product = max(
    product_summary,
    key=lambda product: product_summary[product]["revenue"]
)

print("\n" + "=" * 65)
print("FINAL CONSOLIDATED TRANSACTION REPORT")
print("=" * 65)

print("Student:", LAST_NAME)
print("Seed Number:", SEED_NUM)
print("Favorite Artist:", FAVORITE_ARTIST)
print("Number of Unique Customer Labels:", len(customers))
print("Number of Product Types:", len(products))
print("Total Transaction Records:", total_records)
print("Repeated Purchase Records:", duplicate_count)
print("Total Items Sold:", total_items)
print(f"Total Revenue: PHP {total_revenue:.2f}")
print(f"Average Transaction Value: PHP {average_transaction:.2f}")

print(
    f"Highest Transaction: {highest_transaction['transaction_id']} "
    f"({highest_transaction['product']}) - "
    f"PHP {highest_transaction['total']:.2f}"
)

print(
    f"Lowest Transaction: {lowest_transaction['transaction_id']} "
    f"({lowest_transaction['product']}) - "
    f"PHP {lowest_transaction['total']:.2f}"
)

print(
    f"Highest-Spending Customer: {top_customer} - "
    f"PHP {customer_summary[top_customer]['spending']:.2f}"
)

print(
    f"Highest-Revenue Product: {top_product} - "
    f"PHP {product_summary[top_product]['revenue']:.2f}"
)

print("=" * 65)
print("END OF REPORT")
print("=" * 65)
