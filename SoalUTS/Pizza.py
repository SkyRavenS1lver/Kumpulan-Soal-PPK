import math
listMakan = [input(), input(), input()]
a = listMakan.count("3/4")
if a == 2 and listMakan.count("1/2") == 1:
    b = 1
else:
    b = listMakan.count("1/2")/2
    a = (listMakan.count("3/4")*3+listMakan.count("1/4"))/4
print(math.ceil(a+b)+1)