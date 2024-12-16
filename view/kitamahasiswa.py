from data.mahasiswa import data
class Vmahasiswa:     
    def tampilkan(self):
        if not data:
            print('='*73)
            print("| No |       Nama       |   NIM   | Tugas |  UTS  |  UAS  | Nilai Akhir |")
            print('='*73)
            print("Data masih kosong")
        else:
            print('='*73)
            print("| No |       Nama       |   NIM   | Tugas |  UTS  |  UAS  | Nilai Akhir |")
            print('='*73)
            for idx, (self.nim, datta) in enumerate(data.items(), start=1):
                print(f"| {idx:<3}| {datta['Nama']:<16} | {self.nim:<7} | {datta['Tugas']:<5} | {datta['UTS']:<5} | {datta['UAS']:<5} | {datta['Nilai Akhir']:<11.2f} |")
        

        