def cek_usia(usia):
    if usia >= 17:
        return "Kamu sudah cukup umur untuk mengendarai kendaraan bermotor."
    else:
        return "Kamu belum cukup umur untuk mengendarai kendaraan bermotor."
    
usia_pengguna = int(input("Masukkan usia Anda: "))


hasil = cek_usia(usia_pengguna)
print(hasil)
    
