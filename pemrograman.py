#KAMUS 
harga = 0
qty = 0
total_harga = 0
diskon_persen = 0
harga_setelah_diskon = 0 
pembayaran = 0
kembalian = 0

#ALGORITMA
harga = int(input('harga barang : '))
qty = int(input('jumlah barang : '))
total_harga = harga * qty 
print (f'total_harga = {total_harga:,.2f}')
diskon_persen = float(input('diskon (diskon_dalam_persen): '))
diskon =total_harga * (diskon_persen /100)
harga_setelah_diskon = total_harga - diskon 
print (f'harga_setelah_diskon = {harga_setelah_diskon:,.2f}')
print('\n===========================')
pembayaran = float(input('jumlah pembayaran :'))
kembalian = pembayaran - harga_setelah_diskon 
print (f'kembalian = {kembalian:,.2f}')
print('===========================\n')


dibuat_oleh = '>>> CREATED By J'
hari_ini = 'Minggu'
if (hari_ini == 'SENIN'):
    print(f'{dibuat_oleh} - SENIN -')
elif (hari_ini == 'Selasa'):
    print(f'{dibuat_oleh} - SELASA -')
elif (hari_ini == 'Rabu'):
    print(f'{dibuat_oleh} - R A B U -')
elif (hari_ini == 'Kamis'):
    print(f'{dibuat_oleh} - KAMIS -')
elif (hari_ini == 'jumat'):
    print(f'{dibuat_oleh} - JUM"AT -')
elif (hari_ini == 'Sabtu'):
    print(f'{dibuat_oleh} - SABTU -')
elif (hari_ini == 'Minggu'):
    print(f'{dibuat_oleh} - MINGGU -')