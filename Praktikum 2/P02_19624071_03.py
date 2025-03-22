#NIM/Nama : 19624071/Francis Galton
#Tanggal : 31 Oktober 2024
#Deskripsi : Menentukan pemain dengan jumlah kue terbanyak

#menginput jumlah pemain dan jumlah penunjukan
banyak_pemain = int(input("Banyak pemain: "))
jumlah_penunjukan = int(input("Jumlah penunjukan: "))

#membuat variabel jumlah kue untuk setiap pemain
kue = [0] * banyak_pemain

#menghitung jumlah kue awal berdasarkan urutan
for i in range(banyak_pemain):
    kue[i] = (i % 3) + 1

#melakukan penunjukan
for j in range(jumlah_penunjukan):
    posisi = int(input(f"Orang ke -{j + 1} yang ditunjuk: ")) - 1
    jarak = kue[posisi]

    #memberikan kue tambahan kepada pemain yang ditunjuk
    if kue[posisi] < 3:
        kue[posisi] += 1

    #menyumbangkan kue dari pemain yang berjarak
    if posisi - jarak >= 0:
        if kue[posisi - jarak] > 0:
            kue[posisi - jarak] -= 1
    if posisi + jarak < banyak_pemain:
        if kue[posisi + jarak] > 0:
            kue[posisi + jarak] -= 1

#menentukan pemain dengan jumlah kue terbanyak
max_kue = 0
pemain_terbanyak = []

for i in range(banyak_pemain):
    if kue[i] > max_kue:
        max_kue = kue[i]
        pemain_terbanyak = [i + 1]
    elif kue[i] == max_kue:
        pemain_terbanyak += [i + 1]

print("Orang yang memiliki kue terbanyak adalah orang", end=" ")
for i in range(len(pemain_terbanyak)):
    if i == len(pemain_terbanyak) - 1 and len(pemain_terbanyak) > 1:
        print("dan", end=" ")
    print(pemain_terbanyak[i], end="")
    if i < len(pemain_terbanyak) - 1:
        print(", ", end="")
print(".")