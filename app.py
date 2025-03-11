import os
from flask import Flask, render_template, request
from PIL import Image
import numpy as np
import torch
import torchvision.transforms as transforms
import torchvision.models as models
import pandas as pd

# Load disease and supplement info
disease_info = pd.read_csv('disease_info.csv', encoding='cp1252')
supplement_info = pd.read_csv('supplement_info.csv', encoding='cp1252')

class_names = list(disease_info['disease_name'])

# Load MobileNetV2 Model
num_classes = 39  # Adjust based on the number of classes in your dataset
model = models.mobilenet_v2(weights=None)  # No pre-trained weights
model.classifier[1] = torch.nn.Linear(model.classifier[1].in_features, num_classes)  # Adjust for classification
model.load_state_dict(torch.load("plant_disease_mobilenetv2.pt", map_location=torch.device('cpu')))
model.eval()

# Image transformation
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # MobileNetV2 normalization
])

# Prediction function
def predict(image_path):
    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0)  # Add batch dimension
    with torch.no_grad():
        output = model(image)
    predicted_class = torch.argmax(output, dim=1).item()
    return predicted_class

def remove_before_colon(input_string):
    """Keeps the full name instead of removing anything before ':'."""
    return input_string  # Just return the original string without modification


# Flask app
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact-us.html')

@app.route('/index')
def ai_engine_page():
    return render_template('index.html')

@app.route('/mobile-device')
def mobile_device_detected_page():
    return render_template('mobile-device.html')

@app.route('/submit', methods=['POST'])
def submit():
    if 'image' not in request.files:
        return "No image uploaded", 400

    image = request.files['image']
    filename = image.filename
    file_path = os.path.join('static/uploads', filename)
    image.save(file_path)

    pred = predict(file_path)
    title = remove_before_colon(disease_info['disease_name'][pred]) 
    description = disease_info['description'][pred]
    prevent = disease_info['Possible Steps'][pred]
    image_url = disease_info['image_url'][pred]
    supplement_name = supplement_info['supplement name'][pred]
    supplement_image_url = supplement_info['supplement image'][pred]
    supplement_buy_link = supplement_info['buy link'][pred]

    return render_template('submit.html', title=title, desc=description, prevent=prevent, 
                           image_url=image_url, pred=pred, sname=supplement_name, 
                           simage=supplement_image_url, buy_link=supplement_buy_link)

@app.route('/market')
def market():
    return render_template('market.html', supplement_image=list(supplement_info['supplement image']),
                           supplement_name=list(supplement_info['supplement name']), 
                           disease=list(disease_info['disease_name']), 
                           buy=list(supplement_info['buy link']))

if __name__ == '__main__':
    app.run(debug=True)
