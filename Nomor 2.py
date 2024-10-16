# Mengambil input dari pengguna untuk tiga angka
number1 = int(input("Masukkan angka pertama: "))
number2 = int(input("Masukkan angka kedua: "))
number3 = int(input("Masukkan angka ketiga: "))

# 1. Memeriksa apakah number1 adalah yang terbesar
if (number1 > number2) and (number1 > number3):
    print("Maka angka terbesar adalah:", number1)  # Menampilkan number1 sebagai angka terbesar
# 2. Memeriksa apakah number2 adalah yang terbesar
elif (number2 > number1) and (number2 > number3):
    print("Maka angka terbesar adalah:", number2)  # Menampilkan number2 sebagai angka terbesar
# 3. Jika tidak ada yang lebih besar dari kedua angka sebelumnya, maka number3 adalah yang terbesar
else:
    print("Maka angka terbesar adalah:", number3)  # Menampilkan number3 sebagai angka terbesar
