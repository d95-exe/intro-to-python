set ="My name is Dushyant"
print("Original sentence:", set)
tes = set.split()
n = len(tes)

#reversing every word in original order
for i in range(len(tes)):
    tes[i] = tes[i][::-1]
print("reversing all words in their position:")
print(" ".join(tes))

#reversing every other word
for i in range(0, n, 2):
    tes[i] = tes[i][::-1]
print("\nReversing every other word:")
print(" ".join(tes))

