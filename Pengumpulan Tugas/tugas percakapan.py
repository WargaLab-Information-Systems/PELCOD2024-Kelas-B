# Karakter dan Variabel
karakter_1 = "Asta"
karakter_2 = "Yuno"

# Memperkenalkan karakter
print(f"{karakter_1}: Halo, {karakter_2}! Bagaimana kabarmu hari ini?")
print(f"{karakter_2}: Hai, {karakter_1}! Aku baik-baik saja. Bagaimana denganmu?")

# Input dari pengguna
umur_asta = int(input(f"{karakter_1}: Aku berumur berapa tahun menurutmu, {karakter_2}? "))
umur_yuno = int(input(f"{karakter_2}: Kalau begitu, berapa umurku menurutmu, {karakter_1}? "))

# Logika untuk membandingkan umur
if umur_asta > umur_yuno:
    print(f"{karakter_1}: Wah, ternyata menurutmu aku lebih tua ya!")
elif umur_asta < umur_yuno:
    print(f"{karakter_1}: Jadi, kamu mengira aku lebih muda?")
else:
    print(f"{karakter_1}: Wow, kita seumuran menurut tebakanmu!")

# Operasi Aritmatika: menghitung total umur dan perbedaannya
total_umur = umur_asta + umur_yuno
selisih_umur = abs(umur_asta - umur_yuno)

# Menampilkan hasil
print(f"{karakter_2}: Jika kita menjumlahkan umur kita, hasilnya adalah {total_umur} tahun.")
print(f"{karakter_2}: Dan selisih umur kita adalah {selisih_umur} tahun.")

# Operasi Logika: Cek apakah mereka berusia lebih dari 30 tahun
if umur_asta > 30 and umur_yuno > 30:
    print(f"{karakter_1}: Sepertinya kita berdua sudah cukup tua, ya!")
elif umur_asta <= 30 and umur_yuno <= 30:
    print(f"{karakter_2}: Masih muda nih kita berdua!")
else:
    print(f"{karakter_1}: Sepertinya hanya salah satu dari kita yang sudah tua, hehe.")