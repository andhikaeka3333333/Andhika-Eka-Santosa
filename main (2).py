import math
from random import randint
import random



def Transformasi():
  f = "====================================================="
  print("Selamat datang dalam Transformasi Kalkulator")
  print(f)
  print("By Dhika")
  print(f)
  print("1.Refleksi")
  print("2.Translasi")
  print(f)
  Tanyaaa = input("Masukkan Jenis Transformasi  ")
  if Tanyaaa == "1":
    x = int(input("Berapa X nya "))
    y = int(input("Berapa Y nya "))
    print(f)
    print("1.Sumbu X")
    print("2.Sumbu Y")
    print("3.Daerah Asal (0,0)")
    print("4.Garis y = x")    
    print("5.Garis y = -x")
    print("6.Garis x = h")
    print("7.Garis y = h ")
    print(f)
    jenisRfl = input("Titik di refleksi terhadap apa?  ")
    k = ","
    if jenisRfl  == "1":
      SbX = x , -1 * y
      print(SbX)
    elif jenisRfl == "2":
      SbY = -1 * x  , y
      print(SbY)
    elif jenisRfl  == "3":
      DA = -1 * x  , -1 * y
      print(DA)
    elif jenisRfl == "4":
      print(f'{y} , {x}')
    elif jenisRfl == "5":
      yx = -1 * y , -1 * x
      print(yx)
    elif jenisRfl == "6":
      h = int(input("Berapa Nilai h nya "))
      xh = 2 * h - x  , y
      print(xh)
    elif jenisRfl == "7":
      hh = int(input("Berapa h nya ? "))
      yh = x  , 2 * hh - y
      print(yh)
    else:
      print("ya")
  Back()
    
      
      
  
  


def MainG():
  print("Pilih Permainan ")
  print("1.Balok Game")
  print("2.Game Perkalian")
  gameQ = input("Silahkan Pilih Angka  ")
  if gameQ == "1":
    panjangR = randint(0, 33)
    lebarR = randint(0, 21)
    tinggiR = randint(0, 17)
    volumeR = panjangR * lebarR * tinggiR
    print(f'Panjang = {panjangR}')
    print(f'Lebar : {lebarR}')
    print(f'Tinggi = {tinggiR}')
    QuestioNGame = int(input("Berapa Volumenya "))
    if QuestioNGame == volumeR:
      print("JawabanMu Benar")
    else:
      print("Jawabanmu Salah")

  elif gameQ == "2":

    berapa = int(input("Mau Berapa soal ?  "))
    for i in range(berapa):
      angKa1 = randint(0 , 29)
      angKa2 = randint(0 , 29)
      print("==========================================================")
      print(f'Angka 1 = {angKa1}')
      print(f'Angka 2 = {angKa2}')
      hsil = angKa1 * angKa2
      Jawabanmuu = int(input("Berapa Hailnya ?  "))
      if Jawabanmuu == hsil:
        print("Jawabanmu Benar")
      else:
        print("Jawabanmu salah")
      
    
  

def PersmKuadrat():
  print('##  Persamaan Kuadrat CalcuLator  ##')
  print('=====================================================')
  print("Create by Dhika")
  print('=====================================================')
  print()
  print('Format persamaan: ax^2 + bx + c = 0')

  a = int(input('Input nilai a: '))
  b = int(input('Input nilai b: '))
  c = int(input('Input nilai c: '))
  print()
  D = (b * b) - (4 * a * c)
  print('Diskriminan =', D, end='')
  if (D > 0):
    print(' (akar real dan berbeda)')
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print('x1 =', round(x1, 2))
    print('x2 =', round(x2, 2))
  elif (D == 0):
    print(' (akar real dan sama)')
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = x1

    print('x1 = ', round(x1, 2))
    print('x2 = ', round(x2, 2))
  else:
    print(' (akar tidak real / imajiner)')
  Back()

