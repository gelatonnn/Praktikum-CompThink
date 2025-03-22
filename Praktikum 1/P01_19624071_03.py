#NIM/Nama : 19624071/Francis Galton
#Tanggal : 17 Oktober 2024
#Deskripsi : Membantu Nona Sal dalam menerima pesanan gantungan kunci

bebek = int(input("Masukan jumlah pesanan gantungan kunci bunga : ")) #jumlah pesanan gantungan bebek
ayam = int(input("Masukan jumlah pesanan gantungan kunci ayam : ")) #jumlah pesanan gantungan ayam
kupu = int(input("Masukan jumlah pesanan gantungan kunci kupu-kupu : ")) #jumlah pesanan gantungan kupu

merah = int(input("Masukan umlah clay merah : ")) #jumlah clay merah
biru = int(input("Masukan jumlah clay biru : ")) #jumlah clay biru
ungu = int(input("Masukan jumlah clay ungu : ")) #jumlah clay ungu

merah = merah - (2 * bebek) - ayam - kupu #jumlah clay merah dikurangi
biru = biru - bebek - (2 * ayam) - kupu #jumlah clay biru dikurangi

if (merah >= 0) and (biru >= 0): #cek apakah biru dan merah memiliki sisa
    ungu = ungu - (3 * kupu) #hitung jumlah clay ungu yang diperlukan
    if ungu < 0: #jika clay ungu dibutuhkan
        if merah == biru:
            ungu = ungu + (merah + biru)
        elif(merah < biru):
            ungu = ungu + (2 * merah)
        elif(merah > biru):
            ungu = ungu + (2 * biru)
        if(ungu >= 0): #jika clay ungu sudah cukup maka pesanan dapat dibuat
            print("Pesanan dapat diterima oleh Nona Sal")
        else: #jika clay ungu belum cukup maka pesanan tidak dapat dibuat
            print("Pesanan tidak dapat diterima oleh Nona Sal")
    else: #jika butuh clay tambahan maka pesanan tidak dapat dibuat
        print("Pesanan dapat diterima oleh Nona Sal")
else: #jika clay kurang maka pesanan tidak dapat dibuat
    print("Pesanan tidak dapat diterima oleh Nona Sal")