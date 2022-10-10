n = list(map(int, input().split()))
a = list(set(n))
if n.count(a[0]) == 1:
    print(n.index(a[0]))
else:
    print(n.index(a[1]))