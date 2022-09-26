x = input().split()
b = int(input())
if len(x) == b:
    print("Semua sudah terjajah")
elif len(x) < b:
    print("Maaf negara terlalu kuat")
else:
    x.sort(reverse=True)
    print(x[b])