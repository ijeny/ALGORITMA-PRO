import math
#variabel 
diskon = 0 
pembelian = 0

#memasukkan total belanja
pembelian = float(input("masukkan total belanja = Rp "))
#penghitungan selection
if(pembelian >= 500000):
    harga_diskon = pembelian * 0.05
else:
    harga_diskon = 0
print(f"diskon = {harga_diskon:,.2f} ")