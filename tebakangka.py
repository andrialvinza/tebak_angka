import random

def tebak_angka():
    print("Selamat datang di permainan Tebak Angka!")
    print("Saya sudah memilih angka antara 1 dan 100. Coba tebak angka tersebut!")

    angka_rahasia = random.randint(1, 100)
    tebakan = None
    percobaan = 0

    while tebakan != angka_rahasia:
        tebakan = int(input("Masukkan tebakanmu: "))
        percobaan += 1
        
        if tebakan < angka_rahasia:
            print("Tebakanmu terlalu kecil. Coba lagi!")
        elif tebakan > angka_rahasia:
            print("Tebakanmu terlalu besar. Coba lagi!")
        else:
            print(f"Selamat! Tebakanmu benar. Kamu berhasil dalam {percobaan} percobaan.")
            break

# Menjalankan permainan
tebak_angka()
