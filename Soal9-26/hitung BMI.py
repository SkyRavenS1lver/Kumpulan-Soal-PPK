x = input().split()
w = int(x[0])
h = (int(x[1])/100) **2

bmi = w / h
if bmi < 18.5 :
    print("Berat badan kurang")
elif 18.5 <=  bmi <= 22.9 :
    print("Berat badan normal")
elif 23 <=  bmi <= 29.9:
    print("Berat badan berlebih")
elif bmi > 30 :
    print("obesitas")