#Task 1
store_info = ("FreshMart", "Astana, Respublika Ave 1", "+7 700 000 0000")
print("=" * 30)
print(store_info[0])
print(store_info[1])
print(store_info[2])
print("=" * 30)
print()

#Task 2
names = []
prices = []

while True:
    name = input("Enter product name (or 'done' to finish):")
    if name.lower() == 'done' :
        break
    price = float(input("Enter price:"))

    names.append(name)
    prices.append(price)

print("\n" + "-" * 30)
print(f"Your cart ({len(names)} items):")
print("-" * 30)

for i in range(len(names)):
    print(f"{names[i]} - {prices[i]} KZT")
print("-" * 30)
print()


#Task3
weekly_products = set()
while True:
    name = input("Enter product name (or 'done' to finish): ")
    if name.lower() == 'done':
        break
    weekly_products.add(name)

print(f"\nUnique products: {len(weekly_products)}")
print(weekly_products)
print()

#Task4
customer_name = input("Enter customer name: ")

subtotal = sum(prices)

if subtotal < 3000:
    discount_percent = 0
    discount_text = "No discount"
elif 3000 <= subtotal < 7000:
    discount_percent = 0.05
    discount_text = "Standard discount"
else:
    discount_percent = 0.15
    discount_text = "Premium discount"

discount_amount = subtotal * discount_percent
total = subtotal - discount_amount

receipt = {
    "customer": customer_name,
    "items": len(names),
    "subtotal": subtotal,
    "discount": discount_amount,
    "total": total,
    "discount_name": discount_text
}

print("\n" + "=" * 30)
print(f"RECEIPT - {store_info[0]}")
print("=" * 30)
print(f"Customer : {receipt['customer']}")
print(f"Items : {receipt['items']}")
print("-" * 30)

for i in range(len(names)):
    print(f"{names[i]} - {prices[i]} KZT")

print("-" * 30)
print(f"Subtotal : {receipt['subtotal']} KZT")
print(f"Discount : {receipt['discount']} KZT ({receipt['discount_name']})")
print(f"Total : {receipt['total']} KZT")
print("=" * 30)
