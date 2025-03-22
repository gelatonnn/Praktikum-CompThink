#NIM/Nama : 19624071/Francis Galton
#Tanggal : 31 Oktober 2024
#Deskripsi :Mencari angka yang dapat dibagi dengan angka terakhirnya

#Memasukan input dari pengguna
a = int(input("Masukan nilai A : "))
b = int(input("Masukan nilai B : "))

#membuat variabel array untuk menyimpan angka yang memenuhi syarat
hasil = [0] * (b - a + 1) #membuat array dengan ukuran maksimum yg mungkin terjadi
count = 0 #membuat variabel penghitung

for i in range (a, b+1):
    angka_terakhir = i % 10 #untuk mengambil digit terakhir

    if angka_terakhir != 0:
        if i % angka_terakhir == 0:
            hasil[count] = i #menyimpan angka ke dalam array
            count += 1

#menampilkan hasil
print(f"Terdapat {count} angka yang memenuhi sifat tersebut")