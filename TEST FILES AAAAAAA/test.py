from flask import Flask, render_template, request, send_file
from PIL import Image, ImageDraw, ImageFont
import io
import base64

app = Flask(__name__)

def add_text_to_image(image, text="Sample Text"):
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    
    # Position the text at the top-left corner
    text_position = (10, 10)
    
    # Draw the text on the image
    draw.text(text_position, text, font=font, fill=(255, 255, 255))
    
    return image

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if 'image' not in request.files:
            return "No file uploaded", 400
        
        file = request.files['image']
        
        if file.filename == '':
            return "No selected file", 400
        
        # Open the image file
        image = Image.open(file.stream)
        
        # Add text to the image
        processed_image = add_text_to_image(image)
        
        # Save the processed image to a byte stream
        img_io = io.BytesIO()
        processed_image.save(img_io, 'PNG')
        img_io.seek(0)
        
        # Convert image to base64 to embed in HTML
        img_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')
        
        # Render the image on the webpage
        return render_template('test.html', img_data=img_base64)

    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)
