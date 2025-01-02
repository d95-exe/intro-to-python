ll = int(input("Limit-based sum\nEnter the lower limit: "))
ul = int(input("Enter the upper limit: "))
if ul<ll:
    ul, ll = ll, ul

sum = 0
for i in range(ll, ul+1):
    sum += i
print("\nThe sum of all number between " + ll + " and " + ul + " is: " + str(sum))
