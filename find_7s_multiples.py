#find multiples of 7 between 0-100

nums = []
count = 0
for i in range (1, 101):
    if (i%7 == 0):
        nums.append(i)
        count += 1
print(nums)