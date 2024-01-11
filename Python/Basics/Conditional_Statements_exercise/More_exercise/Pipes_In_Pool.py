v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())
p1_fulling = p1 * h
p2_fulling = p2 * h
total_fulling = p1_fulling + p2_fulling
total_fulling_percent = (total_fulling / v) * 100
p1_fulling_percent = (p1_fulling / total_fulling) * 100
p2_fulling_percent = (p2_fulling / total_fulling) * 100
if total_fulling <= v:
    print(f'The pool is {total_fulling_percent:.2f}% full. Pipe 1: {p1_fulling_percent:.2f}%. Pipe 2: {p2_fulling_percent:.2f}%.')
else:
    more = total_fulling - v
    print(f"For {h:.2f} hours the pool overflows with {more:.2f} liters.")
