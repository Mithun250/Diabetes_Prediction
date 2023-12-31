from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(page_title='Diabetes Prediction')
st.markdown(f'<h1 style="text-align: center;">Diabetes Prediction</h1>', unsafe_allow_html=True)


df=pd.read_csv("C:\\Users\\91915\\OneDrive\\Desktop\\Diabetes\\diabetes_prediction_dataset.csv")

# Preprocessing using Ordinal Encoder
enc=OrdinalEncoder()
df["smoking_history"]=enc.fit_transform(df[["smoking_history"]])
df["gender"]=enc.fit_transform(df[["gender"]])


# Define Independent and Dependent Variables
x= df.drop("diabetes",axis=1)
y=df["diabetes"]


# 70% data - Train and 30% data - Test
x_train , x_test , y_train, y_test = train_test_split(x,y,test_size=0.3)


# DecisionTreeClassifier Algorithm
model = DecisionTreeClassifier().fit(x_train,y_train)
y_pred = model.predict(x_test)
accuracy = metrics.accuracy_score(y_test,y_pred)



col1, col2 = st.columns(2, gap='large')

with col1:
    gender = st.selectbox(label='Gender', options=['Male', 'Female', 'Other'])
    g_dict = {'Female':0.0, 'Male':1.0, 'Other':2.0}

    age = st.text_input(label='Age')

    hypertension = st.selectbox(label='Hypertension', options=['No', 'Yes'])
    h_dict = {'No':0, 'Yes':1}

    heart_disease = st.selectbox(label='Heart Disease', options=['No', 'Yes'])
    heart_dict = {'No':0, 'Yes':1}

with col2:
    smoking_history = st.selectbox(label='Smoking History', 
                                   options=['Never', 'Current', 'Former', 'Ever', 'Not Current', 'No Info'])
    smoking_dict = {'Never':4.0, 'No Info':0.0, 'Current':1.0, 
                            'Former':3.0, 'Ever':2.0, 'Not Current':5.0}

    bmi = st.text_input(label='BMI')

    hba1c_level = st.text_input(label='HbA1c Level')

    blood_glucose_level = st.text_input(label='Blood Glucose Level')

st.write('')
st.write('')
col1,col2 = st.columns([0.438,0.562])
with col1:
    accuracy=st.button(label="Accuracy")
st.write('')

if accuracy:
    try:
        st.write('Accuracy', metrics.accuracy_score(y_test, y_pred))
    except:
        st.warning('Please fill the all required informations')

with col2:
    submit = st.button(label='Submit')
st.write('')


if submit:
    try:
        user_data = np.array( [[ g_dict[gender], age, h_dict[hypertension], heart_dict[heart_disease],
                                smoking_dict[smoking_history], bmi, hba1c_level, blood_glucose_level ]] )

        test_result = model.predict(user_data)

        if test_result[0] == 0:
            col1,col2,col3 = st.columns([0.33,0.30,0.35])
            with col2:
                st.success('Diabetes Result: Negative')
 
        else:
            col1,col2,col3 = st.columns([0.215,0.57,0.215])
            with col2:
                st.error('Diabetes Result: Positive (Please Consult with Doctor)')

    except:
        st.warning('Please fill the all required informations')