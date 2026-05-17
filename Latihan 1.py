#LATIHAN 1
print("LATIHAN 1")
def linear_search(arr, target):
    for i in range (len(arr)):
        if arr[i] == target:
            return i
    return -1
data= [4, 7, 1, 9]
angka_dicari = 9 #target
hasil = linear_search(data, angka_dicari)
if hasil !=-1:
    print("angka", angka_dicari, "ada di indeks ke:", hasil)
else:
    print("angka tidak ditemukan")
