# Variabel
karakter1 = "ambadit"
karakter2 = "ambatukam"

# dialog awal
print(f"{karakter1} : Hai ,{karakter2} aku baru saja membeli beberapa buah")
print(f"{karakter2} : oh , seru! berapa banayk buah yang kamu beli")

# mengambil input dari pengguna
apel = int(input(f"{karakter1}, berapa banyak apel yang kamu beli?"))
jeruk = int(input(f"{karakter1}, berapa banyak jeruk yang kamu beli?"))

# melakukan operasi aritmatika
total_buah = apel + jeruk
harga_per_ekor = 2 # misalnya harga per buah
total_harga = (apel + jeruk) * harga_per_ekor

# menampilkan hasil operasi
print(f"{karakter1} : aku membeli {apel} apel dan {jeruk} jeruk.")
print(f"{karakter2} : jadi, berapa total buah yang kamu beli?")
print(f"{karakter1} : total buahnya adalah {total_buah}.")
print(f"{karakter2} : bagaimana dengan total harganya?")
print(f"{karakter1} : total harganya adalah {total_harga}.")

if apel >= 20:
    print(f"{karakter2} :buah apel kamu ada 20 buah")
elif jeruk > 10:
    print(f"{karakter1} :buah jerukku ada 10 buah")
else:
    print("buah apel dan jeruk aku ada 5 buah")

# Dialog akhir
print(f"{karakter1} : terimah kasih sudah mendengarkan, {karakter2} !")
print(f"{karakter2} : sama-sama, {karakter1} sampai jumpa lagi!")