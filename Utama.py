from view.input_form import masuk
from view.kitamahasiswa import Vmahasiswa
class main:    
    def __init__(self):
        c = masuk()
        b = Vmahasiswa()
        while True:
            print("\n1. lihat data\n2. tambah data\n3. Ubah data\n4. Hapus data\n5. Cari data\n6. keluar")
            pilihan = input("Masukkan pilihan (1-6): ")
            if pilihan == '1':
                b.tampilkan()
            elif pilihan == '2':
                c.tambah()
            elif pilihan == '3':
                c.ubah()
            elif pilihan == '4':
                c.hapus()
            elif pilihan == '5':
                c.cari()
            elif pilihan == '6':
                print("terima kasih")
                exit()
            else:
                print("data tidak valid. Masukkan angka lagi")
                
main()