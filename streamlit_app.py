import streamlit as st
import pandas as pd
import joblib

model = joblib.load('model.pkl')
quality= ['Low','Medium','High']

st.markdown("<h1 style='text-align: center;'>Predictive Maintenance Centre</h1>", unsafe_allow_html=True)

st.write('Enter the required information to get the prediction about machine status.')

quality_type = st.selectbox('Product Quality',quality)
air_temp = st.number_input('Air Temperature',min_value=0.0,step=1.1)
process_temp = st.number_input('Process Temperature',min_value=0.0,step=1.1)
speed = st.number_input('Rotational Speed (rpm)',min_value=0.0,step=1.0)
torque = st.number_input('Torque',min_value=0.0,step=1.1)
tool = st.number_input('Tool Wear Time (min)',min_value=0.0,step=1.0)

if st.button('Submit'):
    if quality_type=='Low':
        quality_type= 0
    elif quality_type=='Medium':
        quality_type=1
    else:
        quality_type=2

    user_input = pd.DataFrame({
        'Type': [quality_type],
        'Air temperature': [air_temp],
        'Process temperature': [process_temp],
        'Rotational speed': [speed],
        'Torque': [torque],
        'Tool wear':[tool]
        })
    
    prediction = model.predict(user_input)
    if prediction==0:
        st.write('Normal Operation')
    elif prediction==1:
        st.write('Tool Wear Failure')
    elif prediction==2:
        st.write('Heat Dissipation Failure')
    elif prediction==3:
        st.write('Power Failure')
    elif prediction==4:
        st.write('Overstrain Failure')
    elif prediction==5:
        st.write('Other Failure (Random)')

    
    
