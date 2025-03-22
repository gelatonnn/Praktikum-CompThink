a = int(input("Masukan jam kebernagkatan : "))
b = int(input("Masukan jam kepulangan : "))
if (6 <= a <= 8 or 15 <= a <= 17):
    tarif_a = 0
    transport_1 = "Bis Universitas"
elif (7 <= a <= 18):
    tarif_a = 5000
    transport_1 = "Bus Kota"
else:
    tarif_a = 10000
    transport_1 = "Travel"

if (6 <= b <= 8 or 15 <= b <= 17):
    tarif_b = 0
    transport_2 = "Bis Universitas"
elif (7 <= b <= 18):
    tarif_b = 5000
    transport_2 = "Bus Kota"
else:
    tarif_b = 10000
    transport_2 = "Travel"

T = tarif_a + tarif_b
print(f"Nona Deb berangkat dengan {transport_1} dan pulang dengan {transport_2} dan membayar sebanyak {T} ")

