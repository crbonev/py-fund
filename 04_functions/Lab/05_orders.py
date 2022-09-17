product = input()
quantity = int(input())


def total_price(qty, prd):
    result = 0
    price = {'coffee': 1.50, 'coke': 1.40, 'water': 1.00, 'snack': 2.00}
    if prd in price:
        result = price[prd] * qty

    return result


print(f'{total_price(quantity, product):.2f}')
