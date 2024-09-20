# tentukan variabel dan type data terlebih dahulu

orang1 = "Arzha"
orang2 = "Gima"

# lalu buatlah sebuah percakapan

print(f"{orang1} : halo {orang2} Gima apakah kamu homesick selama kuliah di UTM?")
print(f"{orang2} : Hai zha {orang1}, alhamdulilah udah berkurang homesickku karena udah terbiasa")
print(f"{orang1} : owalah bagus deh kalo gitu")
print(f"{orang2} : oh iya, ini kan udah mau musim praktikum  {orang1} kamu nggak pengen belajar ? (pengen sih/ nggak pengen)")
jawaban = input(f"{orang1} : ")

if jawaban.lower() == "pengen sih":
    print(f"{orang2} : wih belajar apa tuh zha?")
else:
    print(f"{orang2} : kalo aku grammar karena kan aku sastra inggris")

print(f"{orang1} : belajar coding gim, wih bahasa inggris")
print(f"{orang2} : hehe iyaa nih, eh kamu bawa modul kemarin ga si zhaa?")
print(f"{orang1} : iya aku udah bawa modulnya nya")
print(f"{orang2} : ouh iya?")

# input untuk data penugasan modul
modul_arzha =int(input(f"{orang1} : iya, aku cuma bawa"))
modul_gima =int(input(f"{orang2} : aku cuma"))

# menghitung data berbeda penugasan modul

selisih_modul =abs(modul_arzha - modul_gima)

# lanjut dengan penyeleksian untuk menentukan kondisinya
if modul_arzha>modul_gima:
    print(f"{orang1} : loh ternyata aku lebih banyak bawa {selisih_modul} modul ya dari {orang2}")
elif modul_arzha<modul_gima:
    print(f"{orang1} : loh ternyata aku lebih sedikit {selisih_modul} modul ya dari {orang2}")
else:
    print(f"{orang1} : loh ternyata hampir sama ya jumlahnya")
    
# lalu masukkan data operasi aritmatika lain
total_modul = modul_arzha
* modul_gima
total_dibagikan_dua = total_modul / 2
print(f"{orang2} : Zha kalo kita kalikan dan hasinya dibagi 2 jadi berapa ya ?")
print(f"{orang1} : eh iya berapa ya? waitt ngitung dulu")
print(f"{orang2} : modul punya mu kan {modul_arzha}, sedangkan modul ku kan {modul_gima}")
print(f"{orang1} : jadi kalau di kalikan hasilnya jadi {total_modul} buah")
print(f"{orang2} : dan hasil yang dikalikan tadi dibagi 2 jadi {total_dibagikan_dua} buah")