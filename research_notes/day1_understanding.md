# What is face recognition?
Face recognition is the process of verifying a person's identity based on unique facial features captured from photos and viedos. The basic steps of face recognition are: 

Face detection -> Face alignment -> Embedding -> Matching

## Face Detection:
Face detection is the initial step in the process, where the system identifies and locates human faces within an image or video frame. This step isolates the facial region from the background, enabling further processing.

## Alignment:
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

# Why is face recognition with aging or appearance chage is difficult?