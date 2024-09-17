orang1 = "amel"
orang2 = "marvin"

print(f"{orang1} : halo, marvin. apa kabar?")
print(f"{orang2} : hai amel, kabar baik, kamu?")
print(f"{orang1} : aku juga baik - baik saja")
print(f"{orang2} : anw umur kamu berapa amel?")
Umur1=int(input(f"{orang1} :"))

# Operasi logika
if Umur1 == 18:
    print(f"{orang2} : Umur kita sama dong")
else:
    print(f"{orang2} : Ternyata umur kita beda ya")


Umur2=int(input(f"{orang1} : Oh kalau aku  "))
print(f"{orang2} : kira-kira umur kita kalau di tambah jadi berapa ya?")

# operasi aritmatika
total_umur= abs(Umur1+Umur2)
print(f"{orang1} : Umur kamu kan {Umur1} tahun terus kalau aku {Umur2} tahun jadi totalnya {total_umur}")


print(f"{orang2} : oiya, kost kamu dimana?")
print(f"{orang1} : aku kost di Graha Trunojoyo, kamu?")
print(f"{orang2} : kalau aku kost di graha kamal")
print(f"{orang1} : oh jauh banget, kapan-kapan main yuk")
print(f"{orang2} : boleh-boleh")
