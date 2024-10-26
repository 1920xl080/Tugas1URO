```
Definisikan fungsi `tambah(x, y)`:
    - Terima dua angka, `x` dan `y`.
    - Kembalikan hasil `x + y`.

Definisikan fungsi `kurang(x, y)`:
    - Terima dua angka, `x` dan `y`.
    - Kembalikan hasil `x - y`.

Definisikan fungsi `kali(x, y)`:
    - Terima dua angka, `x` dan `y`.
    - Kembalikan hasil `x * y`.

Definisikan fungsi `bagi(x, y)`:
    - Terima dua angka, `x` dan `y`.
    - Jika `y ≠ 0`, kembalikan hasil `x / y`.
    - Jika `y = 0`, kembalikan pesan "Tidak bisa dibagi dengan nol".

Tampilkan pilihan operasi yang tersedia:
    - "1. Tambah"
    - "2. Kurang"
    - "3. Kali"
    - "4. Bagi"

Masuk ke dalam loop dan meminta input pengguna:
    - Minta pengguna memasukkan pilihan operasi (1, 2, 3, 4, atau 'exit' untuk keluar).
    
Periksa pilihan operasi:
    - Jika `pilihan == 'exit'`:
        - Tampilkan pesan "Kalkulator berhenti. Terima kasih!" dan keluar dari loop.
    - Jika `pilihan` ada dalam ('1', '2', '3', '4'):
        - Minta pengguna memasukkan `angka1` dan `angka2`.
        - Periksa apakah input valid:
            - Jika input tidak valid, tampilkan pesan "Input tidak valid. Masukkan angka yang benar."
            - Jika valid, lakukan operasi sesuai pilihan:
                - Pilihan `1`: Tambah kedua angka.
                - Pilihan `2`: Kurangi `angka1` dengan `angka2`.
                - Pilihan `3`: Kali kedua angka.
                - Pilihan `4`: Bagi `angka1` dengan `angka2` (cek `angka2 ≠ 0`).
        - Tampilkan hasil operasi.
    - Jika pilihan tidak valid, tampilkan pesan "Pilihan operasi tidak valid."

Kembali ke langkah 2 hingga pengguna memilih 'exit'.
Selesai.



