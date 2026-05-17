print("STUDI KASUS 3")
print("NAIVE STRING MATCHING")
# Dokumen / text
text = "tan imup adalah seorang mahasiswa yang rajin belajar algoritma dan struktur data"
print(text)
# Kata yang dicari
pattern = "tan imup"
print("kata yg dicari:", pattern)
# Proses pencarian
for i in range(len(text) - len(pattern) + 1):
    # Membandingkan substring dengan pattern
    if text[i : i + len(pattern)] == pattern:
        # Menampilkan posisi kata ditemukan
        print("Kata ditemukan di index", i)
