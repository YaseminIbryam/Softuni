limit_first_num = int(input())
limit_second_num = int(input())
limit_third_num = int(input())
for first in range(1, limit_first_num + 1):
    if first % 2 == 0:
        for second in range(2, limit_second_num + 1):
            prime = True
            for second_num in range(2, second):
                if second == 2:
                    break
                if second % second_num == 0:
                    prime = False
            if prime:
                for third in range(1, limit_third_num + 1):
                    if third % 2 == 0:
                        print(first, second, third)
