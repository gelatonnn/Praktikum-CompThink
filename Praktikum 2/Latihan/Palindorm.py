n = int(input("Masukkan panjang string: "))
string = str(input("Masukkan string: "))
palindrom = True
for i in range(n//2):
    if string[i] != string[n-1-i]:
        palindrom = False
if palindrom:
    print(f"{string} adalah palindrom")
else:
    print(f"{string} bukan palindrom")
