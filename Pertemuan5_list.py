# 1
namakendaraan = ["vixion", "sepedabermotor", "150", "putih", "beroda_dua"]
print("namakendaraan gw")
print(namakendaraan)
print("==========")
# 2
namakendaraan.extend([200, "kopling"])
print(namakendaraan)
# 3
namakendaraan.insert(0, 'yamaha', )
print(namakendaraan)
# buat program python dengan matchcase
luas = input("masukan luas")
match luas:
  case "luas persegi":
      sisi = int(input("masukan nilai persegi"))
      jawab = sisi * sisi
      print(f"luas persegi {jawab}")
  case "luas lingkaran":
      jari = int(input("masukkan jari-jari"))
      jawab = 22/7 * jari ** 2
      print(f"luas lingkaran {jawab}")
  case "luas segitiga":
      a = int(input("masukkan alas"))
      t = int(input("masukkan tinggi"))
      jawab = 1/2 * a * t
      print(f"luas lingkaran {jawab}")
  case _:
    print("salah oi")

