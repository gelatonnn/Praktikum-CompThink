a = int(input("Masukan Koordinat Katak : "))
kanan = int(input("Masukan panjang lompatan katak ke kanan : "))
kiri = int(input("Masukan panjang lompatan katak ke kiri : "))
if (a >= 0, a%2 == 0): 
    k = kanan * kiri
elif (a%2 == 1):
    k = a * 2
elif (a < 0):
    k = kanan * kiri
elif (a < 0, a%3 ==0):
    k = kiri * 2
if (k%2 == 0):
    lompat_kanan = k // 2
    lompat_kiri = k // 2
else:
    lompat_kanan = k // 2 + 1
    lompat_kiri = k // 2
akhir = a + (kanan * lompat_kanan) - (kiri * lompat_kiri)
print("Koordinat katak sekarang adalah ", akhir)