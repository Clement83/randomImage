import os
import random
from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/random-image')
def random_image():
    media_folder = './media'
    images = [f for f in os.listdir(media_folder) if os.path.isfile(os.path.join(media_folder, f))]
    if not images:
        return "No images found", 404
    selected_image = random.choice(images)
    return send_from_directory(media_folder, selected_image)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)