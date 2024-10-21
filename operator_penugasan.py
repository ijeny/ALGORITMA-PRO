#DEKLARASI VARIABEL
bil1 = 0
bil2 = 0
jumlah = 0
kurang = 0
kali = 0
bagi = 0
hasil_bagi = 0
sisa_bagi = 0
pangkat = 0

#INPUT
bil1 = int(input("masukkan bilangan 1 : "))
bil2 = int(input("masukkan bilangan 2 : "))
jumlah = kurang = kali = bagi = hasil_bagi = sisa_bagi = pangkat = bil1

#PROSES
jumlah += bil2 
kurang -= bil2
kali *= bil2
bagi /= bil2
hasil_bagi //= bil2
sisa_bagi %= bil2
pangkat **= bil2

#OUTPUT
print()
print(f"hasil penjumlahan     : {jumlah}")
print(f"hasil pengurangan     : {kurang}")
print(f"hasil perkalian       : {kali}")
print(f"hasil pembagian       : {bagi:.2f}")
print(f"hasil pembagian genap : {hasil_bagi}")
print(f"sisa hasil bagi       : {sisa_bagi}")
print(f"hasil perpangkatan    : {pangkat}")