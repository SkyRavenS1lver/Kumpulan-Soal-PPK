x = input().lower()
listhasil = []
listhasil.append(x.count("a"))
listhasil.append(x.count("i"))
listhasil.append(x.count("u"))
listhasil.append(x.count("e"))
listhasil.append(x.count("o"))
listhasil = str(sum(listhasil))
if len(listhasil) >= 1:
    listhasil = str(sum(list(map(int, list(listhasil)))))
    if len(listhasil) >= 1:
        listhasil = str(sum(list(map(int, list(listhasil)))))
print(listhasil)