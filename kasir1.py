pilihan="y"
while pilihan=="y":
    print("""
    ==============================
    
    Kantin Sekolah
    List Menu Makanan dan minuman
 
    ==============================
    A. Es Teh : Rp 3.000
    B. Ayam Geprek : Rp 10.000
    C. Mie Instan : Rp 5.000
    D. Nasi Goreng : Rp 14.000
    ==============================
    """)
    pesan=str(input("masukkan list abjad menu yang dipesan ="))
    jumlahpesan=int(input("masukkan jumlah pesanan ="))
    if pesan == "a":
        listnama= "Es Teh"
        harga=(11000*jumlahpesan)
        ppn= int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga*0.2)
            totalharga=int(harga-diskon+ppn)
        else:
            diskon =(0)
            totalharga=int(harga+ppn)
    elif pesan == "b":
        listnama= "Ayam Geprek"
        harga = (10000*jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            totalharga =int(harga-diskon+ppn)
        else:
            diskon =(0)
            totalharga =int(harga+ppn)
    elif pesan == "c":
        listnama= "Mie Instan"
        harga=int(5000*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon=0
        totalharga=int(harga+ppn)
    elif pesan == "d":
        listnama= "Nasi Goreng"
        harga=int(14000*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon=0
        totalharga = int(harga+ppn)
    else:
        listnama = "-"
        harga = "-"
        ppn = "-"
        diskon = "-"
        totalharga = "-"
        pilihan=input("menu tidak tersedia, silahkan masukkan abjad menu yang tersedia silahkan ulangi kembali Y/N =")
 
    print("--------------------------")
    print("Kantin Sekolah")
    print("--------------------------")
    print("Menu :",listnama)
    print("Jumlah Pesan :", jumlahpesan)
    print("Harga :", harga)
    print("Diskon :", diskon)
    print("PPN :", ppn)
    print("--------------------------")
    print("Jumlah Bayar :", totalharga)
    print("--------------------------")
    pilihan=input("apakah anda ingin order kembali Y/N =")