# get start and end
# for k in start..end
#   dictionary k : integer += 1

dictionary = {}
for i in range(24):
    dictionary[i] = 0

start_time = 10
while True:
    start_time = int(input("Enter the start time you want (24 hr clock): "))
    if start_time < 0 or start_time > 24:
        break
    end_time = int(input("Enter the end time you want (24 hr clock): "))

    for i in range(start_time, end_time + 1):
        dictionary[i] += 1

for key in dictionary:
    if dictionary[key] > 0:
        print(key, end=" : ")
        for i in range(1, dictionary[key] + 1):
            print(i, end='')
        print("")
