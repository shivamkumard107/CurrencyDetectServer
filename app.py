from flask import Flask, request, jsonify
import flask
import werkzeug
from detect import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def check():
    return 'OK'


@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('name')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": "Welcome {param} to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD": "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })


@app.route('/image', methods=['POST'])
def handle_request():
    files_ids = list(flask.request.files)
    image_num = 1
    file_name = ""
    for file_id in files_ids:
        imagefile = flask.request.files[file_id]
        filename = werkzeug.utils.secure_filename(imagefile.filename)
        print("Image Filename : " + imagefile.filename)
        imagefile.save(filename)
        file_name = filename
        image_num = image_num + 1
    note = helper(file_name)
    print(note)
    if note != -1:
        return jsonify({
            "note": note,
        })
    else:
        return jsonify({
            "note": -1
        })


if __name__ == "__main__":
    app.run()
