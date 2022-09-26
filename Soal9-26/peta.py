a = list(map(int, input().split()))
b = list(map(int, input().split()))
x = a[0]
y = a[1]
xKapal = b[0]
yKapal = b[1]
print(("-"*x))
print(((("*")*x)+"\n")*(yKapal-1), end="")
print(((("*")*(xKapal-1))+"="+((("*")*(x-xKapal))))+"\n", end="")
print(((("*")*x)+"\n")*(y-yKapal), end="")
print("-"*x)