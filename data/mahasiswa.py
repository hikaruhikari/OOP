data = {}
class Mahasiswa:
    def __init__(self, nama, nim, tugas, uts, uas):
        self.nama = nama
        self.nim = nim
        self.tugas = tugas
        self.uts = uts
        self.uas = uas
        self.nilai_akhir = None
        
    def tambah(self):
        ra = self.tugas *30/100
        rb = self.uts *35/100
        rc = self.uas *35/100
        nilai_akhir = ra + rb + rc
        data[self.nim] = {
            "Nama": self.nama, 
            "NIM": self.nim, 
            "Tugas": self.tugas, 
            "UTS": self.uts, 
            "UAS": self.uas, 
            "Nilai Akhir": nilai_akhir
        }
        print("Data berhasil ditambahkan")
        
    def ubah(self):
        ra = self.tugas *30/100
        rb = self.uts *35/100
        rc = self.uas *35/100
        nilai_akhir = ra + rb + rc
        data[self.nim] = {
            "Nama": self.nama, 
            "NIM": self.nim, 
            "Tugas": self.tugas, 
            "UTS": self.uts, 
            "UAS": self.uas, 
            "Nilai Akhir": nilai_akhir
        }

    def hapus(self, nim):
        if nim in data:
            del data[nim]
            print("Data berhasil dihapus")
        else:
            print("Data tidak ditemukan")
    
    def cari(self, nim):
        if nim in data:
            print("Data ditemukan!")
            print('=' * 73)
            print("| No |       Nama       |   NIM   | Tugas |  UTS  |  UAS  | Nilai Akhir |")
            print('=' * 73)
            dat = data[nim]
            print(f"| {dat['Nama']:<16} | {self.nim:<7} | {dat['Tugas']:<5} | {dat['UTS']:<5} | {dat['UAS']:<5} | {dat['Nilai Akhir']:<11.2f} |")
            print('=' * 73)
        else:
            print("NIM tidak ditemukan")
            
