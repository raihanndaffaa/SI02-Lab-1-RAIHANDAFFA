# SOAL 1 - Menghitung rata-rata
# Tuliskan program untuk Soal 1 di bawah ini
print("SOAL 1 - Menghitung rata-rata")
x = eval(input("Masukan bilangan pertama: "))
y = eval(input("Masukan bilangan kedua: "))
z = eval(input("Masukan bilangan ketiga: "))

print("Rata-rata bilangan ", x, ",", y, ",", "dan ", z, "Adalah ",
      (x + y + z) / 3)

# SOAL 2 - Menulis kelipatan bilangan
# Tuliskan program untuk Soal 2 di bawah ini
print("SOAL 2 - Menulis kelipatan bilangan ")
kelipatan = int(
    input("masukan sebuah bilangan bulat yang ingin di cari kelipatannya: "))

# for kelipatan in range(kelipatan, 30, kelipatan) : print (kelipatan ,"", sep="---" ,end="")

"""
print(
    "hasil kelipatan bilangan tersebut : ",
    kelipatan,
    kelipatan + kelipatan,
    kelipatan + kelipatan + kelipatan,
    kelipatan + kelipatan + kelipatan + kelipatan,
    kelipatan + kelipatan + kelipatan + kelipatan + kelipatan,
    sep="---", end=""
    )

"""

print (
  "hasil kelipatan bilangan tersebut : ",
    kelipatan *1 ,
    kelipatan *2 , 
    kelipatan *3 , 
    kelipatan *4 , 
    kelipatan *5 , 
    sep="---", end=""
      )