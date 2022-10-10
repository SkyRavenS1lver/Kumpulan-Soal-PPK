x = list(map(int, input().split()))
harga = x[0]*x[1]
if harga > x[2]:
    print(harga-x[2])
else:
    print(0)