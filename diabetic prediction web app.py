# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 22:18:34 2025

@author: HP
"""

import numpy as np
import pickle
import streamlit as st

# loading the saved model
#loaded_model = pickle.load(open('C:/Users/HP/OneDrive/Desktop/ml/trained_model.sav', 'rb'))
#loaded_model = pickle.load(open('trained_model.sav', 'rb'))
import os

model_path = os.path.join(os.path.dirname(__file__), 'trained_model.sav')
loaded_model = pickle.load(open(model_path, 'rb'))

import pickle
import os

#creating a function for prediction
def diabetes_prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'

def main():
    #title for webpage
    st.title('Diabetes Prediction App')
    
    #input data
    
    Pregnancies=st.text_input('Number of Pregnancies')
    Glucose=st.text_input('Mention the Glucose Level')
    BloodPressure=st.text_input('Mention the Blood Pressure Level')
    SkinThickness=st.text_input('What is your Skin Thickness Value')
    Insulin=st.text_input('Mention insulin level')
    BMI=st.text_input('Mention your BMI')
    DiabetesPedigreeFunction=st.text_input('Mention Diabetes Pedigree Function level')
    Age=st.text_input('Mention your age')
    
    #code for prediction
    diagnosis=''
    
    #creating button
    if st.button('Diabetes Test Result'):
        diagnosis=diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    st.success(diagnosis)
    

if __name__=='__main__':
    main()
    
    
    
    
    
    
    