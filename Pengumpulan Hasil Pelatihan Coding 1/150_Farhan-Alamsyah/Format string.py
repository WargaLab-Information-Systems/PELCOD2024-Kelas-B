nama = "Farhan Alamsyah"
pesan = f"Nama saya {nama}"
print(pesan)

umur = 18
pesanTambahan = "Umur saya {}". format(umur)
pesanlengkap = f"Nama : {nama} dan Umur : {umur}"
print(pesanTambahan)
print(pesanlengkap)
# contoh format untuk variabel yang mengandung integer

pesanmanual = "nama saya yang benar adalah" + nama + "dan berumur " + str(umur)
print(pesanmanual)
# jika manual harus menggunakan format str() untuk mengubah integer menjadi string