from flask import Flask, request, jsonify, render_template


app = Flask(__name__)

#@app.route('/')
#def hello():
#    return render_template('generic.html')
    
@app.route('/', methods=['GET', 'POST'])
def returnClass():
    return '<p> Class </p>'

