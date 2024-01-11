deposit_sum = float(input())
period = int(input())
percent = (float(input()))/100
total_sum = deposit_sum + period * ((deposit_sum * percent) / 12)
print(total_sum)
