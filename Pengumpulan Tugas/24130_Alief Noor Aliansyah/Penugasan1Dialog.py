# Dialog antara penjual dan pembeli

def dialog_penjual_pembeli():
    print("Penjual: Selamat datang! Ada yang bisa saya bantu?")
    pembeli = input("Pembeli: ")
    
    print(f"Penjual: Oh, {pembeli} ya? Kami punya beberapa produk yang bagus.")
    print("Penjual: Apa yang sedang Anda cari?")
    cari = input("Pembeli: ")

    if cari.lower() == 'baju':
        print("Penjual: Kami punya baju dengan berbagai model, apakah Anda ingin melihatnya?")
        respon = input("Pembeli: ")

        if respon.lower() == 'ya':
            print("Penjual: Ini koleksi baju terbaru kami, harganya mulai dari Rp150.000.")
        else:
            print("Penjual: Baik, jika ada yang ingin ditanyakan, jangan ragu.")
    else:
        print(f"Penjual: Maaf, {cari} tidak tersedia sekarang. Ada yang lain yang ingin Anda lihat?")

    print("Pembeli: Terima kasih, saya akan lihat-lihat dulu.")
    print("Penjual: Silakan, jangan sungkan jika butuh bantuan.")

# Menjalankan dialog
dialog_penjual_pembeli()
