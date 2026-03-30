#Input & Variables
customer = input("Enter customer name: ")
product = input("Enter product name: ")
price = float(input("Enter price per unit (KZT): "))
quantity = int(input("Enter quantity: "))

#Calculations
subtotal = price * quantity
if subtotal > 5000:
    discount = subtotal * 0.10
else:
    discount = 0

total = subtotal - discount

#Formatted Output
print("=" * 30)
print('SHOP RECEIPT')
print("=" * 30)
print(f"Customer :  {customer}")
print(f"Product : {product}")
print(f"Price : {price} KZT")
print(f"Quantity : {quantity}")
print("-" * 30)
print(f"Subtotal : {subtotal} KZT")
print(f"Discount : {discount} KZT")
print(f"Total : {total} KZT")
print("=" * 30)

#Comparison
print("Discount applied:", subtotal > 5000)
print("Paid more than 3000:", total > 3000)