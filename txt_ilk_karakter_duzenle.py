import os

# Klasör yolunu belirtin
folder_path = r"C:\Users\HP\Desktop\ranger\labels\val"

# Klasördeki tüm dosyaları döngüyle gezin
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        # Dosya yolu
        file_path = os.path.join(folder_path, filename)

        # Dosyayı açın ve satırları döngüyle gezin
        with open(file_path, "r+") as f:
            lines = f.readlines()
            f.seek(0)  # Dosya başına dön
            for line in lines:
                # Satırın ilk karakterini değiştir
                f.write("1" + line[1:])
            f.truncate()  # Dosyanın sonundaki gereksiz karakterleri sil
