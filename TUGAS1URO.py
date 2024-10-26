def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y != 0:
        return x / y
    else:
        return "Tidak bisa dibagi dengan nol"

print("Pilih operasi:")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")

while True:
    operasi = input("Masukkan pilihan operasi (1/2/3/4) atau 'exit' untuk keluar: ")

    if operasi == 'exit':
        print("Kalkulator berhenti. Terima kasih!")
        break

    if operasi in ('1', '2', '3', '4'):
        try:
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))

            if operasi == '1':
                print(f"Hasil: {tambah(angka1, angka2)}")
            elif operasi == '2':
                print(f"Hasil: {kurang(angka1, angka2)}")
            elif operasi == '3':
                print(f"Hasil: {kali(angka1, angka2)}")
            elif operasi == '4':
                print(f"Hasil: {bagi(angka1, angka2)}")

        except ValueError:
            print("Input tidak valid. Masukkan angka yang benar.")
    else:
        print("Pilihan operasi tidak valid.")
