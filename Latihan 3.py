#LATIHAN 3
print("LATIHAN 3")
print("BUBBLE SORT")
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range (n-i-1):
            if arr[j] > arr [j+1]:
                arr [j], arr[j+1] = arr[j+1], arr [j]
    return arr
# data yang akan diurutkan
data = [9, 3, 5, 1]
#panggil fungsi
hasil = bubble_sort(data)
#tampilkan hasil
print ("Data sebelum sorting:", [9, 3, 5, 1])
print("Data setelah sorting:", hasil)