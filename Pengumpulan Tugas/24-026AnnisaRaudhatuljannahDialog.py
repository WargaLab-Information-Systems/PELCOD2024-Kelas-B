nama_karakter1 = "Valdo"
nama_karakter2 = "Kevin"

print(f"Halo, {nama_karakter1} dan {nama_karakter2}!")

harga_baju = float(input(f"{nama_karakter1}: berapa harga satu baju ini? Rp "))
print(f"{nama_karakter2}: Harganya Rp {harga_baju}")

jumlah_bajudibeli =int(input(f"{nama_karakter1}: wah murah sekali. hmm beli berapa baju yaa?"))

uang_Valdo = float(input(f"{nama_karakter1}: Eh uangku tinggal berapa ya? Rp ")) 

total_harga = harga_baju * jumlah_bajudibeli

if uang_Valdo >= total_harga:
    print(f"{nama_karakter2}: Uangmu cukup!")
    print(f"{nama_karakter1}: Aku akan beli {jumlah_bajudibeli} baju.")
else:
    print(f"{nama_karakter2}: Uangmu tidak cukup!")
    print(f" {nama_karakter1}: Aku hanya punya Rp {uang_Valdo}, sedangkan total harga Rp {total_harga} yasudah secukup uangnya saja")