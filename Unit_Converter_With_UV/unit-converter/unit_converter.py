import streamlit as st

def convert_units(value, from_unit, to_unit):

    conversions = {
        "meter_kilometer": 0.001, # meter = 0.001 kilometer
        "kilometer_meter" : 1000, # kilometer = 1000 meter
        "gram_kilogram": 0.001, # gram = 0.001 kilogram
        "kilogram_gram" : 1000, # kilogram = 1000 gram
    }

    key = f"{from_unit}_{to_unit}" # generate a key based on input and output units
     
    if key in conversions:
       conversion = conversions[key]
       return value * conversion
    else:
        return "Conversion not supported"
    
st.title("Unit Converter")

value = st.number_input("Enter the value", min_value=1.0, step=1.0)
from_unit = st.selectbox("Convert from", ["meter", "kilometer", "gram", "kilogram"])
to_unit = st.selectbox("Convert to", ["meter", "kilometer", "gram", "kilogram"])

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit)
    st.write(f"Converted value: {result}")