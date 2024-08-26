from flask import Flask, render_template, request
from PIL import Image, ImageDraw, ImageFont
import io
import base64
from predict import *

app = Flask(__name__)

def add_text_to_image(image, text="Sample Text"):
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    
    # Position the text at the top-left corner
    text_position = (10, 10)
    
    # Draw the text on the image
    draw.text(text_position, text, font=font, fill=(255, 255, 255))
    
    return image

def returntext(text: str): 
    return "hello"+ text



@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if 'image' not in request.files:
            return "No file uploaded", 400
        
        file = request.files['image']
        
        if file.filename == '':
            return "No selected file", 400
        
        # Get the additional string from the form
        

        # Open the image file
        image = Image.open(file.stream)
        
        # Add text to the image
        processed_image = image
        
        # Save the processed image to a byte stream
        img_io = io.BytesIO()
        processed_image.save(img_io, 'PNG')
        img_io.seek(0)
        
        # Convert image to base64 to embed in HTML
        img_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')
        display_text_list = predict(transform_image(image))
    
        # Render the image and text on the webpage
        return render_template('final.html', img_data=img_base64, display_text=display_text_list[1], probability = "{:.3f}".format(display_text_list[0]))

    return render_template('final.html')

if __name__ == '__main__':
    app.run(debug=True)


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