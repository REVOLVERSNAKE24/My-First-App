import streamlit as st
import pandas as pd
st.title("My First App")
click = st.button ("Inicio") 
st.write ("ES VERDAD O FALSO", click)

if click== True:
    st.image("images.png")

#with st.sidebar:
num1 = st.slider('Elige un Numero', 0, 200, 25)
num2 = st.slider('Elige un Numero 2', 0, 200, 25)
Suma = num1+num2
#st.[num1, num2, Suma]
st.write("La suma de",num1," y  ",num2,"es :",Suma)


st.write("Multiplicamos")
nn1 = st.number_input("Dame n1")
nn2 = st.number_input("Dame n2")

multi = nn1*nn2 
st.write ("La Multiplicacion es",nn1," y ",nn2,"es :",multi)

#st.button ("Seccion 1")

# Estas Lienas fueron para agregar una hoja de calculo y un mapa con datos represntados en puntos y una tabla

#df = pd.read_csv('https://raw.githubusercontent.com/quantum-apps/mapa/main/data.csv')

#st.write(df)

#st.map(df)


#Estos Comandos Sirven Para Dar Estilo A La Escritura Que Demos A La Aplicacion Web!!!
st.text ("Hello World")
st.latex (" \int_1^2")
st.markdown ("#titulo")
st.markdown ("Ayala Valois **_Luis_ Emmanuel.**")