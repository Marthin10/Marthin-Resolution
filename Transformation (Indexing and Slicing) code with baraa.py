# Transformation : Data extration (Indexing and slicing)

word = "Hello"

# print huruf yang akan diprint dari kata "Hello" index 0 hasil = H
print(word[0])
# print huruf yang akan diprint dari kata "Hello" index 1 hasil = e
print(word[1])
# print huruf yang akan diprint dari kata "Hello" index 2 hasil = l
print(word[2])
# print huruf yang akan diprint dari kata "Hello" index 3 hasil = l
print(word[3])
# print huruf yang akan diprint dari kata "Hello" index 4 hasil = o
print(word[4])
# print huruf yang akan diprint dari kata "Hello" index 4 hasil akan error
print(word[5])
# print huruf yang akan diprint dari kata "Hello" index -1 hasil = o
print(word[-1])
# print huruf yang akan diprint dari kata "Hello" index -2 hasil = l
print(word[-2])
# print huruf yang akan diprint dari kata "Hello" index -3 hasil = l
print(word[-3])
# print huruf yang akan diprint dari kata "Hello" index -4 hasil = e
print(word[-2])
# print huruf yang akan diprint dari kata "Hello" index -5 hasil = H
print(word[-5])
# print huruf yang akan diprint dari kata "Hello" index -6 hasil = error
print(word[-6])
# Kesimpulan : Jika dari depan index mulai dari 0 dan jika dari belakang index mulai dari -1 dan jika index di luar jumlah huruf -1(jika dari depan atau belakang) akan terjadi error
# Indexes minus digunakan ketika ingin mengambil objek yang lebih dekat dari belakang dan positif jika lebih dekat dari depan
