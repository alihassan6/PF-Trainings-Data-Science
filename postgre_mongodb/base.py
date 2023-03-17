import io
import os
import tqdm
import glob
import traceback
import psycopg2
import pymongo
import gridfs
import bson
from bson.objectid import ObjectId
from flask import Flask
from flask import request
import zipfile
from multiprocessing.pool import ThreadPool
from flask import render_template, send_from_directory
from werkzeug.utils import secure_filename
import cv2
import random

app = Flask(__name__)

con = psycopg2.connect(host="localhost", dbname="pf_data", user="ali", password="Ds@123")
cr = con.cursor()

cr.execute("""
    CREATE TABLE IF NOT EXISTS image (
        id SERIAL PRIMARY KEY,
        person_name VARCHAR(255),
        embeddings BYTEA,
        image_path VARCHAR(255)
    )
""")
con.commit()

def get_embeddings(im_path):
    im = cv2.imread(im_path)
    width = im.shape[1]
    height = im.shape[0]
    new_width = int(width*0.5)
    new_height = int(height*0.5)
    x = random.randint(0,new_width)
    y = random.randint(0,new_height)
    return im[y:y+new_width,x:x+new_width,:]


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(filename)
            os.makedirs("unzipped", exist_ok=True)
            with zipfile.ZipFile(filename, "r") as zip_ref:
                zip_ref.extractall("unzipped")  
            person_name = os.path.splitext(filename)[0]
            file_path = "media/ali-hassan/8A56FC4956FC3811/PF_DataScience/mongoDB_postgres/unzipped/test/hassan.jpg"
            #embeddings = get_embeddings(file_path)
            cr.execute(
                "INSERT INTO image (person_name, image_path) VALUES (%s, %s)",
                (person_name, file_path)
            )
            con.commit()
    return render_template('zip.html')

@app.route('/image')
def get_image():
    directory = '//media/ali-hassan/8A56FC4956FC3811/PF_DataScience/mongoDB_postgres/unzipped/test'
    filename = 'hassan.jpg'
    return send_from_directory(directory, filename)

if __name__ == '__main__':
    app.run(debug=True)