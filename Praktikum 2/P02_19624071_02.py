#NIM/Nama : 19624071/Francis Galton
#Tanggal : 31 Oktober 2024
#Deskripsi :Pesan Rahasia Nona Sal ke Nona Deb

#Memasukan jumlah huruf pada kamus rahasia
jumlah_huruf = int(input("Masukan jumlah huruf pada kamus rahasia : "))

#membuat list untuk menyimpan pasangan huruf biasa dan huruf rahasia
kamus = [0] * jumlah_huruf

#mengisi kamus dengan input dari pengguna
for i in range (jumlah_huruf):
    huruf_biasa = input(f"Masukan huruf biasa ke-{i + 1} : ")
    huruf_rahasia = input(f"Masukan huruf rahasia ke-{i + 1} : ")
    kamus[i] = (huruf_biasa, huruf_rahasia)

#mengetahui pesan yang ingin diubah
pesan = ""
while pesan == "":
    pesan = input("Masukan pesan yang ingin diubah : ")
    if pesan == "":
        print("Pesan tidak boleh kosong!")

#mengubah pesan biasa menjadi pesan rahasia
pesan_rahasia = ""

#mengakses setiap karakter dalam pesan
for i in range (len(pesan)):
    karakter = pesan[i]

    #mencari huruf rahasia yang sama dengan huruf biasa
    huruf_rahasia = karakter #apabila tidak ditemukan
    ada = False #menandai apakah karakter ditemukan atau tidak

    for j in range (jumlah_huruf):
        if kamus[j][0] == karakter:
            huruf_rahasia = kamus[j][1]
            ada = True #menandai bahwa karakter telah ditemukan
    
    #menambahkan huruf rahasian ke pesan rahasia
    pesan_rahasia += huruf_rahasia

print("Pesan rahasia Nona Sal : ")
print(pesan_rahasia)