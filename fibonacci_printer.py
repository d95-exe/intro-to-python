def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)

for i in range(int(input("Enter no. of steps:"))):
    print(fib(i))