
# **Image Classification with Deep Learning**  

### **🌟 Introduction**  
This project is about building an **Image Classification System** that can identify fruits and vegetables using deep learning. I used TensorFlow to train a model and deployed it as a web app with Streamlit. The app takes an image as input and predicts what fruit or vegetable it is with a confidence score.

This project demonstrates how to create a simple but powerful image classification tool using deep learning.  

---  

### **📂 Dataset**  
The dataset includes images of 35 different fruits and vegetables, each organized into folders based on the category (e.g., Apple, Banana, Tomato).  

---  

### **🧪 Preprocessing**  
- **Image Resize**: All images were resized to 180x180 pixels to make them consistent.  
- **Normalization**: The images were scaled to values between 0 and 1 for better performance.  
- **Data Augmentation**: I used techniques like rotating and flipping images to improve the model's ability to recognize different variations of the same object.  

---  

### **🤖 Model Details**  
- The model was trained to recognize 35 different fruits and vegetables using a deep learning approach.
- I used a neural network that learns features from images and makes predictions based on what it learns.  
- The model was trained to be accurate and efficient using the Adam optimizer.  

---  

### **📈 Training and Evaluation**  
- The model was trained on the images, with some reserved for testing to make sure it could make accurate predictions on new data.  
- After training, the model was able to recognize fruits and vegetables with a high level of accuracy.  

---  

### **🚀 Deployment with Streamlit**  
I created a simple web app using Streamlit where users can upload an image of a fruit or vegetable, and the model will predict what it is.  
- **Image Upload**: You can upload an image file (e.g., Banana.jpg).  
- **Prediction**: The app will display the image and show the predicted label (like "Banana") along with a confidence score.  

---  

### **🎨 Application Demo**  
1. Upload an image of a fruit or vegetable.  
2. The app will process the image and show the prediction (e.g., "Banana").  
3. It will also show the confidence level of the prediction (e.g., 85%).  

---  

### **💡 Challenges and Learnings**  
1. **Improving Model Accuracy**: It took time to fine-tune the model for better performance.  
2. **Making the App User-Friendly**: Setting up a simple interface for users to upload images and get results was an important part of the project.  
