from crypt import methods
import json
from flask import Flask, jsonify, request
from flask_cors import CORS
from io import BytesIO
import base64
from redis import Redis

from PIL import Image

app = Flask(__name__)
CORS(app)
redis = Redis(host="redis", port=6379)

# Configure the app for production
app.config["DEBUG"] = False

@app.route("/")
def index():
    return "<h1>APIs for inference </h1>"

@app.route("/info-api", methods=['GET'])
def info_api():
    info = {
        "model_details": {
            "name": "linknet",
            "accuracy": 0.95
        }
    }
    return jsonify(info)



@app.route('/prediction', methods=["POST"])
def prediction():
    # get form DICOM data
    form_data = request.form

    print(form_data)
    print("INFO: Obtaining predictions")
    results = {
          "data": {
                "attributes": [{
                    "title": "Prediction",
                    "description": "Abnormal"
                    },
                    {
                        "title": "Probability",
                        "description": "94.5"
                    },
                    {
                        "title": "Operation",
                        "description": "Operation was successful"
                    }
                ],
                "sections": [{
                    "start" : {
                        "x": 100,
                        "y": 100
                    },
                    "end": {
                        "x": 200,
                        "y": 200
                    }
                }
            ]
        }
    }

    return jsonify(results)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)