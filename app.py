from flask import Flask, request, jsonify
import flask
import werkzeug
import re
# from detect import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def check():
    return 'OK'


@app.route('/post', methods=['POST'])
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
    from detect import helper
    note = helper(file_name)
    note += ".jpg"
    print("Detected note: ", note)
    currency = ""
    if(re.findall(".*[2][0][0][0].*", note)):
        currency = "2000"
    elif(re.findall(".*[2][0][0][^0].*", note)):
        currency = "200"
    elif(re.findall(".*[2][0][^0].*", note)):
        currency = "20"
    elif(re.findall(".*[1][0][0][^0].*", note)):
        currency = "100"
    elif(re.findall(".*[1][0][^0].*", note)):
        currency = "10"
    elif(re.findall(".*[5][0][0].*", note)):
        currency = "500"
    elif(re.findall(".*[5][0][^0].*", note)):
        currency = "50"
    else:
        currency = "-1"
    
    print("Detected Currency: ", currency)
    if currency != "-1":
        return jsonify({
            "note": currency
        })
    else:
        return jsonify({
            "note": -1
        })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4555, debug=True)
