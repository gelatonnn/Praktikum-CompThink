#NIM/Nama : 19624071/Francis Galton
#Tanggal : 17 Oktober 2024
#Deskripsi : Program untuk membantu adik Tuan Leo dalam memilih uang

a = int(input("Banyak uang Peng yang ditawarkan : "))
b = int(input("Banyak uang Kom yang ditawarkan : "))
peng = a * 10000 #mengkonversi uang peng ke rupiah
kom = b * 5000 #mengkonversi uang kom ke rupiah
print(f"Konversi mata uang Peng ke rupiah : {peng}")
print(f"Konversi mata uang Kom ke rupiah : {kom}")
if (peng > kom): #mengecek apakah uang peng lebih dari kom
    print("Adik Tuan Leo memilih uang Peng.")
elif(kom > peng): #mengecek apakah uang kom lebih dari peng
    print("Adik Tuan Leo memilih uang Kom.")
