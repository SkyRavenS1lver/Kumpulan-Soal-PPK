x = input()
one = x.find("be")
two = x.find("la",one)
three = x.find("la",two+2)
four = x.find("ng",three)
if one < two < three < four:
    print("BISA")
else:
    print("TIDAK")