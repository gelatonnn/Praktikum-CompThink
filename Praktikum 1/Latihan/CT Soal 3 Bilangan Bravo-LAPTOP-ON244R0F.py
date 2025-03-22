a = int(input("Masukan angka : "))
if a < 999:
    print("Angka yang anda masukan belum sesuai")
elif a > 999:
    angka1 = a // 1000
    angka2 = a % 1000 // 100
    angka3 = a%100 // 10
    angka4 = a%10 // 10
    total = angka1 + angka2 + angka3 + angka4
    if (total % angka4):
        print("LU KONTOL)")