EncryptL = {"Revan" : 0, "Angga" : 1, "Duta" : 2, "Paul" : 3, "Komang" : 4}

Database = ["10 Januari 1998","10 Agustus 2000", "11 Februari 2003", "12 September 1999", "3 Maret 1995"]
N = input().capitalize()
if N in EncryptL:
    print(Database[EncryptL[N]])
else:
    print("Nama tidak terdaftar")