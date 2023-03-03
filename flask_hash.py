from flask import Flask
import matplotlib.image as image
import hashlib

app2 = Flask(__name__)
@app2.route('/')
def image_hash():
    img = image.imread('imag.jpg')
    img_bytes = img.tobytes()
    result = hashlib.md5(img_bytes).hexdigest()
    return result
if __name__ == '__main__':
    app2.run()

