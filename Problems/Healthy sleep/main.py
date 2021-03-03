min_time = int(input())
max_time = int(input())
sleep_time = int(input())
if min_time > sleep_time:
    print("Deficiency")
else:
    if min_time <= sleep_time and max_time >= sleep_time:
        print("Normal")
    else:
        print("Excess")
