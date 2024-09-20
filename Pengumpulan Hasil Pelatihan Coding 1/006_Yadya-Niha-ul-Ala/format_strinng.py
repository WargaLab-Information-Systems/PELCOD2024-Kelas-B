nama = "Scaramouche"

pesan = f"My beloved {nama}"
print(pesan)

umur = 500
pesan2 = "He's {}".format(umur) 
print(pesan2 + " YO.") 

pesann = "My Beloved {}, he's {} yo".format(nama, umur) #caara riweh
print(pesann)

pesann = f"He's my Beloved {nama}, he's {umur} yo" #caara egx riweh
print(pesann)

pesanmanual = "My cutie " + nama + " he's " + str(umur) #di sini int umur dirubah menjadi string
print(pesanmanual)