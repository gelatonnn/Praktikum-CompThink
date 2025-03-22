a = int(input("Masukan angka : "))
if a > 999:
    digit1 = a // 1000
    digit2 = a % 1000 // 100
    digit3 = a & 100 // 10
    digit4 = a % 10
    kali = digit1 * digit4
    tambah = digit2 + digit3
    if kali % tambah == 0:
        print(f"Angka {a} adalah angka spesial.")
    else:
        print(f"Angka {a} bukan angka spesial")
elif a <= 999:
    print("Masukan angka yang sesuai")