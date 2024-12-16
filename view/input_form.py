from data.mahasiswa import data, Mahasiswa
class masuk():     
    def tambah(self):
        nama = input("Nama: ")
        nim = input('NIM: ')
        tugas = int(input('Nilai Tugas: '))
        uts = int(input('Nilai UTS: '))
        uas = int(input('NIlai UAS: '))

        mhs = Mahasiswa(nama, nim, tugas, uts, uas)
        mhs.tambah()

        
    
    def ubah(self):
        nim = input("masukkan nim yang akan diubah: ")
        if nim in data:
            nama = input("Nama: ")
            nim = input('NIM: ')
            tugas = int(input('Nilai Tugas: '))
            uts = int(input('Nilai UTS: '))
            uas = int(input('NIlai UAS: '))
            mhs = Mahasiswa(nama, nim, tugas, uts, uas)
            mhs.ubah()
        else:
            print("NIM tidak ditemukan")

        

    def hapus(self):
        nim = input("Masukkan nim yang ingin dihapus: ")
        mhs = Mahasiswa(nim, "d", "c", "b", "a")
        mhs.hapus(nim)


    def cari(self):
        nim = input("Masukkan NIM yang dicari: ")
        mhs = Mahasiswa(nim, "d", "c", "b", "a")
        mhs.cari(nim)

      
    