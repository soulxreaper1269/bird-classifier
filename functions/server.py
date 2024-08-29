from flask_serverless import FlaskServerless
from app import app

serverless_app = FlaskServerless(app)

def handler(event, context):
    return serverless_app(event, context)
