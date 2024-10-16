# Fungsi untuk mencetak bilangan ganjil sampai n
def cetak_bilangan_ganjil(n):
    # 1. Menampilkan pesan bahwa program akan mencetak bilangan ganjil hingga n
    print(f"Bilangan ganjil hingga {n}:")
    
    # 2. Melakukan perulangan dari 1 hingga n
    for i in range(1, n + 1):
        # 3. Memeriksa apakah angka i adalah bilangan ganjil
        if i % 2 != 0:  # Bilangan ganjil jika sisa pembagian 2 tidak sama dengan 0
            # 4. Jika i ganjil, cetak i tanpa pindah ke baris baru
            print(i, end=" ")
    
    # 5. Akhir fungsi; semua bilangan ganjil hingga n telah dicetak
    # (Tidak perlu instruksi tambahan karena output sudah dihasilkan)

# Input: Pengguna memasukkan angka n
n = int(input("Masukkan sebuah angka: "))  # Mengambil input dari pengguna
cetak_bilangan_ganjil(n)  # Memanggil fungsi untuk mencetak bilangan ganjil
