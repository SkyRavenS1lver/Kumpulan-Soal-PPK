x = list(map(float, input().split()))
if x[0]%7 == 0:
    pi = 22/7
else:
    pi = 3.14
print(pi*x[0]*x[1]*x[2])