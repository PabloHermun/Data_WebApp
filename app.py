import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header("About our cars") # Create a header

hist_button = st.button('Build histogram') # crear un botón

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creating a histogram of the on-sale cars based on their mileage')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


scat_button = st.button('Build scatter plot') # create a button

if scat_button:
    # Write a message
    st.write('Creating a scatter plot of the cars\' mileage and price')

    # Create a scatter plot
    fig2 = px.scatter(car_data, x="odometer", y="price") 

    # Show an interactive Plotly plot
    st.plotly_chart(fig2, config={"responsive": True})