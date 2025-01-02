nums = ["","","","","","","","","",""]
print("\nSum & Average\nEnter 10 numbers:")
for i in range(0,10):
    nums[i] = int(input("Number " + str(i+1) + ": "))
    i = i+1
sum = 0
for i in range(0, 10):
    sum += nums[i]

print("\nThe sum of elements is: " + str(sum))
print("\nThe average of these elements is: " + str(sum/10))