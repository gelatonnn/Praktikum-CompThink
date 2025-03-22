a = int(input("Banyak uang Peng yang ditawarkan : "))
b = int(input("Banyak uang Kom yang ditawarkan : "))
peng = a * 10000
kom = b * 5000
print(f"Konversi mata uang Peng ke rupiah : {peng}")
print(f"Konversi mata uang Kom ke rupiah : {kom}")
if (peng > kom):
    print("Adik Tuan Kil memilih uang Peng")
else:
    print("Adik Tuan Kil memilih uang Kom")