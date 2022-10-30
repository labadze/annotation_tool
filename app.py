import base64
import os
from os import walk
import json

import flask
from flask import Flask, request, send_from_directory
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True, resources={r"/*": {"origins": "*"}})

app.config['CORS_HEADERS'] = 'Content-Type'


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


def get_dir_files():
    file_list = []
    # mylist = [f for f in glob.glob("*.txt")]
    filenames = next(walk('static/img'), (None, None, []))[2]  # [] if no file
    if len(filenames) > 0:
        for filename in filenames:
            if filename.split('.')[1].lower() == 'png' or filename.split('.')[1].lower() == 'jpg' or \
                    filename.split('.')[1].lower() == 'svg' or filename.split('.')[1].lower() == 'jpeg':
                items = read_file()
                entry = next((x for x in items if str(x["img_path"]) == str(filename)), None)
                item_json_obj = {
                    "file_path": '{server_url}/static/img/{filename}'.format(filename=filename,
                                                                             server_url='http://127.0.0.1:5000'),
                    "file_name": filename,
                    "data_available": entry is not None and len(entry["annotations"]) > 0
                }
                file_list.append(item_json_obj)
    return file_list


def read_file():
    # Opening JSON file
    f = open('data.json')
    # returns JSON object as
    # a dictionary
    data = json.load(f)
    # Closing file
    f.close()
    return data


def write_data_to_file(data):
    data_list = read_file()
    list_to_write = []
    if len(data_list) > 0:
        list_to_write.append(data)
        for item in data_list:
            list_to_write.append(item)
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(list_to_write, f, ensure_ascii=False, indent=4)
    else:
        list_to_write.append(data)
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(list_to_write, f, ensure_ascii=False, indent=4)


@app.route('/image_list', methods=['GET'])
def root():  # put application's code here
    image_list = get_dir_files()
    return {
               "data": image_list,
           }, 200, {
               "Content-Type": "application/json"
           }


@app.route('/file/<file_id>', methods=['GET'])
def get_file_info(file_id):
    items = read_file()
    if len(items) == 0:
        return {
                   "error": "There is no data in file."
               }, 400, {
                   "Content-Type": "application/json"
               }

    entry = next((x for x in items if str(x["id"]) == str(file_id)), None)
    if entry is None:
        return {
                   "error": "There is no entry with provided Id (Not found)."
               }, 404, {
                   "Content-Type": "application/json"
               }
    return {
               "data": entry
           }, 200, {
               "Content-Type": "application/json"
           }


@app.route('/file', methods=['GET'])
def get_by_file_name():
    encoded_file_name = request.args.get('encoded_file_name')
    decoded_file_name = base64.b64decode(encoded_file_name).decode('utf-8')
    items = read_file()
    if len(items) == 0:
        return {
                   "success": False,
                   "error": "There is no data in file."
               }, 200, {
                   "Content-Type": "application/json"
               }
    entry = next((x for x in items if str(x["img_path"]) == str(decoded_file_name)), None)
    if entry is None:
        return {
                   "success": False,
                   "error": "There is no entry with provided file name (Not found)."
               }, 200, {
                   "Content-Type": "application/json"
               }
    return {
               "success": True,
               "data": entry
           }, 200, {
               "Content-Type": "application/json"
           }


@app.route('/file', methods=['POST', 'OPTIONS'])
@cross_origin(allow_headers=['Content-Type'])
def save_file_info():
    data = request.get_json()
    write_data_to_file(data=data)
    return {
               "success": True,
               "data": data
           }, 201, {
               "Content-Type": "application/json"
           }


@app.route('/file/<file_id>', methods=['PATCH'])
def set_file_info(file_id):
    data = request.get_json()
    items = read_file()
    if len(items) == 0:
        return {
                   "error": "There is no data in file."
               }, 400, {
                   "Content-Type": "application/json"
               }

    entry = next((x for x in items if str(x["id"]) == str(file_id)), None)
    if entry is None:
        return {
                   "error": "There is no entry with provided Id (Not found)."
               }, 404, {
                   "Content-Type": "application/json"
               }
    updated_list = []
    for item in items:
        if item["id"] != int(file_id):
            updated_list.append(item)
    updated_list.append(data)
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(updated_list, f, ensure_ascii=False, indent=4)
    return {
               "success": True,
               "id": file_id,
               "data": data
           }, 200, {
               "Content-Type": "application/json"
           }


@app.route('/', methods=['GET'])
def render():
    return flask.render_template("index.html")


@app.route('/test', methods=['GET'])
def render_test():
    return flask.render_template("test.html")


if __name__ == '__main__':
    app.run(use_reloader=True)
