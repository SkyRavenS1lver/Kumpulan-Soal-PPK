x = input().split()
x[1] = x[1].upper()
dict = {"JANUARI":0,
        "FEBRUARI":31,
        "MARET":59,
        "APRIL":90,
        "MEI":120,
        "JUNI":151,
        "JULI":181,
        "AGUSTUS":212,
        "SEPTEMBER":243,
        "OKTOBER":273,
        "NOVEMBER":304,
        "DESEMBER":334
        }
print((int(x[0])+dict[x[1]]),"hari")