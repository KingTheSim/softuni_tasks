# user input
exam_hour = int(input())
exam_min = int(input())
arrival_hour = int(input())
arrival_min = int(input())

# logic
minutes_exam = exam_min + (exam_hour * 60)
minutes_arrival = arrival_min + (arrival_hour * 60)
diff = abs(minutes_exam - minutes_arrival)

if minutes_arrival > minutes_exam:
    print("Late")
    if diff >= 60:
        print(f"{diff // 60}:{(diff % 60):02d} hours after the start")
    else:
        print(f"{diff} minutes after the start")
elif minutes_arrival <= minutes_exam:
    if diff > 30:
        print("Early")
        if diff >= 60:
            print(f"{diff // 60}:{(diff % 60):02d} hours before the start")
        else:
            print(f"{diff % 60} minutes before the start")
    elif diff == 0:
        print("On time")
    else:
        print("On time")
        print(f"{diff % 60} minutes before the start")
