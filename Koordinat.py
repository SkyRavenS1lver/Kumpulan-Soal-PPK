N1 = list(map(float, input().split()))
N2 = list(map(float, input().split()))
tp = [0.0, 0.0]
if N1==N2==tp:
    print('Titik')
elif N1==N2 or N1==tp or tp==N2 or (N1[0]/N2[0] == N1[1]/N2[1]):
    print('Garis')
else:
    print('Segitiga')