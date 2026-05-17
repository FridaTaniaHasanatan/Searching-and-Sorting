print("STUDI KASUS 2")
def bubble_sort(arr) :
    n = len(arr)
    for i in range(n):
        for j in range (n-i-1):
            if arr[j] > arr [j+1]:
                arr [j], arr[j+1] = arr[j+1], arr [j]
    return arr
# data yang akan diurutkan
data = [60, 80, 75, 90, 85, 70]
#panggil fungsi
hasil = bubble_sort(data)
#tampilkan hasil
print ("Data sebelum sorting:", [60, 80, 75, 90, 85, 70])
print("Data setelah sorting:", hasil)