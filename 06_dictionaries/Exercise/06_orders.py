buy = False
products_quantities = {}
products_prices = {}
while not buy:
    data = input()
    if data == 'buy':
        buy = True
        break
    else:
        data = data.split(' ')
    product = data[0]
    price = float(data[1])
    quantity = int(data[2])

    if product not in products_prices:
        products_prices[product] = price
        products_quantities[product] = quantity
    else:
        products_prices[product] = price
        products_quantities[product] += quantity


for p1, q1 in products_quantities.items():
    price = float(products_prices.get(p1))
    print(f'{p1} -> {price * q1:.2f}')