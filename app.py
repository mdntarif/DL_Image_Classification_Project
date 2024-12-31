import tensorflow as tf
from tensorflow.keras.models import load_model
import streamlit as st
import numpy as np

st.header('Image Classification Model')

# Load model
model_path = '/Users/mdtarif/Documents/ML/Image Classification Project/Image_classify.keras'
try:
    model = load_model(model_path, compile=False)  # Load without compiling
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])  # Recompile
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

data_cat = ['apple', 'banana', 'beetroot', 'bell pepper', 'cabbage', 'capsicum', 'carrot',
            'cauliflower', 'chilli pepper', 'corn', 'cucumber', 'eggplant', 'garlic', 'ginger',
            'grapes', 'jalepeno', 'kiwi', 'lemon', 'lettuce', 'mango', 'onion', 'orange',
            'paprika', 'pear', 'peas', 'pineapple', 'pomegranate', 'potato', 'raddish',
            'soy beans', 'spinach', 'sweetcorn', 'sweetpotato', 'tomato', 'turnip', 'watermelon']

img_height, img_width = 180, 180
image = st.text_input('Enter Image name', 'Banana.jpg')

if tf.io.gfile.exists(image):  # Ensure the image file exists
    image_load = tf.keras.utils.load_img(image, target_size=(img_height, img_width))
    img_arr = tf.keras.utils.img_to_array(image_load)  # Fix conversion method
    img_bat = tf.expand_dims(img_arr, 0)

    predict = model.predict(img_bat)
    score = tf.nn.softmax(predict)

    st.image(image, width=200)
    st.write('Veg/Fruit in image is ' + data_cat[np.argmax(score)])
    st.write('With accuracy of {:.2f}%'.format(np.max(score) * 100))
else:
    st.error(f"Image file not found: {image}")