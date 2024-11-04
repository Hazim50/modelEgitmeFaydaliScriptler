import os


def remove_unlabeled_images(image_folder, label_folder):
    image_files = os.listdir(image_folder)

    for image_file in image_files:
        if image_file.endswith(".jpg"):
            label_file = os.path.splitext(image_file)[0] + ".txt"
            label_path = os.path.join(label_folder, label_file)
            image_path = os.path.join(image_folder, image_file)

            if not os.path.exists(label_path):
                os.remove(image_path)
                print(f"Etiketi olmayan fotoğraf silindi: {image_file}")


remove_unlabeled_images("/home/hazim/Desktop/hazimEtiketlenecek/images/", "/home/hazim/Desktop/hazimEtiketlenecek/labels/")
