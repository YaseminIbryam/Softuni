N = int(input())
intersections = []
for _ in range(N):
    range_1, range_2 = input().split('-')
    range_1_start, range_1_end = range_1.split(',')
    range_2_start, range_2_end = range_2.split(',')
    set_1 = {num for num in range(int(range_1_start), int(range_1_end) + 1)}
    set_2 = {num for num in range(int(range_2_start), int(range_2_end) + 1)}
    intersection = sorted(list(set_1.intersection(set_2)))
    intersections.append(intersection)
longest_intersection = max(intersections, key=lambda x: len(x))
print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")

