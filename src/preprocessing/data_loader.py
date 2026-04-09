import os

def load_dataset():
    DATA_DIR = os.path.join("data", "raw_data", "fgnet")
    dataset = {}

    for person in os.listdir(DATA_DIR):
        person_path = os.path.join(DATA_DIR, person)
        
        if not os.path.isdir(person_path):
            continue
        
        images = []
        for img_name in os.listdir(person_path):
            img_path = os.path.join(person_path, img_name)
            images.append(img_path)
        
        dataset[person] = images
    
    return dataset

if __name__ == "__main__":
    dataset = load_dataset()