def hitung_bmr(jenis_kelamin, berat, tinggi, umur):
    if jenis_kelamin.lower() == 'pria':
        bmr = 66 + (13.7 * berat) + (5 * tinggi) - (6.8 * umur)
    else:
        bmr = 655 + (9.6 * berat) + (1.8 * tinggi) - (4.7 * umur)
    return bmr

while True:
    jenis_kelamin = input("Masukkan jenis kelamin Anda (Pria/Wanita): ")
    if jenis_kelamin.lower() not in ['pria', 'wanita']:
        print("Input tidak ditemukan. Silakan masukkan 'Pria' atau 'Wanita'.")
        continue
    berat = float(input("Masukkan berat badan Anda dalam kg: "))
    tinggi = float(input("Masukkan tinggi badan Anda dalam cm: "))
    umur = int(input("Masukkan umur Anda dalam tahun: "))

    bmr = hitung_bmr(jenis_kelamin, berat, tinggi, umur)
    print("BMR Anda adalah: ", bmr)

    ulangi = input("Apakah Anda ingin menghitung BMR lagi? (Ya/Tidak): ")
    if ulangi.lower() != 'ya':
        break