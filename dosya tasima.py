import os
import shutil

source_folder_path = r'D:\griffin\veri setleri\UYZ2023_dataset\images'  # kaynak klasör yolunu buraya girin
txt_folder_path = r'D:\griffin\veri setleri\UYZ2023_dataset\txt'  # txt dosyalarının hedef klasör yolunu buraya girin
jpg_folder_path = r'D:\griffin\veri setleri\UYZ2023_dataset\images'  # jpg dosyalarının hedef klasör yolunu buraya girin

# txt klasörü oluştur
if not os.path.exists(txt_folder_path):
    os.makedirs(txt_folder_path)

# jpg klasörü oluştur
if not os.path.exists(jpg_folder_path):
    os.makedirs(jpg_folder_path)

# kaynak klasöründeki dosyaları işle
for file_name in os.listdir(source_folder_path):
    if file_name.endswith('.txt'):
        # txt dosyalarını txt klasörüne taşı
        shutil.move(os.path.join(source_folder_path, file_name), os.path.join(txt_folder_path, file_name))
        print(f"{file_name} dosyası {txt_folder_path} klasörüne taşındı.")
    elif file_name.endswith('.jpg'):
        # jpg dosyalarını jpg klasörüne taşı
        shutil.move(os.path.join(source_folder_path, file_name), os.path.join(jpg_folder_path, file_name))
        print(f"{file_name} dosyası {jpg_folder_path} klasörüne taşındı.")
    else:
        # diğer dosyaları geç
        continue
