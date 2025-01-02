num = int(input("\nFACTORIAL FINDER\nEnter a number:\n>>>"))

fact = 1
for i in range(1, num+1):
    fact *= i

print("\nThe Factorial is :", fact)