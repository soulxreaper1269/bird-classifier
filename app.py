from flask import Flask, request, render_template
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
        

        file = request.files['image']

        if file.filename == '':
            return 'No selected file'
        #add prediction logic somewhere down here
        img = Image.open(file.stream)
        img_io = io.BytesIO()
        img.save(img_io, 'PNG')
        img_io.seek(0)
        img = base64.b64encode(img_io.getvalue()).decode('utf-8')
        

        txt = "This is a test" #add logic for returning class and probabilities later 

        return render_template('final.html',img_data = img, display_text = txt) # add html code ree

    return render_template('final.html')