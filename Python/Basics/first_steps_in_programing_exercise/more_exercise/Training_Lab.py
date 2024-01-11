w = float(input())
h = float(input())
w_sm = w * 100
h_sm = h * 100 - 100
desks_in_colon = w_sm // 120
desks_in_row = h_sm // 70
desks = (desks_in_row * desks_in_colon) - 3
print(int(desks))
