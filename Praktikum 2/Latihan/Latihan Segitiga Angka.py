N = int(input("Masukan N : ")) #meminta input angka
for i in range(1, N+1): #loop untuk membuat baris pola
    for j in range(1, i+1): #loop untuk mencetak angka setiap baris
        print(j, end=" ")
    print() #pindah ke baris baru setiap baris selesai