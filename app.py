from flask import Flask, request, jsonify, render_template, send_file
from PIL import Image
import io
import base64


app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('final.html')
    
@app.route('/', methods=['GET', 'POST'])
def returnClass():
    if request.method == 'POST':
        if 'image' not in request.files:
            return "Please Upload a File", 400
        

        file = request.files['images']

        if file.filename == '':
            return 'No selected file'
    
        img = Image.open(file.stream)
        # now need to add prediction and return it
        img_io = io.BytesIO()
        img = base64.b64encode(img_io.getvalue()).decode('utf-8')
        img_io.seek(0)

        txt = "This is a test" #add logic for returning class and probabilities later 

        return render_template('final.html',img_data = img, display_text = txt) # add html code ree

    return render_template('final.html')