buah = ["apel", "jeruk", "mangga"]

print("List awal:", buah)

buah.append("pisang")
print("Setelah append:", buah)

buah.insert(1, "anggur")
print("Setelah insert:", buah)

buah[0] = "semangka"
print("Setelah mengubah elemen:", buah)

buah.remove("jeruk")
print("Setelah remove:", buah)

buah.pop()
print("Setelah pop:", buah)
