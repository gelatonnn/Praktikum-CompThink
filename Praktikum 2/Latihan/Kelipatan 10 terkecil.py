# Menerima input dari pengguna
N = int(input("Masukkan N: "))

# Menghitung 10^x terkecil yang lebih dari N
x = 0
while 10 ** x <= N:
    x += 1
print(10 ** x)