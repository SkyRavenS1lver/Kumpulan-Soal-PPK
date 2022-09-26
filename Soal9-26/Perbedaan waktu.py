import math
#Pembuatan variabel dan konversi input menjadi string
a1 = input().split()
a2 = input().split()
b1 = [0]*len(a1)
b2 = [0]*len(a2)
b1[0] = int(a1[0])
b1[1] = int(a1[1])
b1[2] = int(a1[2])
b2[0] = int(a2[0])
b2[1] = int(a2[1])
b2[2] = int(a2[2])

#Melakukan Konversi dari 2 masukan ke dalam detiknya
c1 = b1[0]*3600
c2 = b1[1]*60
d1 = c1+c2+b1[2]

c3 = b2[0]*3600
c4 = b2[1]*60
d2 = c3+c4+b2[2]

#Perhitungan perbedaan 2 waktu, kemudian mencari jam, menit dan detiknya
x = abs(d1-d2)
x1 = math.floor(x/3600)
x2 = math.floor(x%3600/60)
x3 = (x%3600)%60
print(x1, "jam", x2, "menit", x3, "detik")