# Program dialog antara dua karakter: Mas Amba dan Rafly

print("Selamat datang di program dialog antara Mas Amba dan Rafly!")
print("Mas Amba: Halo Rafly, ayo kita belajar matematika.")
print("Rafly: Hai Mas Amba Aku paling semangat kalo soal matematika!")
print("Mas Amba: yaudah lansung aku mulai yaa")
print("Rafly: okee")

# input dari pengguna untuk angka
try:
    angka1 = int(input("Mas Amba: Berikan aku angka pertama: "))
    angka2 = int(input("Mas Amba: Berikan aku angka kedua: "))
except ValueError:
    print("Masukkan input yang benar!.")
    exit()


# operasi aritmatika
jumlah = angka1 + angka2
selisih = angka1 - angka2
produk = angka1 * angka2

if angka2 != 0:
    pembagian = angka1 / angka2
else:
    pembagian = None

# Menampilkan hasil operasi aritmatika
print("\nMas Amba: Aku sudah melakukan beberapa perhitungan.")
print(f"Mas Amba: Jumlah dari {angka1} dan {angka2} adalah {jumlah}.")
print(f"Mas Amba: Selisih antara {angka1} dan {angka2} adalah {selisih}.")
print(f"Mas Amba: Produk dari {angka1} dan {angka2} adalah {produk}.")

if pembagian is not None:
    print(f"Mas Amba: Pembagian dari {angka1} oleh {angka2} adalah {pembagian}.")
else:
    print("Mas Amba: Pembagian dengan nol tidak diperbolehkan.")

# Operasi logika
if angka1 > angka2:
    print(f"\nMas Amba: {angka1} lebih besar dari {angka2}.")
elif angka1 < angka2:
    print(f"Mas Amba: {angka1} lebih kecil dari {angka2}.")
else:
    print(f"Mas Amba: {angka1} sama dengan {angka2}.")

# Mengakhiri dialog
print("\nturam: Terima kasih, Mas Amba! Ini sangat membantu.")
print("Mas Amba: Sama-sama, Rafly! Sampai jumpa di pelajaran matemattika berikutnya!")
print("Rafly: okeee")
