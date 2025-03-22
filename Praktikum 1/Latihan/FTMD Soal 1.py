a = int(input("Masukan nilai kuis pertama : "))
b = int(input("Masukan nilai kuis kedua : "))
c = int(input("Masukan nilai kuis ketiga : "))
rata2 = (a + b + c) // 3
if (rata2 >= 80):
    print("Nilai rata-rata Tuan Kil : ", rata2)
    print("Tuan Kil mendapatkan nilai LULUS MEMUASKAN")
elif (rata2 >=70):
    print("Nilai rata-rata Tuan Kil : ", rata2)
    print("Tuan Kil mendapatkan nilai LULUS")
elif (rata2 < 70):
    print("Nilai rata-rata Tuan Kil : ", rata2)
    print("Tuan Kil mendapatkan nilai TIDAK LULUS")