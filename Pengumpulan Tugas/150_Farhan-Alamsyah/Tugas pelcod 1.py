print("Pada suatu hari di taman bermain, dua orang anak sedang bermain.")
anak1 = input("Berikan nama untuk anak pertama: ")
anak2 = input("Berikan nama untuk anak kedua: ")
print(f"{anak2}: Ayo, {anak1}, kita coba naik perosotan!")
print(f"{anak1}: Iya, seru banget! Tapi setelah itu kita mau main apa?")
print(f"{anak2}: Kita bisa main ayunan, atau mungkin balon!")
print(f"{anak1}: Aku mau beli balon. Kira-kira harganya berapa ya?")

print("Penjual balon: Untuk balon harganya Rp 2000 per buah.")
print(f"{anak2}: Berapa balon yang mau kita beli, {anak1}?")
balon = int(input("Masukkan jumlah balon yang ingin dibeli: "))

# Operasi aritmatika
hargabalon = balon * 2000

print(f"Penjual balon: Total harganya Rp {hargabalon}.")
print(f"{anak1}: Oke, ini uangnya.")
print("Penjual balon: Terima kasih! Selamat bermain!")

# Operasi logika
print(f"Apakah jumlah balon yang dibeli lebih dari dua? : {balon > 2}")

print("Akhirnya mereka pun bermain dengan balon sambil tertawa dan bersenang-senang.")
