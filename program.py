# Login Sederhana

print('''
SELAMAT DATANG DI PROGRAM MENGHITUNG
     RUMUS SEGITIGA PYTHAGORAS
''')

print("Silahkan Masukkan Data Diri Anda")

nama  = input("Masukkan Username : ")

while True :
    nim = input ("Masukkan NIM      : ")
    if nim.isdigit():
        break
    else:
        print("NIM harus berupa angka, silahkan coba lagi")

password = input("Masukkan Password : ")

print()
print(20*"=")
print("       LOGIN")
print(20*"=")

print()
print(f"Username  : {nama}")
print(f"NIM       : {nim}")
print(f"Password  : {password}")
print()
print("Anda Berhasil Login")
print()


# Perhitungan Rumus Pythagoras

while True:
# Menampilkan Menu Pilihan

    print("Rumus Pythagoras")
    print("1. Alas")
    print("2. Sisi Tegak")
    print("3. Sisi Miring")
    print("4. Keluar")

    # Mengambil pilihan dari pengguna
    pilihan = int(input("Masukkan pilihan (1-4): "))

    # Alas
    if pilihan == 1:
        sisi_miring = float(input("Masukkan sisi miring: "))
        sisi_tegak = float(input("Masukkan sisi tegak: "))
        rumus_alas = (sisi_miring*2 - sisi_tegak*2)**0.5
        print(f"Hasil alas adalah: {rumus_alas}")
    # Sisi Tegak
    if pilihan == 2:
        sisi_miring = float(input("Masukkan sisi miring: "))
        sisi_alas = float(input("Masukkan sisi alas: "))
        rumus_tegak = (sisi_miring*2 - sisi_alas*2)**0.5
        print(f"Hasil sisi tegak adalah: {rumus_tegak}")
    # Sisi Miring
    if pilihan == 3:
        sisi_tegak = float(input("Masukkan sisi tegak: "))
        sisi_alas = float(input("Masukkan sisi alas: "))
        rumus_miring = (sisi_tegak*2 + sisi_alas*2)**0.
        print(f"Hasil sisi miring adalah: {rumus_miring}")
    # Blok ini menangani pilihan Keluar
    if pilihan == 4:
            print("Keluar dari program")
            break
