from flask import Flask, render_template, request
from PIL import Image
import io
import base64
import os
from predict import *

app = Flask(__name__)


#make a landing page and then a redirect maybe? (for the output)

@app.route('/')
def website():
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if 'image' not in request.files:
            return "No file uploaded", 400
        
        file = request.files['image']
        
        if file.filename == '':
            return "No selected file", 400
        
        image = Image.open(file.stream)
        processed_image = image
        img_io = io.BytesIO()
        processed_image.save(img_io, 'PNG')
        img_io.seek(0)
        
        # Convert image to base64 to embed in HTML
        img_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')
        display_text_list = predict(transform_image(image))

        return render_template('index.html', img_data=img_base64, display_text=display_text_list[1], probability = "{:.3f}".format(display_text_list[0]))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host= "0.0.0.0", port=int(os.environ.get("PORT",8080)))
