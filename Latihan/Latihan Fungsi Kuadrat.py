def fungsi(x):
    x = x ** 2 - 2*x + 5
    return x 

a = int(input("Masukan A : "))
b = int(input("Masukan B : "))

for i in range(a, b+1):
    print(f'f({i}) = {fungsi(i)}')