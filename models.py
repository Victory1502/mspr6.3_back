# Si vous avez des conflits avec Keras, utilisez TensorFlow directement
import pytest
import os, cv2, io
import tensorflow as tf
import numpy as np
import logging
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy



app= Flask(__name__)
CORS(app, origins=["http://127.0.0.1:5000"])

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/sqlite/wildlens.db'
db = SQLAlchemy(app)


# debut class

class PhotoData(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    file_path= db.Column(db.String(255), nullable=False)
    animal_identifier = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

# debut model

# Charger les données
# data_path= 'Dataset'
# categories = os.listdir(data_path)
# label_dict = {category: i for i, category in enumerate(categories)}

# img_size = 100
# data = []
# target = []

# for category in categories:
#     folder_path = os.path.join(data_path, category)
#     img_names = os.listdir(folder_path)

#     for img_name in img_names:
#         img_path = os.path.join(folder_path, img_name)
#         img = cv2.imread(img_path)

#         try:
#             resized = cv2.resize(img, (img_size, img_size))
#             data.append(resized)
#             target.append(label_dict[category])

#         except Exception as e:
#             print("Exception:", e)

# # Normaliser les données
# data = np.array(data) / 255.0
# data = np.reshape(data, (data.shape[0], img_size, img_size, 3))

# # Encoder les labels manuellement sans keras.utils
# num_classes = len(categories)
# target_one_hot = np.zeros((len(target), num_classes))

# for idx, val in enumerate(target):
#     target_one_hot[idx, val] = 1

# # Créer le modèle
# model = tf.keras.Sequential([
#     tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(img_size, img_size, 3)),
#     tf.keras.layers.MaxPooling2D((2, 2)),
#     tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
#     tf.keras.layers.MaxPooling2D((2, 2)),
#     tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
#     tf.keras.layers.MaxPooling2D((2, 2)),
#     tf.keras.layers.Flatten(),
#     tf.keras.layers.Dense(128, activation='relu'),
#     tf.keras.layers.Dense(num_classes, activation='softmax')
# ])

# # Compiler le modèle
# model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# # Entraîner le modèle
# model.fit(data, target_one_hot, epochs=10, validation_split=0.2)

# # Enregistrer le modèle au format HDF5



# # Prédire une nouvelle image
# def predict_animal(model, image_path):
#     img = cv2.imread(image_path)
#     resized = cv2.resize(img, (img_size, img_size))
#     normalized = np.array([resized / 255.0])
#     prediction = model.predict(normalized)
#     predicted_class = categories[np.argmax(prediction)]
#     return predicted_class

# model enregistrer

model = tf.keras.models.load_model("animal_identifier_model.h5")

img_size = 100
categories = ['Castor', 'Chat', 'Chien', 'Coyote', 'Écureuil', 'Lapin', 'Loup','Lynx', 'Ours', 'Puma', 'Rat', 'Raton Laveur', 'Renard'];  # Ajoutez vos catégories

# Prédiction à partir d'une image
def predict_animal(model, image_path):
    img = cv2.imread(image_path)
    resized = cv2.resize(img, (img_size, img_size))
    normalized = np.array([resized / 255.0])
    prediction = model.predict(normalized)
    predicted_class = categories[np.argmax(prediction)]
    return predicted_class


# Utilisation du modèle pour prédire un animal à partir d'une image
image_path = 'chemin_vers_votre_image.jpg'
predicted_animal = predict_animal(model, "depositphotos_258709504-stock-photo-large-dog-footprint-fresh-imprint.jpg")
print(f"L'animal prédit est : {predicted_animal}")