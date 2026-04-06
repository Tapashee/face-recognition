# What is face recognition?
Face recognition is the process of verifying a person's identity based on unique facial features captured from photos and viedos. The basic steps of face recognition are: 

Face detection -> Face alignment -> Embedding -> Matching

## Face Detection
Face detection is the initial step in the process, where the system identifies and locates human faces within an image or video frame. This step isolates the facial region from the background, enabling further processing.

## Alignment
Face alignment standardizes the orientation and positioning of detected faces to ensure consistency across the dataset. This includes correcting variations such as rotation, tilt, and scale. By transforming faces into a normalized and properly aligned format, this step reduces discrepancies caused by pose, lighting conditions, and facial expressions, thereby improving the robustness and accuracy of the model.

## Embedding
Embedding refers to the transformation of a facial image into a numerical representation, commonly known as a feature vector. This vector encodes the unique characteristics of a face in a high-dimensional space.These embeddings enable efficient comparison between faces by converting visual information into mathematical form.

One of the most widely used models for generating embeddings is FaceNet, which produces a 128-dimensional feature vector for each input image. Other notable models include ArcFace, VGG-Face, DeepFace, and ViT-Face.

## Matching
In the matching stage, the generated embeddings are compared to determine identity. This is achieved by computing similarity scores between feature vectors. Common techniques used for similarity measurement include:

### Euclidean Distance: 
Measures the straight-line distance between two embeddings. A smaller distance indicates greater similarity between faces.
### Cosine Similarity: 
Evaluates the angle between two vectors. A smaller angle (or higher cosine value) indicates higher similarity.
### Machine Learning Methods: 
Algorithms such as Support Vector Machines (SVM) and K-Nearest Neighbors (K-NN) can also be used for classification and matching.

# Why is face recognition difficult with appearance change?
Face recognition systems often struggle when a person’s appearance changes over time. These changes can significantly affect the accuracy of the model because facial features are not always constant. Appearance of a person can change in following ways:
- Aging
- Looks variation (caused by weight change, accessories, hair style, makeup, facial expression) 
- Lighting conditions
- Pose variations

## Aging Effects
- Facial structure changes over time
- Skin texture gradually evolves
- Wrinkles develop and become more prominent
- Skin may sag with age
- Facial contours can shift or lose definition

These changes directly impact facial feature representations (feature vectors) used for identification. As a result, the model may find it more difficult to accurately recognize the same individual over time.

## Looks Variation Effects
Changes in appearance can also make recognition challenging, including:
- Hairstyles (e.g., long hair vs short hair vs bald head)
- Facial hair (beard, mustache)
- Makeup
- Accessories (glasses, hats, masks)

These variations can partially obscure or modify key facial features.

## Lighting Condition Effects
Different lighting conditions can change how facial features appear in an image. Shadows, brightness, and contrast variations may distort important details used for recognition.

## Pose Variation Effects
Variations in head position (side view, tilted face) and facial expressions (smiling, frowning) can affect how features are captured and interpreted.

