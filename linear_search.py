print("Linear Search - Python")
y = int(input("Enter a number to add to array, 0 to end:"))
arr = [y]
while True:
    x = int(input("Enter another number: "))
    if x == 0:
        break
    arr.append(x)
print(arr)
target = int(input("\nEnter target: "))
for i in range(len(arr)):
    if arr[i] == target:
        print(f"Target found at index {i}")
