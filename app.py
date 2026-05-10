import streamlit as st

# Page Title
st.set_page_config(page_title="Mechanical Unit Converter", layout="centered")

# Header
st.title("Mechanical Unit Converter and Material Density Checker")

# Student Information
st.markdown("## Student Information")
st.write("**Full Name:** Ahmad Umar")
st.write("**Roll Number:** 75")

st.markdown("---")

# =========================
# UNIT CONVERTER SECTION
# =========================

st.header("Mechanical Unit Converter")

conversion_type = st.selectbox(
    "Select Conversion Type",
    ["Length", "Weight", "Temperature"]
)

# Length Converter
if conversion_type == "Length":
    meter = st.number_input("Enter value in meters", value=0.0)
    centimeter = meter * 100
    millimeter = meter * 1000
    inch = meter * 39.3701

    st.success(f"Centimeters: {centimeter:.2f} cm")
    st.success(f"Millimeters: {millimeter:.2f} mm")
    st.success(f"Inches: {inch:.2f} in")

# Weight Converter
elif conversion_type == "Weight":
    kg = st.number_input("Enter value in kilograms", value=0.0)
    gram = kg * 1000
    pound = kg * 2.20462

    st.success(f"Grams: {gram:.2f} g")
    st.success(f"Pounds: {pound:.2f} lbs")

# Temperature Converter
elif conversion_type == "Temperature":
    celsius = st.number_input("Enter temperature in Celsius", value=0.0)
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15

    st.success(f"Fahrenheit: {fahrenheit:.2f} °F")
    st.success(f"Kelvin: {kelvin:.2f} K")

st.markdown("---")

# =========================
# MATERIAL DENSITY CHECKER
# =========================

st.header("Material Density Checker")

materials = {
    "Steel": 7850,
    "Aluminum": 2700,
    "Copper": 8960,
    "Brass": 8500,
    "Cast Iron": 7200
}

material = st.selectbox("Select Material", list(materials.keys()))

density = materials[material]

st.info(f"Density of {material}: {density} kg/m³")

# Simple Comparison
user_density = st.number_input(
    "Enter your measured density value (kg/m³)",
    value=0.0
)

if user_density > 0:
    difference = abs(user_density - density)

    if difference < 200:
        st.success("The material density is approximately correct.")
    else:
        st.warning("The material density is different from standard value.")

st.markdown("---")
st.caption("Developed using Streamlit")
