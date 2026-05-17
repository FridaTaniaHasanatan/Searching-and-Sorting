#STUDI KASUS
print("STUDI KASUS 1")
def linear_search(arr, target):
    for i in range (len(arr)):
        if arr[i] == target:
            return i
    return -1
data= [12,7,25,9,15]
angka_dicari = 25 #target
hasil = linear_search(data, angka_dicari)
print(data)
if hasil !=-1:
    print("angka", angka_dicari, " ada di indeks ke -", hasil)
else:
    print("angka tidak ditemukan")
