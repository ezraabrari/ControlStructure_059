# Fungsi untuk mencetak pola desain
def cetak_pola(n):
    # 1. Melakukan perulangan dari 1 hingga n (inklusif)
    for i in range(1, n + 1):
        # 2. Pada setiap nilai i, cetak angka i, sebanyak i kali
        for j in range(i):
            print(i, end=" ")  # Cetak angka i dengan spasi setelahnya
        print()  # 3. Pindah ke baris baru setelah mencetak satu baris

# Input: Pengguna memasukkan angka n
n = int(input("Masukkan sebuah angka: "))  # 4. Mengambil input dari pengguna untuk menentukan ukuran pola
cetak_pola(n)  # 5. Memanggil fungsi untuk mencetak pola berdasarkan nilai n
