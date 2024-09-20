# Karakter dialog
karakter1 = "Rina"
karakter2 = "Andi"

# Fungsi untuk dialog
def dialog():
    print(f"{karakter1}: Hai Andi! Berapa umurmu?")
    umur_andi = int(input(f"{karakter2}: Umurku adalah: "))

    print(f"{karakter1}: Bagus! Aku ingin tahu berapa umurku. Coba tebak!")
    tebakan = int(input(f"{karakter2}: Masukkan tebakanku: "))

    # Menentukan umur Rina
    umur_rina = umur_andi + 3  # Rina lebih tua 3 tahun

    # Memeriksa tebakan
    if tebakan == umur_rina:
        print(f"{karakter1}: Wow, tebakanmu benar! Umurku adalah {umur_rina}.")
    else:
        print(f"{karakter1}: Sayangnya, tebakanmu salah. Umurku adalah {umur_rina}.")

    # Menghitung total umur
    total_umur = umur_andi + umur_rina
    print(f"{karakter1}: Jika kita menjumlahkan umur kita, totalnya adalah {total_umur} tahun.")

    # Operasi logika untuk menentukan siapa yang lebih tua
    if umur_rina > umur_andi:
        print(f"{karakter1}: Aku lebih tua darimu, Andi!")
    else:
        print(f"{karakter2}: Aku lebih tua darimu, Rina!")

# Memulai dialog
dialog()