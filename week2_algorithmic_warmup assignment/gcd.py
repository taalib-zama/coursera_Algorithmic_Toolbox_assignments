# Uses python3
x = 0
def euclidgcd(a,b):
    if b == 0:
        return a
    x = a%b
    return euclidgcd(b,x)
a , b = [int(i) for i in input().split()]
print(euclidgcd(a,b))

