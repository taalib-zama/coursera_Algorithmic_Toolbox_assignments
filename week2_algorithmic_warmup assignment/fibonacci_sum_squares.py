# Uses python3
n = int(input())
def fib_number(n):
    a, b = 0, 1
    for i in range(n % 60):
        a, b = b, (a + b)
    return a

print((fib_number(n+1)*fib_number(n))%10)