def HukumColoumb():
  print("Coloumb Calculator")
  print("====================================================================")
  print("By Dhika")
  print("====================================================================")
  k = 9 * 10**9
  muatan1 = int(input("Masukkan Q1  "))
  muatan2 = int(input("Masukkan Q2 " ))
  print("====================================================================")
  print("Masukkan huruf M jika satuan dalam bentuk microcoloumb dan masukkan huruf C jika satuan nya Coloumb")
  Tanya = input("Muatannya Dalam satuan apa (μC / C)   ")
  print("=====================================================================")
  print("Masukkan M jika meter , Masukkan CM jika satuannya CentiMeter")
  TanyaJ = input("Jaraknya Dalam Satuan (CM / M)  ")
  jarak = int(input("Masukkan Jarak dari Kedua Muatan "))

  if TanyaJ == "CM":
    print("Jawabannya Adalah")
    jarakBaru = jarak * 10**-2
    if Tanya == "M":
      microD = muatan1* 10**-6
      microDK = muatan2* 10**-6
      hasilOK = k * microD * microDK / jarakBaru**2
      print(hasilOK)

    elif Tanya == "m":
      microO = muatan1* 10**-6
      microB = muatan2* 10**-6
      Micero = k * microO * microB / jarakBaru**2
      print(Micero)

    elif Tanya == "C":
      Banyak = k * muatan1 * muatan2 / jarakBaru**2
      print(Banyak)

    elif Tanya == "c":
      Yes = k * muatan1 * muatan2 / jarakBaru**2
      print(Yes)

  elif TanyaJ == "M":
    print("Jawabannya Adalah")
    if Tanya == "M":
      micro1 = muatan1* 10**-6
      micro2 = muatan2* 10**-6
      hasilM1 = k * micro1 * micro2 / jarak**2
      print(hasilM1)

    elif Tanya == "m":
      micro3 = muatan1* 10**-6
      micro4 = muatan2* 10**-6
      hasilM = k * micro3 * micro4 / jarak**2
      print(hasilM)

    elif Tanya == "C":
      hasilC1 = k * muatan1 * muatan2 / jarak**2
      print(hasilC1)

    elif Tanya == "c":
      hasilC = k * muatan1 * muatan2 / jarak**2
      print(hasilC)

  else:
    print("ERORRR!!")
  Back()


def Kalkulator():
  ds = input("Jenis perhitungan apa yang kamu inginkan? ")
  if ds == "perkalian":
    angka1 = int(input("Masukkan Angka 1 "))
    angka2 = int(input("Masukkan angka 2 "))
    hpr = angka2 * angka1 
    print(f'Hasilnya adalah {hpr}.' )
  elif ds == "penjumlahan":
    angkay = int(input("Masukkan Angka 1 "))
    angkay2 = int(input("Masukkan angka 2 "))
    hpj = angkay + angkay 
    print(f'Hasilnya adalah {hpj}.' )
  elif ds == "pembagian":
    angkabagi1 = int(input("Masukkan Angka 1 "))
    angkabagi2 = int(input("Masukkan angka 2 "))
    hpb = angkabagi1 / angkabagi2
    print(f'Hasilnya adalah {hpb}.' )
  else:
    kurng = int(input("Masukkan Angka 1 "))
    kur = int(input("Masukkan Angka 2 "))
    kalai = kurng - kur
    print(f'Hasilnya adalah {kalai}.' )
  Back()
def bangunRuang():
  print("3D Kalkulator ")
  print("=====================================================================")
  print("By Dhika")
  print("===================================================================")
  print("Silahkan Pilih ")
  print("1.Kubus")
  print("2.Balok")
  print("===================================================================")
  VolumeQ = input("Jenis Bangun Ruang Apa yang Ingin Kamu hitung ")
  if VolumeQ == "1":
    sKubus1 = input("Sisi Kubus ")
    Pangkat = sKubus1 * sKubus1 * sKubus1
    print(f'Hasilnya Adalah {Pangkat} ')
  elif VolumeQ == "2":
    p = input("Berapa Panjang ")
    l = input("Berapa Lebar ")
    t = input("Berapa Tinggi  ")
    w = p * l * t
    Balok = print(f'Hasilnya Adalah {w}')
  else:
    print(7)
  Back()
  
  
def Admin():
  passw = input("Masukkan Password")
  if passw == "DhikaPython1":
    print("Nomor WhatsApp 085656596197")
    print("Nama Admin : Andhika Eka Santosa")
  else:
    print("Maaf Password Tidak Sesuai , Silahkan Meminta kepada Admin")
    print("===================================================================")
    bacK = input("Apakah ingin kembali ke menu awal? (YA / TIDAK)")
  Back()
    
def Menu():
  namee = input("Siapa namamu? ")
  print(f'Halo {namee} selamat datang di aplikasi Math Solver by Dhika')
  print("Selamat Datang di Math Solver")
  print("======================================================================")
  print("By Dhika")
  print("=======================================================================")

  print("1. PersamaanKuadrat ")
  print("2. Hukum Coloumb")
  print("3. Kalkulator")
  print("4. Bangun Ruang")
  print("5. Informasi Admin")
  print("6. Math Quiz")
  print("7. Transformasi")
  print("========================================================================")

  Option1 = input("Silahkan Pilih    ")

  if Option1 == "1": 
    PersmKuadrat()
  elif Option1 == "2":
    HukumColoumb()
  elif Option1 == "3":
    Kalkulator()
  elif Option1 == "4":
    bangunRuang()
  elif Option1 == "5":
    Admin()
  elif Option1 == "6":
    MainG()
  elif Option1 == "7":
    Transformasi()
    
    
  else:
    print("Error")






  
def Back():
  print("=================================================================")
  print("1.Kembali ke menu utama")
  print("2.Tetap disini")
  back = input("Silahkan Pilih  ")
  if back == "1":
    print("=================================================================")
    Menu()
  elif back == "2":
    print("Terima Kasih")
    print("=================================================================")
  else:
    print(".")
    
Menu()