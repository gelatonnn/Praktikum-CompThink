a = int(input("Berapa soal isian yang telah diselesaikan? "))
b = int(input("Berapa soal esai yang telah disekesaikan? "))
isian = 14
esai = 2
x = (isian - a) * 10
y = (esai - b) * 20
if (x + y <=60):
    print("Tuan Riz akan berhasil mengerjakan semua soal")
else:
    print("Tuan Riz tidak berhasil mengerjalan semua soal")