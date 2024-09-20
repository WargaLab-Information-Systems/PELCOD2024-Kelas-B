nama1 = "sulis"
nama2 = "dinda"

print(f"{nama1} :kabarmu piye,{nama2}enak ora ndek bangkalan")
print(f"{nama2} :enak ae opo o tumben-tumbenan takon kabarku") 
print(f"{nama1} :aku kate takon iki loh,hitung ya rek aku ndue 10 apel dan kamu kasih aku 5 lagi,berapa total apelku saiiki?")
print(f"{nama2} :totale") 
jawaban =int(input(f"{nama2} :"))

hasil = 10 + 5
if hasil == jawaban:
    print(f"{nama1} :jawabanmu bener weh")
    print(f"{nama2} :yo iyolah, itu loh gampang")
else:
    print(f"{nama1} :salah lah cuyy")
    print(f"{nama2} :terus gimana,aku gatau")

    print(f"{nama1} :gampang iku nko takon ae nang google")
    print(f"{nama2} :iyo wes")