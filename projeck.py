import numpy as np
import matplotlib.pyplot as plt

x1 = int(input("Masukkan Nilai X1 = "))
y1 = int(input("Masukkan Nilai y1 = "))
x2 = int(input("Masukkan Nilai X2 = "))
y2 = int(input("Masukkan Nilai y2 = "))

m = (y2-y1)/(x2-x1)
N = x2-x1+1
x = x1

if x1 == x2:
    print("Garis vertical")
# ini di kerja
elif y1 == y2:
    y = y1 = y2
    titikx = []
    titikya = []
    print("Garis vertical")
    print("-----------------------------")

    while x <= x2:
        print("Garis Yang dilewati adalah (", x, ",", y, ")")
        titikx.append(x)
        titikya.append(y)
        x = x+1

    plt.plot(titikx, titikya)
    plt.show()


else:
    titikx = []
    titikya = []
    print("Nilai kemiringannya adalah m = ", m)
    print("Nilai N adalah N = ", N)
    print("Nilai X adalah x = ", x)
    print("____________________________")

    i = 0
    while i < N:
        x = x1 + i
        j = 0
        while j <= i:
            y = m*(x-x1)+y1
            ya = round(y)
            j = j+1
        print("Nilai x nya adalah = ", x)
        print("nilai Y adalah = ", y)
        print("nilai Ya adalah = ", ya)
        print("Garis yang dilewati adalah (", x, ",", ya, ")")
        print("-----------------------------")
        titikx.append(x)
        titikya.append(ya)
        i = i+1
    plt.plot(titikx, titikya)
    plt.show()
