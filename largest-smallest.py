print("LARGEST AND SMALLEST\nEnter numbers, and i will tell you the sum \nof the smallest and the largest.")
arr = []
lnt = 0
while(True):
    arr.append(int(input("Number: ")))
    lnt += 1
    choice = input("\nEnter another? y/n: ")
    if(choice == "y"):
        choice = ""
        continue
    else:
        print("\nExiting addition...")
        break

print("\nYour array:")
print(arr)
i, max, min= 0, arr[0], arr[0]
while(i < lnt):
    if (arr[i] > max):
        max = arr[i]
    i += 1
print("\nLargest value: " + str(max))

i = 0
while(i < lnt):
    if (arr[i] < min):
        min = arr[i]
    i += 1
print("\nSmallest value: " + str(min))
print("\nSum = " + str(min+max))