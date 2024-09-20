n1 = "Tamara"
n2 = "Riri"
t1 = float(input("Masukkan tinggi orang pertama (cm): "))
t2 = float(input("Masukkan tinggi orang kedua (cm): "))

print(f"\n{n1}: Haii {n2}, gimana kabarmu?")
print(f"{n2}: Kabar baik nih.")
print(f"{n1}: Eh kamu imut banget, btw tinggi kamu berapa sih?")
print(f"{n2}: Tebak dong.")
print(f"{n1}: {t2} cm, bener nggak?")
print(f"{n2}: Betul banget, {n1}. Kalo kamu, tinggi badannya berapa?")
print(f"{n1}: Aku sih sekitar {t1} cm.")
print(f"{n2}: Wah tinggi banget yah.")
print(f"{n1}: hahah iya kayanya aku ngikut papaku tingginya makanya tinggi")
print(f"{n2}: aku penasaran deh sama selisih tinggi kita")
print(f"{n1}: sama, gimana kalo kita hitung biar tau")
print(f"{n2}: gas lah")
if t1 > t2:
    selisih = t1 - t2
    print(f"{n2}: Ternyata Kamu lebih tinggi dari aku sekitar {selisih:.2f} cm.")
elif t1 < t2:
    selisih = t2 - t1
    print(f"{n2}: Wah, ternyata kamu lebih tinggi dari kamu sekitar {selisih:.2f} cm.")
else:
    print(f"{n2}: iya!")
