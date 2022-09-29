import os
import numpy as np
import pandas as pd
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from flask import Flask, render_template, request
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array

app = Flask(__name__)

#dic = {0 : 'Ok', 1 : 'Not Good'}

model = load_model('model.hdf5')

def get_model():
    global model
    model = load_model('model.hdf5')
    print("Model loaded!")

def load_image(img_path):

    i = image.load_img(img_path, target_size=(250, 250))
    i = image.img_to_array(i)                    
    i = np.expand_dims(i, axis=0)         
    i /= 255.  
    p = model.predict(i)                                    


    
   # return dic[p[0]]


get_model()

@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template('index.html')

@app.route("/submit", methods = ['GET','POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']

		img_path = "C:/Users/Paras Kapoor/image/" + img.filename	
		img.save(img_path)

		p = load_image(img_path)

	return render_template("index.html", prediction = p, img_path = img_path)
  

if __name__ == "__main__":
    app.run(debug = True)


