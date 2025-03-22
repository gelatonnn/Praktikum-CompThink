def pascal(N):
    # Inisialisasi matriks NxN dengan nilai 0
    matrix = [[0] * N for i in range(N)]
    
    # Set nilai baris dan kolom pertama menjadi 1
    for i in range(N):
        matrix[i][0] = 1  # kolom pertama
        matrix[0][i] = 1  # baris pertama
    
    # Isi matriks sesuai aturan segitiga Pascal
    for i in range(1, N):
        for j in range(1, N):
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
    
    # Cetak hasil matriks segitiga Pascal
    for baris in matrix:
        for nilai in baris:
            print(nilai, end=" ")
        print()

N = int(input("Masukkan N: "))
pascal(N)