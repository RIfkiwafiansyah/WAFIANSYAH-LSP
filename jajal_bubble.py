def garis() :
    print("=======================================")

def ascending(mylist):
    mylist = sorted(mylist)
    print(mylist)

def descending(mylist):
    mylist = sorted(mylist, reverse = True)
    print(mylist)

print ("Masukan tiga buah nilai")

nilaiA = int(input("Masukan nilai A : "))
nilaiB = int(input("Masukan nilai B : "))
nilaiC = int(input("Masukan nilai C : "))
angka = [nilaiA, nilaiB, nilaiC]
garis()

#fungis rata-rata
def rata_rata(angka):
    return sum(angka)/len(angka)

print("""urutan hasil escending : """,(ascending(angka)))

print("""urutan hasil descending : """,(descending(angka)))

print("Angka Terbesar : ",max(angka))

print("Angka Terbesar : ",min(angka))

print("Rata - rata nilai : ",rata_rata(angka))
