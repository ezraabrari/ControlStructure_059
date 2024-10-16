# Mengambil input dari pengguna untuk memasukkan nilai siswa
grade = int(input("Masukkan nilai suatu siswa: "))

# 1. Memeriksa apakah nilai lebih besar atau sama dengan 90
if grade >= 90:
    print("Excellent performance")  # Menampilkan pesan untuk kinerja sangat baik
# 2. Memeriksa apakah nilai lebih besar atau sama dengan 80
elif grade >= 80:
    print("Very Good Performance")  # Menampilkan pesan untuk kinerja sangat baik
# 3. Memeriksa apakah nilai lebih besar atau sama dengan 70
elif grade >= 70:
    print("Good Performance")  # Menampilkan pesan untuk kinerja baik
# 4. Memeriksa apakah nilai lebih besar atau sama dengan 60
elif grade >= 60:
    print("Average performance")  # Menampilkan pesan untuk kinerja rata-rata
# 5. Jika nilai kurang dari 60
else:
    print("Bad Performance")  # Menampilkan pesan untuk kinerja buruk
