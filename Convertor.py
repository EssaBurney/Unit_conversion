import streamlit as st

# Title & Description
st.title("♻️ Unit Converting Application")
st.markdown("### Converts Length, Weight, and Time (Up to Years)")
st.write("Select a category, choose a unit conversion, enter a value, and get the result instantly.")

# Unit Conversion Logic
def convert_units(category, value, unit):
    category = category.lower()

    if category == "length":
        if unit == "Meters to Kilometers":
            return value / 1000
        elif unit == "Kilometers to Meters":
            return value * 1000
        elif unit == "Meters to Miles":
            return value * 0.000621371
        elif unit == "Miles to Meters":
            return value / 0.000621371
        elif unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371

    elif category == "weight":
        if unit == "Grams to Kilograms":
            return value / 1000
        elif unit == "Kilograms to Grams":
            return value * 1000
        elif unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462
        elif unit == "Grams to Pounds":
            return value * 0.00220462
        elif unit == "Pounds to Grams":
            return value / 0.00220462

    elif category == "time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24
        elif unit == "Days to Years":
            return value / 365
        elif unit == "Years to Days":
            return value * 365
        elif unit == "Seconds to Days":
            return value / 86400
        elif unit == "Seconds to Years":
            return value / 31536000
        elif unit == "Years to Seconds":
            return value * 31536000

# Category Selection
category = st.selectbox("Select a category", ["None", "Length", "Weight", "Time"])

# Unit Options
unit = None
if category == "Length":
    unit = st.selectbox("Select conversion", ["Meters to Kilometers", "Kilometers to Meters","Meters to Miles", "Miles to Meters","Kilometers to Miles", "Miles to Kilometers"])

elif category == "Weight":
    unit = st.selectbox("Select conversion", ["Grams to Kilograms", "Kilograms to Grams","Kilograms to Pounds", "Pounds to Kilograms","Grams to Pounds", "Pounds to Grams"])

elif category == "Time":
    unit = st.selectbox("Select conversion", ["Seconds to Minutes", "Minutes to Seconds","Minutes to Hours", "Hours to Minutes","Hours to Days", "Days to Hours","Days to Years", "Years to Days","Seconds to Days", "Seconds to Years", "Years to Seconds"])

# Value Input & Result
if category != "None" and unit:
    value = st.number_input("Enter the value to convert", step=0.01)
    if st.button("Convert"):
        result = convert_units(category, value, unit)
        if result is not None:
            st.success(f"The result is: {result:.5f}")
        else:
            st.error("Conversion failed. Please check your input.")
