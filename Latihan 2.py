#LATIHAN 2
print("LATIHAN 2")
def binary_search(arr, target):
    left = 0                #batas kiri
    right = len(arr) -1     #batas kana
    #selama batas kiri dan kanan belum bersilang
    while left <= right:
        #cari indeks tengah
        mid = (left + right) // 2
        if arr [mid] == target:
            return mid 
        elif target < arr [mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1
data = [2, 4, 6, 8, 10]
angka_dicari = 8   #target
hasil = binary_search(data, angka_dicari)
if hasil != -1:
    print("angka ", angka_dicari, "ada di indeks ke-", hasil)
else:
    print("angka tidak ditemukan")