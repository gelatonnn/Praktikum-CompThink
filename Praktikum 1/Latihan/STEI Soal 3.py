# a = int(input("Tanggal awal makan di resto : "))
# poin = 30 - a + 1
# r = 10
# g = 5
# o = 2
# if (poin // 10 > 0):
#     Ramen = poin // 10
#     Sisa = poin % 10
#     if (Sisa // 5 > 0):
#         Gyoza = Sisa // 5
#         SisaGyoza = Gyoza % 5
#         if (SisaGyoza // 2 > 0 ):
#             Ocha = SisaGyoza // 2
#         else:
#             Ocha = 0
#     else:
#         Gyoza = 0
#         Ocha = 0
# elif (poin // 5 > 0):
#     Ramen = 0
#     Gyoza = poin // 5
#     Sisa = poin % 5
#     if (Sisa // 2 > 0):
#         Ocha = Sisa // 2
#     else:
#         Ramen = 0
#         Ocha = 0
# elif (poin // 2):
#     Ramen = 0
#     Gyoza = 0
#     Ocha = poin // 2
# else:
#     print("Tidak cukup Poin untuk ditukarkan")

# print(f"Total poin yang didapatkan : {poin}")
# print(f"Nona Dep mendapatkan {Ramen} Ramen, {Gyoza} Gyoza, dan {Ocha} Ocha")

a = int(input("Tanggal awal makan di resto: "))
p = 30 - (a-1)
Ocha = 2
Gyoza = 5
Ramen = 10
if p // 10 > 0:
    R = p // 10
    s = p % 10
    if s // 5 > 0:
        G = s // 5
        ss = s % 5
        if ss // 2 > 0:
            O = ss // 2
        else:
            O = 0
    else:
        G = 0
        O = 0
elif p // 5 > 0:
    R = 0
    G = p // 5 
    s = p % 5
    if s // 2 > 0:
        O = s // 2
    else:
        R = 0
        O = 0
elif p // 2:
    R = 0
    G = 0
    O = p // 2
else:
    print("Tidak ada barang yang bisa ditukarkan")

print(f"Nona Deb mendapat {R} ramen, {G} gyoza, dan {O} ocha")