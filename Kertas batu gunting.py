N = input().split(" ")
A = N[0]
B = N[1]

if (A == "8<" and B == "[]") or (A == "[]" and B == "()" ) or (A == "()" and B== "8<"):
    print("Pemain A menang")
elif (A == "[]" and B == "8<") or (A == "()" and B == "[]" ) or (A == "8<" and B == "()"):
    print("Pemain B menang")
else:
    print("Draw")