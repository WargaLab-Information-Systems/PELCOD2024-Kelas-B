print("Pada suatu hari di sebuah toko buah terdapat dua orang anak yang ingin membeli buah")
anak1 = input("berikan nama untuk anak pertama: ")
anak2 = input("berikan nama untuk anak kedua: ")
print(f"{anak2} : Kamu mau beli buah apa {anak2}?")
print(f"{anak2} : Aku mau beli buah apel")
print(f"{anak1} : Ohhh kalo aku mau beli buah semangka")
print(f"{anak2} : Pak ini buahnya berapa ya pak?")
print("Pak penjual : Untuk buah apel harganya Rp 5000 kalo semangka Rp 8000")
print(f"{anak2} : Pak aku sama temen ku beli buah semangka sama apelnya")
print("Pak penjual : Bual apel nya berapa, buah semangkanya berapa?")
apel = int(input("Masukkan jumlah buah apel: "))
semangka = int(input("Masukkan jumlah buah semangka: "))

# Operasi aritmatika
hargaapel = apel * 5000
hargasemangka = semangka * 8000

print(f"Pak penjual : Total harganya {hargaapel + hargasemangka}")
print(f"{anak2} : Iya pak ini uangnya")
print("Pak penjual : Iya dek terimakasih banyak")

# Operasi logika
print(f"apakah jumlah semangka lebih banyak dari apel? : {semangka > apel}")

print("Akhirnya mereka pun pulang dan makan buah bersama")
