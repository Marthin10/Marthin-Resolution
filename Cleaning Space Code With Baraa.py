# cleaning space at the right, left and both side using method strip
text = "   Engineering   "

print(text)
# Clean both side
print(text.strip())
# Clean right side
print(text.rstrip())
# Clean left side
print(text.lstrip())
# Jika mau clean aspek lain (jadi harus diclean dlu object sebelum dia)
print(text.strip().strip("E"))
# Jika mau clean aspek lain (jadi harus diclean dlu object sesudah dia (kalau objectnya sebelah kiri))
print(text.strip().strip("g"))
