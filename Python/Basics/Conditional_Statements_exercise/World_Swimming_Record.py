record_seconds = float(input())
distance_meters = float(input())
seconds_per_meter = float(input())
slowing_down_seconds = (distance_meters // 15) * 12.5
total_seconds = distance_meters * seconds_per_meter + slowing_down_seconds
if total_seconds < record_seconds:
    print(f" Yes, he succeeded! The new world record is {total_seconds:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_seconds-record_seconds:.2f} seconds slower.")
