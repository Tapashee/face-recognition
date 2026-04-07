import os
import cv2
import matplotlib.pyplot as plt
from data_loader import load_dataset

DATA_DIR = "data/raw_data/fgnet"

def show_images(dataset, num_people=3, images_per_person=5):
    for person, image_paths in list(dataset.items())[:num_people]:
        plt.figure(figsize=(10, 3))

        for i, img_path in enumerate(image_paths[:images_per_person]):
            img = cv2.imread(img_path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            plt.subplot(1, images_per_person, i+1)
            plt.imshow(img)
            plt.title(person)
            plt.axis("off")

        plt.show()

if __name__ == "__main__":
    dataset = load_dataset(DATA_DIR)
    show_images(dataset)