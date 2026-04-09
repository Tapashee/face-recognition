import os
import cv2 as cv
from src.preprocessing.data_loader import load_dataset

DEST_DIR = os.path.join("data", "processed_data", "fgnet")

def face_detection_opencv(dataset):
    # Load Haar cascade (pretrained frontal face detector)
    face_cascade = cv.CascadeClassifier(
        cv.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    for person, img_paths in dataset.items():
        # Create folder for this person
        person_dir = os.path.join(DEST_DIR, person)
        os.makedirs(person_dir, exist_ok=True)

        face_count = 0

        for img_path in img_paths:
            # Read image
            image = cv.imread(img_path)

            # Convert to grayscale
            gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

            # detect face
            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.3,
                minNeighbors=5
            )

            # if no face found continue
            if len(faces) == 0:
                print(f"No face found in image path: {img_path}")
                continue

            # Crop and save each face found in the image
            for (x, y, w, h) in faces:
                face = image[y:y+h, x:x+w]
                face_count += 1
                save_path = os.path.join(person_dir, f"face_{face_count}.jpg")
                cv.imwrite(save_path, face)
            

if __name__ == "__main__":
    dataset = load_dataset()
    face_detection_opencv(dataset)