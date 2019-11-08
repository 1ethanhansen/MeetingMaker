# get start and end
# for k in start..end
#   dictionary k : integer += 1

student_dict = {}
for i in range(24):
    student_dict[i] = 0

mentor_dict = {}
for i in range(24):
    mentor_dict[i] = 0

start_time = 10
print("STARTING MENTOR TIME GATHERING")
while True:
    start_time = int(input("Enter the start time you want (24 hr clock): "))
    if start_time < 0 or start_time > 24:
        break
    end_time = int(input("Enter the end time you want (24 hr clock): "))

    for i in range(start_time, end_time + 1):
        mentor_dict[i] += 1

print("STARTING STUDENT TIME GATHERING")
while True:
    start_time = int(input("Enter the start time you want (24 hr clock): "))
    if start_time < 0 or start_time > 24:
        break
    end_time = int(input("Enter the end time you want (24 hr clock): "))

    for i in range(start_time, end_time + 1):
        student_dict[i] += 1

for key in mentor_dict:
    if mentor_dict[key] >= 2 and student_dict[key] > 0:
        print(key, end=" : ")
        for i in range(1, mentor_dict[key] + 1):
            print("*", end='')
        for i in range(1, student_dict[key] + 1):
            print(i, end='')
        print("")
