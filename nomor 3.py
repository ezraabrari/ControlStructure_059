# Mengambil input dari pengguna untuk limit deret Fibonacci
n = int(input("Masukkan limit dari sebuah Fibonacci: "))
number1 = 0  # Angka pertama dalam deret Fibonacci
number2 = 1  # Angka kedua dalam deret Fibonacci
hasil = number2  # Menyimpan hasil penjumlahan dari dua angka sebelumnya

# 1. Melakukan perulangan selama number1 kurang dari atau sama dengan n
while number1 <= n:
    print(number1, end=", ")  # Mencetak number1 dengan pemisah koma
    number1 = number2  # Mengupdate number1 menjadi nilai number2
    number2 = hasil  # Mengupdate number2 menjadi hasil penjumlahan sebelumnya
    hasil = number1 + number2  # Menghitung hasil penjumlahan dari dua angka sebelumnya
