import streamlit as st
import pickle

pipe = pickle.load(open('pipe.pickle','rb'))
data_frame =pickle.load(open('read_csv.pickle','rb'))

st.title('Laptop Price Predictor')

brand=st.selectbox("Company Name",data_frame['Company'].unique())
ram=st.selectbox("RAM (GB)",data_frame['Ram'].unique())
hdd=st.selectbox("HDD Storage (GB)",[0,128,256,512,1024,2048])
sdd=st.selectbox("SDD Storage (GB)",[0,8,128,256,512,1024])
cpu=st.selectbox("Processor",data_frame['Cpu brand'].unique())
gpu=st.selectbox("GPU", data_frame['Gpu brand'].unique())
weight=st.number_input('Weight of the Laptop')
touch=st.selectbox("Touchscreen",['No','yes'])
os=st.selectbox("OS",data_frame['os'].unique())

display=st.selectbox("IPS",['No','yes'])

screen_size=st.number_input("Screen Size")

resolution=st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

if st.button('Predict Price'):
    pass

