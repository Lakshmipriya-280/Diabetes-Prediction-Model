# 🩺 Diabetes Prediction Model

A Machine Learning project to predict whether an individual is diabetic or not based on medical diagnostic measurements.  
This project uses **Support Vector Machine (SVM)** for classification and is deployed using **Streamlit** as a web application.  

## 📌 Problem Statement
Diabetes is a chronic metabolic disease characterized by elevated blood glucose levels, which can lead to severe health complications.  
Early detection and intervention are crucial for improving patient outcomes.  
This project aims to build a predictive system that classifies individuals as **diabetic** or **non-diabetic**.

## ⚙️ System Requirements
- **CPU**: Intel Core i5/i7 (10th Gen or newer) or AMD Ryzen 5/7  
- **RAM**: 8 GB minimum  
- **Storage**: 50 GB free (SSD recommended)  
- **GPU**: Not required  
- **Internet**: Stable connection  


## 🛠️ Tech Stack
- **Languages/Tools**: Python, Streamlit, Google Colab, Anaconda, Spyder  
- **Libraries**:  
  - `numpy`  
  - `pandas`  
  - `scikit-learn`  
  - `pickle`  
  - `os`  
  - `streamlit`  

**Features used:**
- Pregnancies  
- Glucose  
- Blood Pressure  
- Skin Thickness  
- Insulin  
- BMI  
- Diabetes Pedigree Function  
- Age  

**Target Variable:**
- `Outcome`:  
  - `0` → Non-Diabetic  
  - `1` → Diabetic  


## 🚀 Project Workflow
1. **Data Collection** – Load CSV dataset.  
2. **Data Preprocessing** – Standardize data, handle train/test split.  
3. **Model Training** – Train an SVM classifier.  
4. **Evaluation** – Accuracy:  
   - Training Data: ~77%  
   - Test Data: ~72%  
5. **Saving Model** – Model stored using `pickle` as `trained_model.sav`.  
6. **Deployment** – Deployed with **Streamlit** for interactive predictions.  



   git clone https://github.com/Lakshmipriya-280/Diabetes-Prediction-Model.git
   cd Diabetes-Prediction-Model
