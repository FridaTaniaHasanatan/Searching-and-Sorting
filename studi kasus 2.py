print("STUDI KASUS 2")
def bubble_sort(arr) :
    n = len(arr)
    for i in range(n):
        for j in range (n-i-1):
            if arr[j] > arr [j+1]:
                arr [j], arr[j+1] = arr[j+1], arr [j]
    return arr
# data yang akan diurutkan
data = [2,3,1,5,4]
#panggil fungsi
hasil = bubble_sort(data)
#tampilkan hasil
print ("Data sebelum sorting:", [2,3,1,5,4])
print("Data setelah sorting:", hasil)
