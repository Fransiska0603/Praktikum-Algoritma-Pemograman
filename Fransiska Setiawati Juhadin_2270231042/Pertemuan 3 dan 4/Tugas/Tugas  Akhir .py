print("-----Fransiska Setiawati Juhadin")
print("----------warteg Santuy----------")
print("----------2270231042----------")


nama = input("Nama Pelanggan : ")
tanggal = input ("Tanggal Pembelian : ")
alamat = print("Jalan Gang Sadar 1 RT.02/RW.01,JatiMurni,Kampung Sawah, Kec. Pondok Melati, Kota Bekasi,Jawa Barat")
notelp = print ("500600")
print("--------------------------------------") 
print("       ======== Menu ========         ")
print("--------------------------------------")
print("1. Ayam Goreng           	Rp. 10000")
print("2. Perkedel	                Rp.  7000")
print("3. Kentang Balado	        Rp.  5000")
print("4. Sayur Sop	                Rp. 12000") 
print("5. Ikan Goreng               Rp. 11000") 
print("6. Telor Balado	            Rp.  6000") 
print("--------------------------------------")
h = []
a = 1

menu_pesanan = int(input("Masukan Menu Pesanan : "))
if menu_pesanan == 1: 
    harga = 10000
elif menu_pesanan == 2: 
    harga = 7000
elif menu_pesanan == 3: 
    harga = 5000
elif menu_pesanan == 4: 
    harga = 12000
elif menu_pesanan == 5:
    harga = 11000
elif menu_pesanan == 6:
    harga = 6000
else:
    while True:
        print("==== Menu tidak tersedia silahkan pilih menu lainnya ====")
        if menu_pesanan == 1 or menu_pesanan == 2 or menu_pesanan == 3 or menu_pesanan == 5 or menu_pesanan == 6:
         if menu_pesanan == 1: 

            harga = 10000
        elif menu_pesanan == 2: 
            harga = 7000
        elif menu_pesanan == 3:
            harga = 5000
        elif menu_pesanan == 4:
            harga = 12000
        elif menu_pesanan == 5: 
            harga = 11000
        elif menu_pesanan == 6:
            harga = 6000
            break

jumlah_pembelian = int(input("Masukan Jumlah Pembelian : "))
for i in range(jumlah_pembelian): h.append(harga)

while True:
    jawab = input("Apakah ada yang ingin ditambah/dikurangi? tambah/kurang/n?")
    if jawab == 'tambah':
        tambah = int(input("Masukan Menu Pesanan :"))
        if tambah == 1: 
            harga = 10000
        elif tambah == 2: 
            harga = 7000
        elif tambah == 3: 
            harga = 5000
        elif tambah == 4:
            harga = 12000
        elif tambah == 5: 
            harga = 11000
        elif tambah == 6: 
            harga = 6000
    jumlah_tambahan = int(input("Masukan Jumlah Tambahan : "))
    for i in range(jumlah_tambahan): 
        h.append(harga)
    c = jumlah_tambahan + jumlah_pembelian 
    print("Total Pesanan: ",c)
    bayar = sum(h)
    print("Total Pembayaran: Rp.{}",format(bayar))
    break
kurang = int(input("Berapa jumlah yang ingin dikurangkan? : "))
for i in range(kurang):
    if      kurang <= 1: 
            a -= kurang 
            del h[a]
            bayar = sum(h)
            break 
    else:
        kurang -= a 
        del h[kurang] 
        if kurang < 0:
            break
    c = jumlah_pembelian - kurang 
    print("Total Pemesanan: ",c) 
    bayar = sum(h)
    print("Total Pembayaran: Rp.{}",format(bayar))
    break
else:
    bayar = sum(h)
    c = jumlah_pembelian 
    print("Total Pemesanan: ",c)
    print("Total Pembayaran: Rp.{}",format(bayar))