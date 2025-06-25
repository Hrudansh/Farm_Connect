# Farm_Connect
# 🌾 Farm Connect: AI-Driven Disease Detection and Farmer Support System

Farm Connect is an AI-powered web-based platform designed to assist farmers in identifying plant diseases, receiving tailored treatment recommendations, and accessing agricultural support via a multilingual chatbot. The system utilizes a deep learning model (MobileNetV2) trained on the Plant Village dataset to detect 39+ plant disease classifications with over **91.33% accuracy**.

## 🚀 Features

- 🔍 **AI-Based Plant Disease Detection**  
  Uses MobileNetV2 model trained on augmented image datasets for real-time disease identification.
  
- 🧠 **Multilingual Chatbot Support**  
  Provides treatment suggestions, farming tips, and product recommendations in user-friendly language.

- 📱 **Mobile & Desktop Support**  
  Fully responsive web interface to allow farmers to capture and upload images using smartphones or desktops.

- 🌐 **Offline Capability**  
  Essential features work even in low-connectivity regions.

- 🧪 **Product Recommendations**  
  Suggests fertilizers, pesticides, and supplements based on the diagnosed disease.

## 🧠 Technology Stack

| Layer         | Tools & Libraries                                |
|---------------|--------------------------------------------------|
| AI Model      | MobileNetV2, TensorFlow, Keras                   |
| Backend       | Python, Flask / FastAPI                          |
| Frontend      | HTML, CSS, JavaScript                            |
| Data Handling | NumPy, Pandas, OpenCV                            |
| Deployment    | Render / Hugging Face Spaces / Firebase          |
| Chatbot       | NLP techniques, Multilingual Support             |
| Security      | Firebase/Auth0, HTTPS, Encrypted API Calls       |

## 📊 Model Performance

- **Train Accuracy**: 90.00%  
- **Validation Accuracy**: 90.69%  
- **Test Accuracy**: 91.33%  
- **F1 Score**: 0.9160

### ✅ Evaluation Metrics
- Classification Report
- Confusion Matrix
- Precision, Recall, F1-Score

## 📁 Functional Requirements

1. Collect dataset from various agricultural sources.
2. Preprocess and store the data in `.csv` format.
3. Apply image augmentations (rotation, flipping, jitter, blur, affine).
4. Train MobileNetV2 using TensorFlow/Keras.
5. Evaluate model performance with relevant metrics.
6. Build a REST API using Flask or FastAPI.
7. Create a responsive frontend with upload functionality.
8. Integrate a multilingual chatbot for farmer interaction.
9. Provide product recommendations for detected diseases.

## ⚙️ Non-Functional Requirements

- ⏱️ **Performance**: ≥ 90% accuracy, response in ≤ 3 seconds  
- 🌍 **Scalability**: Supports multiple concurrent users  
- 🧑‍🌾 **Usability**: Farmer-friendly UI, multilingual support  
- 🔒 **Security**: Auth via Firebase/Auth0, encrypted data transfer  
- 📈 **Reliability**: 99.5% uptime, robust predictions  
- 🔄 **Maintainability**: Modular structure for easy updates  
- 🕐 **Availability**: 24/7 access with failover mechanisms  


## 💡 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Farm-Connect.git
   cd Farm-Connect
pip install -r requirements.txt
python app.py

📦 Deployment
Easily deploy on Render, Hugging Face Spaces, or Firebase Hosting.

Backend and model exposed via REST API.

Secure authentication and data handling using Firebase/Auth0.

📌 Limitations & Future Work
📉 Dataset imbalance may affect accuracy for rare diseases.

🌐 Current chatbot supports only English (multilingual expansion ongoing).

📡 Connectivity issues in rural areas tackled via offline capabilities.

🔁 Real-time training updates and community image contributions under development.

🤝 Contributions
Contributions are welcome! Please fork the repo and submit a pull request.

🌱 Empowering farmers with AI — one crop at a time.

