import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('electric_vehicle_price_predictor.pkl','rb'))

def app():

    st.markdown('<center><h2>Electric Vehicle Price Prediction</h2></center>', unsafe_allow_html=True)
    st.caption('<center>Enter the Vehicle Details</center>', unsafe_allow_html=True)

    st.text('1 : Battery Electric Vehicle (BEV) & 0 : Plug-in Hybrid Electric Vehicle (PHEV)')
    vehicle_type = st.number_input('Vehicle Type', min_value=0, max_value=10, value=0)
    st.text('1 : Clean Alternative Fuel Vehicle Eligible & 2 : Not eligible due to low battery range & 0 : Eligibility unknown as battery range has not been researched')
    cafv_eligibility = st.number_input('CAFE Eligibility', min_value=0, max_value=10, value=0)
    e_range = st.number_input('Electric Range', min_value=0, max_value=500, value=0)
    msrp = st.number_input('Base MSRP', min_value=0, max_value=1000000, value=0)
    legislative_district = st.number_input('Legislative District', min_value=0, max_value=100, value=0)
    year = st.number_input('Year', min_value=0, max_value=2030, value=2023)

    if st.button('Predict'):
        input_point = np.array([[vehicle_type, cafv_eligibility, e_range, msrp, legislative_district, year]])
        prediction = model.predict(input_point)[0]

        st.caption('Vehicle Predict Price {}'.format('$' + str(prediction)))

if __name__ == '__main__':
    app()
