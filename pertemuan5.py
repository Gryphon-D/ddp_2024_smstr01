# tugas1
bilangan = int(input("masukan angka :"))
hasil = bilangan % 2
if hasil == 0 :
  print(f"angka {bilangan} merupakan genap")
elif hasil == 1 :
  print(f"angka {bilangan} merupakan ganjil")
else : 
  print("jangan masukin desimal panjul") 

# tugas2
nilai = int(input("masukan nilai"))
if nilai >= 75 :
  print(f"kamu lulus")
elif nilai <= 75 :
  print(f"kamu tidak lulus") 

# tugas3
nilai = int(input("masukan umur"))
if nilai >= 18 :
  print(f"kamu tua")
elif 13 <= nilai <= 18  :
  print(f"kamu remaja")
else :
  print(f"kamu bocil")

# tugas4
nilai = int(input("masukan nominal"))
if nilai >= 100000000:
  print(f"selamat kamu gold")
elif 20000000<= nilai <= 100000000:
  print(f"kamu silver")
else :
  print(f"kamu bronze")

# tugas5
bon = int(input("Masukkan jumlah pembelian: "))
total = bon * 0.9 if bon >= 100 else bon
print(f"Total harga setelah diskon: {total}" if bon > 100 else f"Total harga tanpa diskon:{bon}")