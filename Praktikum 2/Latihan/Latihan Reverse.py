N = int(input("Masukan N : ")) #input jumlah bilangan
bilangan = [0] * N #Inisiasi list dengan ukuran N untuk menyimpan bilangan

for i in range(N): #minta input bilangan
    bil = int(input())
    bilangan[N - i - 1] = bil #menyimpan bilangan di posisi terbalik

print("Hasil dibalik : ")
for bil in bilangan: #Menampilkan hasil bilangan dalam urutan terbalik
    print(bil, end=" ")