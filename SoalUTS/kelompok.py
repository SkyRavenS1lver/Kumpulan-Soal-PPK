a = list(map(int, input().split()))
total = 0
b = a[1]
a = a[0]
c = a%4
d = b%4
if c>=2 and d>=2:
    total = a//4+b//4+1
else:
    total = a//4+b//4
print(total)