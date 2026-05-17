#NAIVE STRING MATCHING
print("NAIVE STRING MATCHING ")
text = "DATA STRUKTUR DATA"
pattern = "DATA"
for i in range (len(text) - len(pattern) + 1):
    if text [i :i+len(pattern)] == pattern:
        print("ketemu di index", i) 
        
#KMP (KNUT-MORRIS-PRAT) belajar sendiri
