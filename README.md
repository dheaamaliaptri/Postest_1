# Postest_1_A
Nama : Dhea Amalia Putri

NIM : 2309116037

Kelas : Sistem Informasi A'23

# PROGRAM MENGHITUNG RUMUS SEGITIGA PYTHAGORAS

# Flowchart

   ![postest 1 flowchart drawio](https://github.com/dheaamaliaptri/Postest_1/assets/144705099/8f18e4c1-31fe-4545-a1e1-f4140b0c6a3a)
   ![postest 1 flowchart2 drawio](https://github.com/dheaamaliaptri/Postest_1/assets/144705099/3b964218-8dee-4b9d-a386-511c0f3924c5)

# Penjelasan Output

   Program python yang saya buat ini terdapat Login Sederhana dan juga memungkinkan user untuk menghitung panjang sisi segitiga siku-siku, dengan menggunakan panjang dua sisi lainnya. Program ini menerapkan rumus teorema pythagoras untuk melakukan perhitungan.

Pada program ini saya juga menggunakan perulangan while pada Input NIM dan Input saat memilih menu pilihan rumus

# 1. Login Sederhana

   Pertama-tama, pengguna harus memasukkan data diri terlebih dahulu melalui input. Program ini menggunakan loop while pada bagian NIM pengguna, loop ini akan terus berjalan sampai pengguna memasukkan NIM yang valid (hanya angka). Disini saya menggunakan .isdigit() yang berguna untuk memeriksa apakah sebuah string hanya memiliki angka atau tidak, jika pada string itu hanya mengandung angka maka akan bernilai True dan jika memiliki setidaknya satu saja karakter yang bukan merupakan angka maka nilai yang akan dihasilkan adalah False. Lalu mencetak pesan 'Anda telah berhasil login'

   <img width="248" alt="Screenshot 2023-09-26 025350_2" src="https://github.com/dheaamaliaptri/Postest_1/assets/144705099/206a4622-669d-4faf-a464-fd4c458a5790">

# 2. Perhitungan Rumus Pythagoras

   Program ini juga menggunakan loop while True untuk menampilkan menu pilihan (alas, sisi tegak, sisi miring, atau keluar) kepada pengguna

Tergantung pilihan dari pengguna, progrm akan meminta pengguna menginputkan panjang sisi-sisi yang ingin diketahui

1. Mencari sisi alas segitiga ((sisi miring² - sisi tegak²) x 0.5)

   <img width="224" alt="Screenshot 2023-09-26 025350_alas" src="https://github.com/dheaamaliaptri/Postest_1/assets/144705099/2063fb98-aa54-4cb1-9d77-0a6ee5371cfa">

2. Mencari sisi tegak segitiga ((sisi miring² - sisi alas²) x 0.5)

   <img width="204" alt="Screenshot 2023-09-26 044223" src="https://github.com/dheaamaliaptri/Postest_1/assets/144705099/d95067bd-c4d7-4bb3-bba6-ebe572ecfd0c">


3. Mencari sisi Miring ((sisi alas² - sisi tegak²) x 0.5)

   <img width="201" alt="Screenshot 2023-09-26 044237" src="https://github.com/dheaamaliaptri/Postest_1/assets/144705099/6ffbaab5-90ba-4e95-9890-7a4bd84c2e84">

4. Keluar dari program

   <img width="168" alt="Screenshot 2023-09-26 044247" src="https://github.com/dheaamaliaptri/Postest_1/assets/144705099/c8003080-3c38-43e6-80d9-efad1e5d255c">
