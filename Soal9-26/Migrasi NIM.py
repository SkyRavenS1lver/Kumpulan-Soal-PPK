x = input().split("-")
x[0], x[1], x[2], x[3] = x[3][2:], x[0], x[2], x[1]
print("/".join(x))