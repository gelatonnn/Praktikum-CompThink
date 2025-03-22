#NIM/Nama : 19624071/Francis Galton
#Tanggal : 17 Oktober 2024
#Deskripsi : Menentukan sebuah bilangan apakah Unik, Super Unik, atau Biasa

a = int(input("Masukan sebuah bilangan : "))
if (a >= 1000): #mengecek apakah bilangan sudah 4 digit atau belum
    angka1 = a // 1000 
    angka2 = a % 1000 // 100
    angka3 = a % 100 // 10
    angka4 = a % 10
    if (angka1 != angka2 and angka1 != angka3 and angka1 != angka4 and angka2 != angka3 and angka2 != angka4 and angka3 != angka4): #mengecek apakah setiap digit berbeda atau ada yang sama
        if ((angka1 + angka2 + angka3 + angka4) % 2 ==1): #mengecek apakah memenuhi syarat jumlah bilangan ganjil
            if (angka1 > angka4) and a % 2 == 0: #mengecek apakah bilangan memenuhi syarat bilangan super unik
                print("Bilangan tersebut adalah bilangan Super Unik")
            elif (angka1 > angka4) and ((angka2 + angka3) > angka1): #mengecek apakah bilangan memenuhi syarat bilangan super unik
                print("Bilangan tersebut adalah bilangan Super Unik")
            elif ((angka2 + angka3) > angka1 and a % 2 == 0): #mengecek apakah bilangan memenuhi syarat bilangan super unik
                print("Bilangan tersebut adalah bilangan Super Unik")
            else: #jika tidak memenuhi maka bilangan tersebut adalah bilangan unik
                print("Bilangan tersebut adalah bilangan Unik")
        else: #jika tidak memenuni maka bilangan tersebut adalah bilangan biasa
            print("Bilangan tersebut adalah Bilangan Biasa")
    else:
        print("Bilangan tersebut adalah bilangan Biasa.")
else: #mengecek apakah bilangan yang dimasukan 4 digit atau tidak
    print("Masukan 4 bilangan")
