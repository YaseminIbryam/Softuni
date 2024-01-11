hour_exam = int(input())
minute_exam = int(input())
arrived_hour = int(input())
arrived_minute = int(input())
exam_min_minus_arrived_min = minute_exam - arrived_minute
arrived_min_minus_exam_min = arrived_minute - minute_exam
exam_h_minus_arrived_h = hour_exam - arrived_hour
arrived_h_minus_exam_h = arrived_hour - hour_exam
if hour_exam == arrived_hour:
    if minute_exam == arrived_minute:
        print("On time")
    elif arrived_minute < minute_exam:
        if exam_min_minus_arrived_min <= 30:
            print(f"On time")
        else:
            print("Early")
        print(f"{exam_min_minus_arrived_min} minutes before the start")
    elif arrived_minute > minute_exam:
        print(f"Late\n{arrived_min_minus_exam_min} minutes after the start")
elif hour_exam > arrived_hour:
    if exam_h_minus_arrived_h == 1:
        if arrived_minute < 30:
            print("Early")
            if arrived_minute <= minute_exam:
                print(f"{1}:{exam_min_minus_arrived_min:02d} hours before the start")
            else:
                minutes = 60 + minute_exam - arrived_minute
                print(f"{minutes} minutes before the start")
        elif minute_exam >= arrived_minute:
            print("Early")
            minutes = minute_exam - arrived_minute
            print(f"{1}:{minutes:02d}hours before the start")
        else:
            minutes = 60 - arrived_minute + minute_exam
            if minutes <= 30:
                print("On time")
            else:
                print("Early")
            print(f"{minutes} minutes before the start")
    else:
        print("Early")
        if minute_exam >= arrived_minute:
            hours = hour_exam - arrived_hour
            minutes = minute_exam - arrived_minute
            print(f"{hours}:{minutes:02d} hours before the start")
        else:
            hours = hour_exam - arrived_hour - 1
            minutes = 60 - arrived_minute + minute_exam
            print(f"{hours}:{minutes:02d} hours before the start")
else:  # hour_exam < arrived_hour
    print("Late")
    if arrived_minute >= minute_exam:
        if arrived_h_minus_exam_h == 0:
            print(f"{arrived_min_minus_exam_min} minutes after the start")
        else:
            print(f"{arrived_h_minus_exam_h}:{arrived_min_minus_exam_min:02d} hours after the start")
    else:  # if arrived_minute < minute_exam:
        if arrived_h_minus_exam_h == 1:
            minutes = 60 - minute_exam + arrived_minute
            print(f"{minutes} minutes after the start")
        else:
            hours = arrived_hour - hour_exam + 1
            minutes = 60 - minute_exam + arrived_minute
            print(f"{hours}:{minutes:02d} hours after the start")
