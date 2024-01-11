green_1l_m = 3.4
red_1l_m = 4.3
x = float(input())
y = float(input())
h = float(input())
m_green = (x**2 * 2 - 2 * 1.2) + (x * y - 1.5**2) * 2
m_red = (x * y * 2) + ((x * h)/2) * 2
l_green = m_green / green_1l_m
l_red = m_red / red_1l_m
print(f"{l_green:.2f}")
print(f"{l_red:.2f}")
