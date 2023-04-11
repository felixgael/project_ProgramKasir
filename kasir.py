print("****** Warteg Mbah Sugi Ono ******")
print("-----------------------------------")
pembeli = input('Nama pembeli : ')

harga = []
barang = []
total_PerItem = []
while True:
    print('''
     ========== Daftar Menu =============
    |KODE|     Menu     | Harga |
    ---------LIST MAKANAN---------------
    | NG  | Nasi goreng  | Rp. 12.000,00|
    | PA  | Pecel ayam   | Rp. 22.000,00| 
    | AB  | Ayam bakar   | Rp. 18.000,00|
    ---------LIST MINUMAN---------------
    | ET  | Es Teh       | Rp. 5.000,00|
    | EJ  | Es jeruk     | Rp. 8.000,00| 
    | AM  | Air mineral  | Rp. 4.000,00|    
    ''')

#menu input
    kode = input("Masukkan kode barang : ")
    jumlah = int(input("Jumlah pesanan : "))
    if kode == "NG" or kode == "ng":
        barang.append("Nasi goreng")
        harga.append(12000)
        total_harga = jumlah * 12000
        total_PerItem.append(total_harga)
    elif kode == "PA" or kode == "pa":
        barang.append("Pecel ayam")
        harga.append(22000)
        total_harga = jumlah * 22000
        total_PerItem.append(total_harga)
    elif kode == "AB" or kode == "ab":
        barang.append("Ayam bakar")
        harga.append(18000)
        total_harga = jumlah * 18000
        total_PerItem.append(total_harga)
    elif kode == "ET" or kode == "et":
        barang.append("Es teh")
        harga.append(5000)
        total_harga = jumlah * 5000
        total_PerItem.append(total_harga)
        print(barang,total_harga)
    elif kode == "EJ" or kode == "ej":
        barang.append("Es jeruk")
        harga.append(8000)
        total_harga = jumlah * 8000
        total_PerItem.append(total_harga)
    elif kode == "AM" or kode == "am":
        barang.append("Air mineral")
        harga.append(4000)
        total_harga = jumlah * 4000
        total_PerItem.append(total_harga)
    else:
        print("Menu tidak tersedia, silahkan ulangi kembali !")
        continue

    while True :
        pilihan = input("Tambah pesanan ?\n masukkan (Y / N) : ")
        if pilihan == "Y" or pilihan == "y":
            kode_tambah = input("Masukkan kode barang : ")
            jml_tambah = int(input("Masukkan jumlah pesanan : "))
            if kode_tambah == "NG" or kode_tambah == "ng":
                barang.append("Nasi goreng")
                harga.append(12000)
                total_harga = jml_tambah * 12000
                total_PerItem.append(total_harga)
            elif kode_tambah == "PA" or kode_tambah == "pa":
                barang.append("Pecel ayam")
                harga.append(22000)
                total_harga = jml_tambah * 22000
                total_PerItem.append(total_harga)
            elif kode_tambah == "AB" or kode_tambah == "ab":
                barang.append("Ayam bakar")
                harga.append(18000)
                total_harga = jml_tambah * 18000
                total_PerItem.append(total_harga)
            elif kode_tambah == "ET" or kode_tambah == "et":
                barang.append("Es teh")
                harga.append(5000)
                total_harga = jml_tambah * 5000
                total_PerItem.append(total_harga)
            elif kode_tambah == "EJ" or kode_tambah == "ej":
                barang.append("Es jeruk")
                harga.append(8000)
                total_harga = jml_tambah * 8000
                total_PerItem.append(total_harga)
            elif kode_tambah == "AM" or kode_tambah == "am":
                barang.append("Air mineral")
                harga.append(4000)
                total_harga = jml_tambah * 4000
                total_PerItem.append(total_harga)
            else:
                print("Menu tidak tersedia, silahkan ulangi kembali !")
                continue
        else:
            print("")
            break

    #Total harga
    print("-----------------------------------")
    print("****** Warteg Mbah Sugi Ono ******")
    print("-----------------------------------")
    print("Nama Pembeli        :",pembeli)
    print("Pesanan             :",barang)
    print("Harga per item      :",total_PerItem)
    total_belanja = sum(total_PerItem)
    #print("Jumlah              : Rp",total_belanja)

    #Discount
    if total_belanja >=70000:
        discount = 0.05*total_belanja
    else:
        discount = 0

    print("Diskon              : Rp",discount)
    print("Total               : Rp",total_belanja-discount)

    total_bayar = total_belanja-discount
    print("-----------------------------------")

#Pembayaran
    bayar = int(input("Bayar               : Rp "))
    if bayar > total_bayar:
        print("kembali             : Rp",bayar-total_bayar)
    elif bayar == total_bayar:
        print("kembali             : Rp",bayar-total_bayar)
    else:
        print("Pembayaran kurang   :Rp.",bayar-total_bayar)
    break





