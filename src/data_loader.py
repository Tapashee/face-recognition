import os

def load_dataset(data_dir):
    dataset = {}

    for person in os.listdir(data_dir):
        person_path = os.path.join(data_dir, person)
        
        if not os.path.isdir(person_path):
            continue
        
        images = []
        for img_name in os.listdir(person_path):
            img_path = os.path.join(person_path, img_name)
            images.append(img_path)
        
        dataset[person] = images
    
    return dataset

if __name__ == "__main__":
    DATA_DIR = "data/raw_data/fgnet"
    dataset = load_dataset(DATA_DIR)

# Print number of images per person
for person, images in dataset.items():
    print(person, "->", len(images), "images")