foods = input().split()
stock = {}

for i in range(0, len(foods), 2):
    key = foods[i]
    value = foods[i+1]
    stock[key] = int(value)

search_products = input().split()
for product in search_products:
    if product in stock:
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")