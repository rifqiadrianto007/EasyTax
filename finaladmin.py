import csv
import os
import datetime
from datetime import datetime
import time
from tabulate import tabulate


def loginuser():
    os.system('cls')
    print("==========CEK PLAT NOMOR==========")
    platnomor = str.upper(input("Masukkan Plat Nomor : "))
    file = open('data NIM.csv', 'r')
    # variabel F digunakan untuk mengecek apakah data ditemukan atau tidak, jika tidak ditemukan maka akan bernilai False
    F = False
    # looping untuk membaca file tiap barisnya  
    for line in file :
        # variabel item digunakan untuk menyimpan data yang telah dipisahkan dengan koma 
        item = line.split(',')
        # jika data yang dicari ditemukan maka akan bernilai True, item berisi data yang telah dipisahkan 
        # dengan koma dari file csv yang sudah dialokasikan ke variabel line 
        if platnomor == item[2] :
            # jika data ditemukan maka variabel F akan bernilai True
            F = True
            # break digunakan untuk menghentikan looping ketika kondisi F terpenuhi
            break
    # jika variabel F bernilai True maka akan menjalankan perintah dibawahnya
    if F == True : 
        print("Login Anda Berhasil")
    else :
        print("Login Anda Gagal")
        time.sleep(1)
        loginuser()
        
    with open('data NIM.csv', 'r') as file_csv:
        # variabel data digunakan untuk menyimpan data yang akan kita cari
        data = []
        # nilai pencarian ini kita ambil dari plat nomor yang telah diinputkan
        nilai_pencarian = platnomor
        # variabel reader digunakan untuk membaca file csv
        reader = csv.reader(file_csv)
        # variabel header digunakan untuk skip baris pertama yang berisi header
        header = next(reader)
        # variabel indeks_kolom digunakan untuk menampung indeks kolom yang akan kita cari
        indeks_kolom = None
        
        # perulangan untuk mencari indeks kolom, dan enumerate digunakan untuk mengembalikan indeks dan elemen dari list
        for i, kolom in enumerate(header): 
            if kolom == 'No. Plat':
                indeks_kolom = i
                break
            
        # perulangan diatas digunakan untuk mencari indeks dari row, jadi "i" akan berisi indeks dari row dan "kolom" akan berisi elemen dari row
        # memulai looping untuk mencari data yang kita cari
        for row in reader: 
            if row[indeks_kolom] == nilai_pencarian:
                # jika nilai pencarian yaitu plat nomor sama dengan row[indeks_kolom] maka data akan berisi row, 
                # row[indeks kolom] sendiri aslinya adalah row[2] karena indeks kolom dari NO. PLAT adalah 2
                data = row
            
        def tanggal():
            os.system('cls')
            print(f"""
                {"-"*(60)}
                |{"MASUKKAN TANGGAL JATUH TEMPO".center(58)}|
                {"-"*(60)}
                  """)
            # try digunakan untuk mengecek apakah inputan yang dimasukkan adalah angka atau bukan
            try : 
                hari = input("Tanggal = ")
                # ini pembatasan inputan tidak boleh lebih dari 31
                if int(hari) <= 31: 
                    pass
                else :
                    print("Hari yang anda masukkan tidak valid")
                    time.sleep(1)
                    tanggal()

                bulan = input("Bulan = ")
                # ini pembatasan inputan tidak boleh lebih dari 12
                if int(bulan) <= 12: 
                    pass
                else:
                    print("Bulan yang Anda masukkan ngaworr!!")
                    time.sleep(1)
                    tanggal()
                
                tahun = input("Tahun = ")
                # ini pembatasan inputan yang panjangnya tidak boleh kurang dari 4 dan angkanya tidak boleh kurang dari 2000
                if len(tahun) >= 4 and (int(tahun)) >= 2000: 
                    pass
                else:
                    print("Tahun yang Anda masukkan tidak benarr!!")
                    time.sleep(1)
                    tanggal()
            # except digunakan ketika inputan yang dimasukkan bukan angka maka akan mengembalikan error dan input ulang       
            except ValueError: 
                print("Masukkan data yang valid!")
                time.sleep(1)
                tanggal()
                
            os.system('cls')
            # variabel n digunakan untuk menyimpan tanggal yang telah diinputkan
            n = (f"{hari}/{bulan}/{tahun}")
            # ini pembatasan inputan tanggal yang panjangnya tidak boleh lebih dari 10, karena format tanggal adalah dd/mm/yyyy
            if len(n) <= 10: 
                #format tanggal hari/bulan/tahun
                format_tanggal = "%d/%m/%Y"
                # variabel i digunakan untuk menyimpan tanggal yang telah diinputkan dengan format yang telah ditentukan
                i = datetime.strptime(n, format_tanggal)
                # variabel u digunakan untuk menyimpan tanggal dari data csv yang telah diinputkan dengan format yang telah ditentukan
                u = datetime.strptime(data[5], format_tanggal) 
                # tanggal data csv dikurangi dengan tanggal yang diinputkan
                z = u - i 
                # tanggal yang diinputkan dikurangi dengan tanggal data csv
                t = i - u 
                # variabel berikut nantinya akan diisi dengan hasil operasi tanggal
                tahun_sisa = 0
                bulan_sisa = 0
                hari_sisa = 0
               
               
                # jika tanggal yang diinputkan sama dengan tanggal data csv
                if i == u: 
                    print(f"Jenis Kendaraan \t= {data[4]}")
                    print(f"Dengan Plat Nomor \t= {data[2]}")
                    print(f"Atas Nama \t\t= {data[3]}")
                    print(f"Tanggal Jatuh Tempo \t= {data[5]}")
                    print("Status \t\t= Anda Telah Memasuki Jatuh Tempo Pembayaran")
                # jika tanggal yang diinputkan lebih kecil dari tanggal data csv   
                elif i < u: 
                    print(f"Jenis Kendaraan \t= {data[4]}")
                    print(f"Dengan Plat Nomor \t= {data[2]}")
                    print(f"Atas Nama \t\t= {data[3]}")
                    print(f"Tanggal Jatuh Tempo \t= {data[5]}")
                    # jika selisih tanggal lebih dari 365 hari maka akan dihitung berapa tahun dan bulan yang tersisa
                    if int(str(z.days)) > 365: 
                        # z.days artinya selisih tanggal dalam bentuk hari, lalu dibagi 365 untuk menghitung berapa tahun yang tersisa
                        tahun_sisa += z.days // 365
                        # sisa dari pembagian z.days dengan 365, lalu dibagi 30 untuk menghitung berapa bulan yang tersisa
                        bulan_sisa += (z.days % 365) // 30 
                        print(f"Status \t\t\t= Jatuh Tempo Pembayaran Anda {tahun_sisa} tahun {bulan_sisa} bulan lagi")
                    # jika selisih tanggal lebih dari 30 hari maka akan dihitung berapa bulan dan hari yang tersisa
                    elif int(str(z.days)) > 30: 
                        bulan_sisa += z.days // 30
                        hari_sisa += z.days % 30
                        print(f"Status \t\t\t= Jatuh Tempo Pembayaran Anda {bulan_sisa} bulan {hari_sisa} hari lagi")
                    else:
                        print(f"Status \t\t\t= Jatuh Tempo Pembayaran Anda {z.days} hari lagi")
                # jika tanggal yang diinputkan lebih besar dari tanggal data csv       
                elif i > u: 
                    print(f"Jenis Kendaraan \t= {data[4]}")
                    print(f"Dengan Plat Nomor \t= {data[2]}")
                    print(f"Atas Nama \t\t= {data[3]}")
                    print(f"Tanggal Jatuh Tempo \t= {data[5]}")
                    # jika selisih tanggal lebih dari 365 hari maka akan dihitung berapa tahun dan bulan yang terlambat
                    if int(str(t.days)) > 365: 
                        tahun_sisa += t.days // 365
                        bulan_sisa += (t.days % 365) // 30
                        print(f"Status \t\t\t= Anda TELAT Membayar Pajak {tahun_sisa} tahun {bulan_sisa} bulan !!!")
                    elif int(str(t.days)) > 30:
                        bulan_sisa += t.days // 30
                        hari_sisa += t.days % 30
                        print(f"Status \t\t\t= Anda TELAT Membayar Pajak {bulan_sisa} bulan {hari_sisa} hari !!!")
                    else:
                        print(f"Status \t\t\t= Anda TELAT Membayar Pajak {t.days} hari !!!")
            else:
                print("Tanggal yang Anda masukkan tidak valid!!!")
                tanggal()
                           
            print("\n\n=====TEKAN APA SAJA UNTUK KEMBALI=====")
            e = input("")
            if e == "":
                menu()
            else :
                menu()

                
        def pembayaran():
            os.system('cls')
            motor = 300000
            mobil = 1000000
            format_tanggal = "%d/%m/%Y"
            # ariabel i digunakan untuk menyimpan tanggal dari data csv yang telah diinputkan dengan format yang telah ditentukan
            i = datetime.strptime(data[5], format_tanggal) 
            # variabel u digunakan untuk menyimpan tanggal sekarang
            u = datetime.now() 
            # variabel s digunakan untuk menyimpan selisih tanggal dalam bentuk hari kemudian dirubah ke bentuk string
            s = str((u-i).days) 
            # variabel n digunakan untuk menyimpan selisih tanggal dalam bentuk bulan
            n = (u-i) // 30 
            # variabel m digunakan untuk menyimpan n yang dirubah menjadi hari dalam bentuk string
            m = str(n.days) 
            telat_tahun = 0
            telat_bulan = 0
            telat_hari = 0
            denda = int(0)
            biaya_total = int(0)

            # jika selisih tanggal kurang dari 0 hari dan kurang dari 1 bulan maka akan menjalankan perintah dibawahnya
            if int(s) <= 0 and int(m) < 1: 
                print("="*60)
                print("="*60)
                print("".center(58))
                print (f"MANTAPPP ANDA DISIPLIN MEMBAYAR PAJAK".center(58))
                print("".center(58))
                print("="*60)
                if data[4] == "Motor":
                    # jika jenis kendaraan adalah motor maka biaya total akan ditambah dengan biaya motor yang sudah dideklarasikan diatas
                    biaya_total += motor
                    print(f"Biaya Pajak Anda adalah Rp. {motor}") 
                elif data[4] == "Mobil":
                    print(f"Biaya Pajak Anda adalah Rp. {mobil}") 
                    # jika jenis kendaraan adalah mobil maka biaya total akan ditambah dengan biaya mobil yang sudah dideklarasikan diatas
                    biaya_total += mobil 
                print (f"\n\t Biaya Total Pajak Anda adalah = Rp. {int(biaya_total)}".center(60))
                print("".center(58))
                print("="*60)
            # jika selisih tanggal lebih dari 2 hari dan kurang dari 1 bulan maka akan menjalankan perintah dibawahnya
            elif int(s) >= 2 and int(m) <= 1: 
                # jika selisih tanggal lebih dari 365 hari maka akan dihitung berapa tahun dan bulan yang terlambat
                if int(s) > 365: 
                    telat_tahun += ((u-i).days) // 365
                    telat_bulan += (((u-i).days) % 365) // 30
                    print("="*70)
                    print("".center(68))
                    print(f"YAAHHH ANDA TELAT MEMBAYAR PAJAK {telat_tahun} TAHUN {telat_bulan} BULAN".center(68))
                    print("".center(68))
                    print("="*70)
                # jika selisih tanggal lebih dari 30 hari maka akan dihitung berapa bulan dan hari yang terlambat
                elif int(s) > 30: 
                    telat_bulan += ((u-i).days) // 30
                    telat_hari += ((u-i).days) % 30
                    print("="*70)
                    print("".center(68))
                    print(f"YAAHHH ANDA TELAT MEMBAYAR PAJAK {telat_bulan} BULAN {telat_hari} HARI".center(68))
                    print("".center(68))
                    print("="*70)
                else:
                    print("="*70)
                    print("".center(68))
                    print(f"==========YAHHH ANDA TELAT MEMBAYAR PAJAK {(u-i).days} HARI==========".center(68))
                    print("".center(68))
                    print("="*70)
                if data[4] == "Motor":
                    # denda dihitung dari biaya motor dikali 25% lalu ditambah dengan biaya motor
                    denda += motor*(25/100) 
                    # biaya total ditambah dengan biaya motor dan denda
                    biaya_total += motor + denda 
                    print(f"Biaya Pajak Anda adalah Rp. {motor}")
                elif data[4] == "Mobil":
                    denda += mobil*(25/100)
                    biaya_total += mobil + denda
                    print(f"Biaya Pajak Anda adalah Rp. {mobil}") 
                print(f"\nANDA TERKENA DENDA SEBESAR RP. {int(denda)}".center(68))
                print("".center(68))
                print("="*70)
                print(f"\nTOTAL BIAYA PAJAK ANDA ADALAH RP. {int(biaya_total)}".center(68))
                print("".center(68))
                print("="*70)
            # jika selisih tanggal lebih dari 1 bulan dan kurang dari 2 bulan maka akan menjalankan perintah dibawahnya
            elif int(m) > 1 and int(m) <= 2: 
                # jika selisih tanggal lebih dari 365 hari maka akan dihitung berapa tahun dan bulan yang terlambat
                if int(s) > 365: 
                    telat_tahun += ((u-i).days) // 365
                    telat_bulan += (((u-i).days) % 365) // 30
                    print("="*70)
                    print("".center(68))
                    print(f"YAAHHH ANDA TELAT MEMBAYAR PAJAK {telat_tahun} TAHUN {telat_bulan} BULAN".center(68))
                    print("".center(68))
                    print("="*70)
                # jika selisih tanggal lebih dari 30 hari maka akan dihitung berapa bulan dan hari yang terlambat
                elif int(s) > 30: 
                    telat_bulan += ((u-i).days) // 30
                    telat_hari += ((u-i).days) % 30
                    print("="*70)
                    print("".center(68))
                    print(f"YAAHHH ANDA TELAT MEMBAYAR PAJAK {telat_bulan} BULAN {telat_hari} HARI".center(68))
                    print("".center(68))
                    print("="*70)
                else:
                    print("="*70)
                    print("".center(68))
                    print(f"YAHHH ANDA TELAT MEMBAYAR PAJAK {(u-i).days} HARI".center(68))
                    print("".center(68))
                    print("="*70)
                    
                if data[4] == "Motor":
                    # rumus menghitung pajak
                    denda += (motor*25/100*2//12)+32000
                    biaya_total += motor + denda
                    print(f"Biaya Pajak Anda adalah Rp. {motor}")
                elif data[4] == "Mobil":
                    denda += (mobil*25/100*2//12)+100000
                    biaya_total += mobil + denda
                    print(f"Biaya Pajak Anda adalah Rp. {mobil}") 
                    print(f"\nANDA TERKENA DENDA SEBESAR RP. {int(denda)}".center(68)) 
                    print("".center(68))
                    print("="*70)
                    print(f"\nTOTAL BIAYA PAJAK ANDA ADALAH RP. {int(biaya_total)}".center(68))
                    print("".center(68))
                    print("="*70)
            else :
                if int(s) > 365:
                    telat_tahun += ((u-i).days) // 365
                    telat_bulan += (((u-i).days) % 365) // 30
                    print("="*70)
                    print("".center(68))
                    print(f"YAAHHH ANDA TELAT MEMBAYAR PAJAK {telat_tahun} TAHUN {telat_bulan} BULAN".center(68))
                    print("".center(68))
                    print("="*70)
                elif int(s) > 30:
                    telat_bulan += ((u-i).days) // 30
                    telat_hari += ((u-i).days) % 30
                    print("="*70)
                    print("".center(68))
                    print(f"YAAHHH ANDA TELAT MEMBAYAR PAJAK {telat_bulan} BULAN {telat_hari} HARI".center(68))
                    print("".center(68))
                    print("="*70)
                else:
                    print(f"\nYAHHH ANDA TELAT MEMBAYAR PAJAK {(u-i).days} HARI".center(68))
                    print("".center(68))
                    print("="*70)

                if data[4] == "Motor":
                    denda += (motor*25/100*6//12)+32000
                    biaya_total += motor + denda
                    print(f"Biaya Pajak Anda adalah Rp. {motor}")
                elif data[4] == "Mobil":
                    denda += (mobil*25/100*6//12)+100000
                    biaya_total += mobil + denda
                    print(f"Biaya Pajak Anda adalah Rp. {mobil}") 
                print(f"\nANDA TERKENA DENDA SEBESAR RP. {int(denda)}".center(68))
                print("".center(68))
                print("="*70)
                print(f"\nTOTAL BIAYA PAJAK ANDA ADALAH RP. {int(biaya_total)}".center(68))
                print("".center(68))
                print("="*70)
                
            def bayar():
                i = input("\n\nApakah anda akan membayar? [y/n] : ")
                def online():
                    # variabel kode_pembayaran digunakan untuk menyimpan kode pembayaran
                    kode_pembayaran = "" 
                    # variabel u digunakan untuk menyimpan tanggal sekarang dan dirubah ke format tanggal
                    u = datetime.now() 
                    # format tanggal
                    kode_tanggal = u.strftime("%d%m%Y") 
                    print("\n----------Pembayaran Online----------")
                    print("1. Dana")
                    print("2. M-Banking")
                    k = input("Pilih Metode pembayaran = ")
                    if k == "1":
                        os.system('cls')
                        # kode pembayaran terdiri dari DANA + tanggal + 4 digit terakhir dari NIM
                        kode_pembayaran = "DANA" + kode_tanggal + str(data[1][8:12]) 
                        print("\n====================================================")
                        print("========== S T R U K   P E M B A Y A R A N =========")
                        print("====================================================")
                        print ("Nama\t\t\t:", data[3])
                        print ("NIM\t\t\t:", data[1])
                        print ("Plat Nomor\t\t:", data[2])
                        print ("Jenis Kendaraan\t\t:", data[4])
                        print ("Biaya\t\t\t: Rp.", int(biaya_total))
                        print ("Metode Pembayaran\t: Dana")
                        print ("Kode Pembayaran\t\t:", kode_pembayaran)
                        print("====================================================")
                        print("====================================================")
                        print("\n\n ==========TEKAN APA SAJA UNTUK KEMBALI KE MENU==========")
                        j = input("")
                        if j == "":
                            menu()
                        else:
                            menu()
                            
                    elif k == "2":
                        os.system('cls')
                        # kode pembayaran terdiri dari MBANK + tanggal + 4 digit terakhir dari NIM
                        kode_pembayaran = "MBANK" + kode_tanggal + str(data[1][8:12]) 
                        print("\n====================================================")
                        print("========== S T R U K   P E M B A Y A R A N =========")
                        print("====================================================")
                        print ("Nama\t\t\t:", data[3])
                        print ("NIM\t\t\t:", data[1])
                        print ("Plat Nomor\t\t:", data[2])
                        print ("Jenis Kendaraan\t\t:", data[4])
                        print ("Biaya\t\t\t: Rp.", int(biaya_total))
                        print ("Metode Pembayaran\t: M-Banking")
                        print ("Kode Pembayaran\t\t:", kode_pembayaran)
                        print("====================================================")
                        print("====================================================")
                        print("\n\n ==========TEKAN APA SAJA UNTUK KEMBALI KE MENU==========")
                        j = input("")
                        if j == "":
                            menu()
                        else:
                            menu()
                            
                    else :
                        print("Pilihan Anda Salah")
                        print("\n ==========TEKAN APA SAJA UNTUK KEMBALI KE MENU==========")
                        j = input("")
                        if j == "":
                            menu()
                        else:
                            menu()
                    
                def offline():
                    # upper digunakan untuk mengubah inputan menjadi huruf kapital
                    os.system('cls')
                    sm = str.upper(input("Masukkan Kota Anda = "))
                    os.system('cls')
                    print("\n\n\t\t\t\tSILAHKAN MENUJU SAMSAT TERDEKAT\n\n".center(100))
                    with open('samsatbaru.csv', 'r') as f:
                        samsat = []
                        reader = csv.reader(f)
                        header = next(reader)
                        indeks_kolom = None
                        for i, kolom in enumerate(header):
                            if kolom == 'KOTA':
                                indeks_kolom = i
                                break
                        for row in reader:
                            if row[indeks_kolom] == sm:
                                samsat = row
                                tabel_samsat = [header, samsat]
                                table = tabulate(tabel_samsat, tablefmt='grid')
                        
                        # kode diatas sama seperti saat mengecek plat nomor, cuma bedanya ini digunakan untuk menampilkan datanya
                        # ini syarat agar program berjalan atau tidak
                        penentu = False 
                        #jika nilai dari samsat yang sudah kita ambil dari row dan "sm" yaitu inputan kota dari user ada di samsat[0] 
                        # maka penentu akan menjadi True dan program akan melanjutkannya ke print tabel
                        if samsat and sm == samsat[0]: 
                            penentu = True
                        elif not samsat:
                            penentu = False
                        
                        if penentu == True:
                            print(table)
                        else:
                            print("Kota Anda Tidak Terdaftar")
                            time.sleep(0.5)
                            offline()
                            
                        g = input("\n\t\t\t=====TEKAN APA SAJA UNTUK KEMBALI KE MENU AWAL=====")
                        if g == "":
                            loginuser()
                        else :
                            loginuser()

                if i == "y" :
                    os.system('cls')
                    print("\n----------Pilih Metode Pembayaran----------")
                    print("1. Online")
                    print("2. Offline")
                    u = input("Online atau Offline : ")
                    if u == "1" :
                        online()
                    elif u == "2" :
                        offline()
                    else :
                        print("Pilihan Anda Salah")
                        time.sleep(0.5)
                        bayar()
                    
                elif i == "n" :
                    menu()
                else :
                    print("input anda salah")
                    time.sleep(0.5)
                    bayar()
          
            bayar()
             
                   
    def menu():
        os.system('cls')
        print(f"""
        {"-"*(60)}
        |{"PILIH MENU".center(58)}|   
        |{"-"*(58)}|   
        |{"[1] Jatuh Tempo".ljust(58)}|
        |{"[2] Bayar".ljust(58)}|
        |{"[3] Cek Plat Nomor Ulang".ljust(58)}|
        |{"[4] Kembali Ke Menu Awal".ljust(58)}|
        |{''.center(58)}|   
        {"-"*(60)}
                    """)
        p = input("Menu yang diinginkan = ")
        if p == "1":
            tanggal()
        elif p == "2":
            pembayaran()
        elif p == "3":
            loginuser()
        elif p == "4":
            exitkuy()
        else:
            print("Menu tidak valid")
            time.sleep(0.5)
            menu()   
    time.sleep(1)
    menu()   

    

# input username akan memeriksa csv user pada row 0 yang berisi daftar username admin, 
# sedangkan password pada row 1, kesalahan akan diberi waktu 1 detik untuk mengulang   
def login():
    os.system('cls')
    print("Login Admin")
    print("===========")
    username = input("Username: ")
    password = input("Password: ")

# program akan memerika tiap - tiap baris dari data NIM, dan akan berhenti ketika sudah menemukan data yang benar
    login_successful = False 

    with open('user.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
           if row[0] == username and row[1] == password and row[2] == "admin":
                login_successful = True
                break 

    if login_successful:
        print("Login berhasil")
        menu_admin()
    else:
        print("Login gagal")
        time.sleep(1)
        login()


# setiap pilihan menu diberikan opsi yang nantinya akan memanggil function dari masing - masing fitur
def menu_admin():
    os.system('cls')
    print("Menu Admin")
    print("=====")
    print("============== MANAGE DATA ==============")
    print("1. Tambahkan Data")
    print("2. Tamplikan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("============== MANAGE ADMIN ==============")
    print("5. Daftar Admin")
    print("6. Tambah admin")
    print("7. Hapus admin")
    print("============== KELUAR ==============")
    print("8. Cari Data")
    print("9. Keluar")

    menu = input("Pilih menu :")
    if menu == "1":
        create()
    elif menu == "2":
        read()
    elif menu == "3":
        update()
    elif menu == "4":
        delete()
    elif menu == "5":
        daftar_admin()
    elif menu == "6":
        tambah_admin()
    elif menu == "7":
        hapus_admin()
    elif menu == "8":
        jenis_cari()
    elif menu == "9":
        exitkuy()
    else:
        print("Menu tidak tersedia")


# menambahkan data pada csv NIM yang nantinya akan mengubah NIM menjadi nomor plat dengan mengambil 4 angka terakhir
def create():
    os.system('cls')
    print("Create")
    print("======")
    nama =  str.upper(input("Nama: "))
    nim = input("NIM: ")
    empat_angka = nim[-4:]
    no_plat = f'P{empat_angka}IF'
    jenis_ken = (input("Jenis Kendaraan: "))
    tanggal_tempo = input("Tanggal Jatuh Tempo :")

# data yang baru ditambahkan akan otomatis berada di paling bawah dengan nomor urut menyesuaikan nomor terakhir
    with open('data NIM.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        data_csv = list(csv_reader)
        new_no = len(data_csv) + 1
    
    with open('data NIM.csv', mode='a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow([new_no, nim, no_plat, nama, jenis_ken, tanggal_tempo])   
        print("Data berhasil ditambahkan")
    
    pilihan = input("Kembali ke menu admin? (y/n) ")
    if pilihan == "y":
        menu_admin()
    else:
        exitkuy()


# menampilkan semua data dalam data NIM menggunakan perintah with open sebagai pengganti open dan close
def read():
    os.system('cls')
    print("Read")
    print("=====")
    with open('data NIM.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if len(row) >= 5:
             print("No: " + row[0])
             print("Nama: " + row[1])
             print("NIM: " + row[2])
             print("No Plat: " + row[3])
             print("Jenis Kendaraan: " + row[4])
             print("Tanggal Jatuh Tempo:" + row[5])
             print("\n")
            else:
             print("SEMENTARA HANYA INI YANG BISA DITAMPILKAN")
             
    pilihan = input("Kembali ke menu admin? (y/n)")
    if pilihan == "y":
        menu_admin()
    else:
        exitkuy()
        
# memperbarui data sesuai nomor urut pada data NIM, input yang diberikan secara otomatis mengganti data pada nomor yang dituju
def update():
    os.system('cls')
    print("Update")
    print("======")
    no = input("No: ")

# program akan memerika tiap - tiap baris dari data NIM, dan akan berhenti ketika sudah menemukan data yang benar
    found = False  
# sebagai wadah baru untuk menyimpan data yang telah diperbarui 
    data = []

    with open('data NIM.csv', 'r') as file:
        csv_file = csv.reader(file, delimiter=",")
        for row in csv_file:
            data.append(row)

# menampilkan isi data sebelum dan sesudah diperbarui
    for i, row in enumerate(data):
        if row[0] == no:
            print("Data sebelum update:")
            print("No: ", row[0])
            print("Nim: ", row[1])
            print("No Plat: ", row[2])
            print("Nama: ", row[3])
            print("jenis kendaraan: ", row[4])
            print("Tanggal Jatuh Tempo: ", row[5])                 
            print("=====================")

            new_nim = input("Masukkan NIM baru: ")
            new_no_plat = input("Masukkan No Plat baru: ")
            new_nama = str.upper(input("Masukkan Nama baru: "))
            jenis_kendaraan = (input("Masukkan jenis kendaraan baru: "))
            jatuh_tempo = (input("Masukkan Tanggal Jatuh Tempo baru :"))
        
            data[i] = [no, new_nim, new_no_plat, new_nama, jenis_kendaraan, jatuh_tempo]
            found = True  
            break 
   
    with open('data NIM.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)
    if found:
        print("Data berhasil diupdate")
    else:
        print("Data tidak ditemukan")
        
    pilihan = input("Kembali ke menu admin? (y/n)")
    if pilihan == "y":
        menu_admin()
    else:
        exitkuy()


# mengahapus satu baris data pada nomor urut yang diinput
def delete():
    os.system('cls')
    print("Delete")
    print("======")
    no = input("No: ")

    with open('data NIM.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        data_csv = list(csv_reader)

# program akan memerika tiap - tiap baris dari data NIM, dan akan berhenti ketika sudah menemukan data yang benar
    found = False
# sebagai wadah baru untuk menyimpan data yang telah diperbarui 
    new_data = []

# menampilkan isi dari data yang telah berhasil dihapus
    for row in data_csv:
        if len(row) >= 4 and row[0] == no:  
            found = True
            print("Data berhasil dihapus:")
            print("No: ", row[0])
            print("Nim: ", row[1])
            print("No Plat: ", row[2])
            print("Nama: ", row[3])
        else:
            new_data.append(row)
    if found:
        with open('data NIM.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(new_data)
        print("Data berhasil dihapus")   
    else:
        print("Data tidak ditemukan")

    pilihan = input("Kembali ke menu admin? (y/n)")
    if pilihan == "y":
        menu_admin()
    else:
        exitkuy()
    

# menampilkan daftar admin dengan username dan password yang telah terdaftar    
def daftar_admin():
    os.system('cls')
    print("Daftar Admin")
    print("============")
    with open('user.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',' )
        for row in csv_reader:
            if len(row) >= 3:
             print("Username: " + row[0])
             print("Password: " + row[1])
             print("Role: " + row[2])
             print("\n")
            else:
             pass
    pilihan = input("Kembali ke menu admin? (y/n)")
    if pilihan == "y":
        menu_admin()
    else:
        exitkuy()
    return True


# menambahkan daftar admin baru dengan username dan password
def tambah_admin():
    os.system('cls')
    print("Tambah Admin")
    print("============")
    username = input("Username: ")
    password = input("Password: ")
    role = "admin"

# mengulang pengisian username ketika username sudah digunakan pada daftar admin lain
    with open('user.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        existing_admins = [row[0] for row in csv_reader]
    if username in existing_admins:
        print("Username sudah ada. Gagal menambahkan admin.")
    else:
        with open('user.csv', mode='a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow([username, password, role])
        print("Admin berhasil ditambahkan.")

    pilihan = input("Kembali ke menu admin? (y/n) ")
    if pilihan == "y":
        menu_admin()
    else:
        exitkuy()


# menghapus daftar admin menggunakan username yang sudah terdaftar, otomatis username dan password akan dihapus dari data admin
def hapus_admin():
    os.system('cls')
    print("Hapus Admin")
    print("============")
    username = input("Username: ")
    found = False

    with open('user.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        data_csv = list(csv_reader)
        
    with open('user.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        for row in data_csv:
            if len(row) >= 2 and row[0] == username:
                found = True
                print(f"Data {username} berhasil dihapus")
            else:
                csv_writer.writerow(row)
# username tikan akan dihapus apabila gagal ditemukan 
    if not found:
        print("Data tidak ditemukan")
    pilihan = input("Kembali ke menu admin? (y/n)")
    if pilihan.lower() == "y":
        menu_admin()
    else:
        exitkuy()
    

# fitur mencari data berdasarkan pada beberapa pilihan dan jenis pencarian    
def jenis_cari():
    os.system('cls')
    print("Cari Data")
    print("masukan cari berdasarkan")
    print("1. Nama")
    print("2. NIM")
    print("3. jenis kendaraan")
    print("4. kembali ke menu admin")

    menu = input("Pilih menu> ")
    if menu == "1":
        cari_nama()
    elif menu == "2":
        cari_nim()
    elif menu == "3":
        cari_jenis_ken()
    elif menu == "4":
        menu_admin()
    else:
        print("Menu tidak tersedia")
        

# mencari data pada data NIM berdasarkan nama, dapat menampilkan daftar nama yang mengandung sebuah kata    
def cari_nama():
    os.system('cls')
    print("Cari Data")
    print("============")
    keyword = input("Masukkan keyword untuk pencarian nama: ")
    keyword = keyword.upper()
    with open('data NIM.csv', newline='') as csvfile:
        fieldnames = ['No', 'Nim', 'No Plat', 'Nama', 'Jenis Kendaraan']
        reader = csv.DictReader(csvfile, fieldnames = fieldnames)
        data_found = False  

# menampilkan isi dari data yang dicari dari NIM
        for row in reader:
            if keyword in row['Nama'].upper():
                print("No: " + row['No'])
                print("Nama: " + row['Nama'])
                print("NIM: " + row['Nim'])
                print("No Plat: " + row['No Plat'])
                print("Jenis Kendaraan: " + row['Jenis Kendaraan'])
                print("\n")
                data_found = True
        if not data_found:
            print("Data tidak ditemukan")

    pilihan = input("Kembali ke menu admin? (y/n) ")
    if pilihan == "y":
        menu_admin()
    else:
        exitkuy()


# menampilkan data dari pengguna berdasarkan NIM
def cari_nim():
    os.system('cls')
    print("Cari Data")
    print("============")
    nim = input("Cari berdasarkan NIM: ")

    with open('data NIM.csv', newline='') as csvfile:
        fieldnames = ['No', 'Nim', 'No Plat',"Nama", 'Jenis Kendaraan']
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        nim_found = False

# menampilkan isi dari data yang dicari dari NIM
        for row in reader:
            if row['Nim'] == nim:
                print("No: " + row['No'])
                print("Nama: " + row['Nama'])
                print("NIM: " + row['Nim'])
                print("No Plat: " + row['No Plat'])
                print("Jenis Kendaraan: " + row['Jenis Kendaraan'])
                print("\n")
                nim_found = True
                break
        if not nim_found:
            print("Baris tidak ditemukan")

    pilihan = input("Kembali ke menu admin? (y/n) ")
    if pilihan == "y":
        menu_admin()
    else:
        exitkuy()


# menampilkan seluruh pengguna dalam daftar NIM yang menggunakan suatu kendaraan (motor / mobil)    
def cari_jenis_ken():
    os.system('cls')
    print("Cari Data")
    print("============")
    jenis_ken = input("Cari berdasarkan jenis kendaraan: ")
    with open('data NIM.csv', newline='') as csvfile:
        fieldnames = ['No', 'Nama', 'Nim', 'No Plat', 'Jenis Kendaraan']
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        data_found = False 

# menampilkan isi dari data yang dicari dari NIM
        for row in reader:
            if row['Jenis Kendaraan'] == jenis_ken:
                print("No: " + row['No'])
                print("Nama: " + row['Nama'])
                print("NIM: " + row['Nim'])
                print("No Plat: " + row['No Plat'])
                print("Jenis Kendaraan: " + row['Jenis Kendaraan'])
                print("\n")
                data_found = True

        if not data_found:
            print(f"Tidak ada data dengan jenis kendaraan '{jenis_ken}'")

    pilihan = input("Kembali ke menu admin? (y/n) ")
    if pilihan == "y":
        menu_admin()
    else:
        exitkuy()
        

# menu exit untuk menampilkan pesan bahwa program telah selesai digunakan, dan 
# dapat kembali ke menu awal dengan menekan tombol apa saja
def exitkuy():
    print("Terima kasih telah menggunakan program kami")
    print("==========================================")

    print("Tekan apa saja untuk ke menu awal....")
    input()
    home()
            
        
# tampilan menu awal yang akan memberikan akses fitur berdasarkan role (user / admin), dan
# sistem akan mengulang dalam 1 detik ketika pengguna memilih opsi yang tidak tersedia dalam pilihan
def home():
    os.system('cls')

    print("Welcome to EASYTAX")
    print(" _________________________ ")
    print("|                         |")
    print("|        Welcome          |")
    print("|           to            |")
    print("|        EASYTAX          |")
    print("|_________________________|")
    print("1. Login Admin")
    print("2. User")
    print("3. Keluar")

    menu = input("Pilih menu: ")
    if menu == "1":
        login()
    elif menu == "2":
        loginuser()
    elif menu == "3":
        exitkuy()
    else:
        print("Menu tidak tersedia")
        time.sleep(1)
        return home()
home()
