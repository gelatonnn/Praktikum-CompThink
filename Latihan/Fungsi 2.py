def menu(pil1, pil2, pil3):
    print("Menu")
    print("1. " + str(pil1))
    print("2. " + str(pil2))
    print("3. " + str(pil3))
    print("Masukan Pilihan : ")

menu("Burger", "Ayam", "Mie Instan")
makanan = int(input())

menu("Jus", "thai tea", "teh tarik")
minuman = int(input())

menu("kentang", "Krupuk", "abon")
tambahan = int(input())

total_menu = menu
print(total_menu)
