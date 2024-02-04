def func(data_type, variable):
    if data_type == 'int':
        return int(variable) * 2
    elif data_type == 'real':
        return f"{float(variable) * 1.5:.2f}"
    elif data_type == 'string':
        return f"${variable}$"


print(func(input(), input()))