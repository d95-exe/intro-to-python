steps = int(input("\nNumber Pyramid: Enter the number of steps you want: "))

print("\nVertical left-aligned:\n")
for i in range(1, steps + 1):
    row = ""
    for j in range(1, i + 1):
        row += str(j)+" "
    print(row)

print("\nVertical, right-aligned:\n")
for i in range(1, steps + 1):
    line = "  " * (steps - i)
    for j in range(1, i + 1):
        line += " "+str(j)
    print(line)

print("\nVertical, centric:\n")
for i in range(1, steps + 1):
    line = " " * (steps - i)
    for j in range(1, i + 1):
        line += str(j)+" "
    print(line)

print("\nInverted, left-aligned:\n")
for i in range(steps, 0, -1):
    row = ""
    for j in range(1, i + 1):
        row += str(j)+" "
    print(row)

print("\nInverted, right-aligned:\n")
for i in range(steps, 0, -1):
    row = ""
    for j in range(1, i + 1):
        row += str(j) + " "
    print(" " * (2 * (steps - i)) + row)