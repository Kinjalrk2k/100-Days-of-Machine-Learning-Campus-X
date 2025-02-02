import streamlit as st
import pickle

clf = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="Placement Predictor")
st.title("Placement Predictor")

col1, col2 = st.columns(2)

with col1:
    cgpa = st.slider("CGPA", min_value=0.0, max_value=10.0, step=0.01)

with col2:
    iq = st.number_input("IQ", step=1)

submit = st.button("Predict")

if submit:
    result = clf.predict([[cgpa, iq]])
    if result[0] == 1:
        st.write("Placement Ho Jayega")
    else:
        st.write("Placement Nahi Hoga")
