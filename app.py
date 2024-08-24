from flask import Flask, request, jsonify, render_template, send_file
from PIL import Image
import io


app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('test.html')
    
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

        return render_template('generic.html') # add html code ree

