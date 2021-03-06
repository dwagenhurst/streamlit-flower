import streamlit as st
import plotly.express as px
import pickle
import numpy as np
from predict import predict_flower


st.title('Iris Species Predictor')
st.header("Let's predict Iris species")
st.subheader('Cool')

@st.cache()   # saves time since it will only load the file once per user
def read_data():
    return px.data.iris()

show_df = st.checkbox("Do you want to see the data?")

df_iris = read_data()

fig = px.histogram(df_iris, x='sepal_length')
fig

if show_df:
    df_iris


col1, col2 = st.columns(2)

with col1:
    sl = st.number_input("Sepal Length (cm)", 0.0, 10.0)
    sw = st.number_input("Sepal Width (cm)", 0.0, 100.0)
    

with col2:
    pl = st.number_input("Petal Length (cm)", 0.0, 100.0)
    pw = st.number_input("Petal Width (cm)", 0.0, 100.0)  
    
      

user_input = np.array([[sl, sw, pl, pw]])


with open('saved-iris-model.pkl', 'rb') as f:
    classifier = pickle.load(f)


with st.spinner('Predicting...'):
    prediction = predict_flower(classifier, user_input)
prediction


if prediction[0] == 'setosa':
    st.image('https://static.streamlit.io/examples/dog.jpg')



# st.balloons()