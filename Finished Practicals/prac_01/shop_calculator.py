"""
Number of items: 3
Price of item: 100
Price of item: 35.56
Price of item: 3.24
Total price for 3 items is $124.92
"""

total_price = 0
number_items = int(input('Number of items: '))
while number_items < 0:
    print("Invalid number of items!")
    number_items = int(input('Number of items: '))
for i in range(0, number_items):
    price = float(input('Price of item: '))
    total_price = total_price + price
if total_price > 100:
    total_price = total_price * 0.9
print('Total price for', number_items, 'items is ${:.2f}'.format(total_price))