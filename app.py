import streamlit as st 

# Streamlit widgets
st.title('Power Calculator')
st.write('Enter the values to calculate power')

# Input widgets
n = st.number_input('Enter the value of n', value=1, step=1)

# Calculate power
square = n ** 2
cube = n ** 3   
fifth_power = n ** 5

# Display the result
st.write(f'Square of {n} is {square}')  
st.write(f'Cube of {n} is {cube}')
st.write(f'Fifth power of {n} is {fifth_power}')


