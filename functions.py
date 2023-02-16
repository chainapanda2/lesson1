def get_sum(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    delimiter = str('&')
    return str(one + delimiter + two)

summ = get_sum('Learn', 'python').upper()
print(summ)

def format_price(price):
    price = int(price)
    return f'Цена:  {price}  руб.'

a = format_price(56.24)
print(a)
