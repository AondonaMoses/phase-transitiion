# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 13:25:54 2022

@author: -
"""

import numpy as np
import streamlit as st
import pickle



def predictionModel(input_data, model):
    input_data_as_array = np.asarray(input_data)
    input_data_reshape = input_data_as_array.reshape(1, -1)
    prediction = model.predict(input_data_reshape)
    
    if (prediction[0] == 0):
        return "Critical"
    elif (prediction[0] == 1):
        return "Ferromagnetic"
    else:
        return "Paramagnetic"


def main():
    st.title("Phase Transition APP")
    loaded_model = pickle.load(open("tree_phase_model.sav", "rb"))
    
    temp = st.text_input("**Temperature**")
    mag = st.text_input("**Magnetization**")
    
    phase = ""
    
    features = [temp, mag]
    if st.button("RUN TEST"):
        phase = predictionModel(features, loaded_model)
        st.write(phase, "Phase")
    



if __name__ == "__main__":
    main()

