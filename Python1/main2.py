# Task 1
name = input("Enter customer name: ")
subtotal = 0
count = 0

while True:
    product = input("Enter product name (or 'done' to finish): ")
    if product == "done":
        break

    price = int(input("Enter price: "))
    subtotal += price
    count += 1

print("\nCustomer :", name.upper())
print("Items :", count)
print("Subtotal :", float(subtotal), "KZT")

# Task 2
if subtotal < 3000:
    discount = 0.0
    label = "No discount"
elif 3000 <= subtotal < 7000:
    discount = subtotal * 0.05
    label = "5% discount"
else:
    discount = subtotal * 0.15
    label = "15% discount"

final_total = subtotal - discount

print("---------------------------------")
print("Discount tier :", label)
print("Discount :", float(discount), "KZT")
print("Total :", float(final_total), "KZT")

# Task 3
print("\nName uppercase :", name.upper())
print("Name lowercase :", name.lower())
print("Name length :", len(name))

if len(name) > 5:
    print("Long name")
else:
    print("Short name")