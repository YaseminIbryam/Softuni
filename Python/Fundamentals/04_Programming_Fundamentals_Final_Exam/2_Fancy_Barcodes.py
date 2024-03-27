import re

n = int(input())
pattern = r'@#+[A-Z][a-zA-Z0-9]{4,}[A-Z]@#+'
for i in range(n):
    barcode = input()
    valid_barcode = re.search(pattern, barcode)
    if valid_barcode:
        product_group = ''
        barcode = valid_barcode.group()
        for char in barcode:
            if char.isdigit():
                product_group += char
        if not product_group:
            product_group = '00'
        print(f'Product group: {product_group}')
    else:
        print('Invalid barcode')

