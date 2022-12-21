# P2_Komnum_B2
**Repository Praktikum 2 Komputasi Numerik ( B ) - Kelompok 2**

## **Anggota Kelompok**
| Nama                     | NRP        | Kelas    |
| -------------------------| -----------| ---------|
| Alfan Lukeyan Rizki      | 5025211046 | Komnum B |
| Akmal Ariq Romadhon      | 5025211188 | Komnum B |
| Muhammad Rifqi Fadhillah | 5025211228 | Komnum B |

## **Soal Praktikum**
Salah satu kelemahan dari metode Trapezoidal adalah kita harus menggunakan jumlah interval yang besar untuk memperoleh akurasi yang diharapkan. Buatlah sebuah program komputer untuk menjelaskan bagaimana metode Integrasi Romberg dapat mengatasi kelemahan tersebut.
	

## **Penjelasan**
Integrasi Romberg merupakan kombinasi dari _Trapezoidal Rule_ dengan _Richardson Extrapolation_. Dalam penggunaannya, Integrasi Romberg dinilai lebih efektif serta lebih cepat dibandingkan metode lain seperti Metode Simpson. Selain itu Metode Romberg juga dinilai lebih akurat dibading metode lain. <br>  

Dalam pembuatan program Interasi Romberg, dapat digunakan beberapa pilihan. Yang pertama ialah penggunaan _module Integrate_ dari _library spicy_ yang diimport kedalam bahasa _Python_. Untuk menggunakan _module_ tersebut, diperlukan **fungsi, batas bawah, dan batas atas** sebagai parameternya. Berikut adalah contoh penggunaan _module Integrate_ dari _library spicy_ untuk perhitungan Integrasi Romberg. <Br>
```py
import numpy as np
from scipy import integrate

#function = 1/(1+2+x)
#batas bawah = 0
#batas atas = 2

def func(x) :
    return 1/(1+2+x)
calc = integrate.romberg(func, 0, 2, show = True)
print(calc)
```
Selain menggunakan bahasa _python_, dapat digunakan juga bahasa _R_ dalam menghitung Integrasi Romberg. Untuk dapat melakukan perhitungan dengan bahasa _R_ diperlukan _package_ atau _library pracma_. Sama seperti _Spicy_, dalam menghitung Integrasi Romberg diperlukan **fungsi, batas bawah, dan batas atas**. Berikut adalah contoh perhitungan Integrasi Romberg dengan bahasa _R_. <bt>
```R
install.packages("pracma")
library(pracma)

#function = 1/(1+2+x)
#batas bawah = 0
#batas atas = 2

f <- function(x) 1/(1+2+x)
romberg(f, 0, 2)
```
## **_Screeshot Running_ Program**
Menggunakan bahasa _R_ dan RStudio.

![R](https://user-images.githubusercontent.com/109916703/208948689-052eb94b-9ab8-44ad-a099-60b25b310c1a.png)

Menggunakan bahasa _Python_.

![Py](https://user-images.githubusercontent.com/109916703/208949194-ccc8d8a8-9f95-4db8-aaed-070b92d1b820.png)

Menggunakan _calculator online_.

![Py](https://user-images.githubusercontent.com/109916703/208949521-a33847a8-94ac-4f59-a77d-0189d9357078.png)

## **End Of The Line**
```c
#include <stdio.h>

int main(){
    printf("Thank you!");
}
```
