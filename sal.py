import streamlit as st
import joblib
import numpy as np

st.title("Salary Prediction Application")

st.divider()

st.write("With this application, you can estimate your salary based on your years of experience.")

years = st.number_input("Enter number of years at the company", value=1, step=1, min_value=0)
jobrate = st.number_input("Enter the Job Rate", value=3.5, step=0.5, min_value=0.0)

x = [years, jobrate]

model = joblib.load("linearmodel.pkl")

st.divider()

predict = st.button("Predict My Salary")

st.divider()

def indian_number_format(number):
    s, *d = str(f"{number:.2f}").partition(".")
    r = s[::-1]
    groups = [r[:3]] + [r[i:i+2] for i in range(3, len(r), 2)]
    return ",".join(groups)[::-1] + "".join(d)

if predict:
    x1 = np.array([x])
    prediction = float(model.predict(x1)[0])
    st.write(f"Based on your experience, we estimate your salary to be: ₹{indian_number_format(prediction)}")
else:
    st.write("")
