import os
import random
from flask import Flask, send_from_directory
from PIL import Image

app = Flask(__name__)

@app.route('/random-image')
def random_image():
    media_folder = './media'
    webp_folder = './media/webp'
    
    # Vérifier si le dossier WebP existe, sinon le créer
    if not os.path.exists(webp_folder):
        os.makedirs(webp_folder)
    
    # Lister toutes les images dans le dossier media
    images = [f for f in os.listdir(media_folder) if os.path.isfile(os.path.join(media_folder, f))]
    
    if not images:
        return "No images found", 404
    
    # Sélectionner une image au hasard
    selected_image = random.choice(images)
    
    # Obtenir le chemin complet de l'image d'origine
    original_image_path = os.path.join(media_folder, selected_image)
    
    # Générer le nom et chemin de l'image en webp
    webp_image_name = os.path.splitext(selected_image)[0] + '.webp'
    webp_image_path = os.path.join(webp_folder, webp_image_name)
    
    # Si l'image WebP existe déjà, la retourner
    if os.path.exists(webp_image_path):
        return send_from_directory(webp_folder, webp_image_name)
    
    # Sinon, convertir l'image en WebP et la sauvegarder
    try:
        img = Image.open(original_image_path)
        img.save(webp_image_path, 'webp')
    except Exception as e:
        return f"Failed to convert image to WebP: {str(e)}", 500
    
    # Retourner l'image WebP convertie
    return send_from_directory(webp_folder, webp_image_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
