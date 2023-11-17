anggota = ['Bryant', 'yusuf', 'raihan', 'farel']
saldo = [150000, 200000, 100000, 250000]

a = input("Masukkan Transaksi yang ingin dilakukan... ")

if a == "liat saldo":
    print(saldo)
elif a == "simpan uang":
    tambah_saldo = int(input("Masukkan nominal : "))
    saldo_baru = saldo + tambah_saldo
    print(saldo_baru)

    aksi_baru = input("Masukkan Transaksi yang ingin dilakukan : ")

    if aksi_baru == "tarik uang":
        tarik_uang = int(input("Masukkan nominal : "))

        if tarik_uang > saldo_baru:
            print("saldo anda tidak mencukupi")
        else:
            saldo_tarik = saldo_baru - tarik_uang
            print(
                f"transaksi berhasil \n saldo anda sekarang {saldo_tarik}")
    elif aksi_baru == "transfer":
        nominal_transfer = int(input("Masukkan nominal : "))

        if nominal_transfer > saldo_baru:
            print("saldo anda tidak mencukupi")
        else:
            saldo_transaksi = saldo_baru - nominal_transfer
            print(f"transfer berhasil \n saldo anda {saldo_transaksi}")
    else:
        keluar = input('tekan enter sekali untuk keluar: ')

elif a == "tarik uang":
    tarik_uang = int(input("Masukkan nominal : "))

    if tarik_uang > saldo:
        print("saldo anda tidak mencukupi")
    else:
        saldo_tarik = saldo - tarik_uang
        print(
            f"transaksi berhasil \n saldo anda sekarang {saldo_tarik}")
elif a == "transfer":
    nominal_transfer = int(input("Masukkan nominal : "))

    if nominal_transfer > saldo:
        print("saldo anda tidak mencukupi")
    else:
        saldo_transaksi = saldo - nominal_transfer
        print(f"transfer berhasil \n saldo anda {saldo_transaksi}")
else:
    keluar = input('tekan enter sekali untuk keluar: ')
