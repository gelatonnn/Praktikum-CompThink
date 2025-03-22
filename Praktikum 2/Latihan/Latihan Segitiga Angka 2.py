# Meminta input dari pengguna
N = int(input("Masukkan N: "))

# Loop untuk setiap baris pola
for i in range(1, N + 1):
    # Menambahkan spasi di awal setiap baris untuk membuat segitiga sama kaki
    print(" " * (2 * (N - i)), end="")  # Dua spasi per level untuk menyeimbangkan

    # # Bagian menurun dari i hingga 1
    for j in range(i, 0, -1):
        print(j, end=" ")

    # Bagian menaik dari 2 hingga i
    for k in range(2, i + 1):
        print(k, end=" ")

    # Pindah ke baris baru
    print()
