from models import *



logging.basicConfig(level=logging.INFO)

temp_directory = 'temp'
image_directory = 'C:/Users/toshiba/Documents/Bachelor 3/MSPR/MSPR_6.3/Data'
if not os.path.exists(temp_directory):
    os.makedirs(temp_directory)

@app.route('/identify', methods=['POST'])
def identify():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'Aucune image trouvée'}), 400

        image = request.files['image']
        temp_path = os.path.join(temp_directory, image.filename)
        image_path = os.path.join(image_directory, image.filename)
        image.save(temp_path)
        image.save(image_path)

        predicted_animal = predict_animal(model, temp_path)  # Prédiction
        os.remove(temp_path)  # Nettoyage du fichier temporaire
        
        photo_data = PhotoData(
            file_path=image_path,
            animal_identifier=predicted_animal
        )
        
        db.session.add(photo_data)  # Ajouter à la base de données
        logging.info("PhotoData ajouté avec succès.")
        db.session.commit()  # Sauvegarder les changements

        return jsonify({'animal': predicted_animal})
    except Exception as e:
        logging.error("Erreur lors de l'identification de l'image:", exc_info=e)
        return jsonify({'error': 'Erreur lors de l\'identification'}), 500



@app.route("/")
def index():
    return jsonify({"nom": "MBANZILA DIMBOU victory"})