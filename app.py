import pandas as pd
import plotly.express as px
import streamlit as st
import pickle as pkl
import numpy as np

wage = pd.read_csv('wage.csv')
 
 
st.title("Salario esperado")
 
with open("model.pickle", "rb") as m:
    modelo = pkl.load(m)
 
Tab1, Tab2, Tab3 = st.tabs(['Analisis Univariado', 'Analisis Bivariado', 'Modelo'])
 
with Tab1:
   st.subheader("Estadísticas descriptivas - Variables numéricas")
   st.dataframe(wage[['salario_prom', 'educ', 'exper', 'permanencia']].describe())
 
   st.subheader("Distribución de variables numéricas")
 
   fig = px.histogram(wage, x='salario_prom')
   st.plotly_chart(fig)
 
   fig2 = px.histogram(wage, x='educ')
   st.plotly_chart(fig2)
 
   fig3 = px.histogram(wage, x='exper')
   st.plotly_chart(fig3)
 
   fig4 = px.histogram(wage, x='permanencia')
   st.plotly_chart(fig4)

   st.subheader("Frecuencias - Variables categóricas")
   
   st.write("Género")
   st.dataframe(wage['genero'].value_counts())
 
   st.write("Estado civil")
   st.dataframe(wage['estadocivil'].value_counts())
 
   st.subheader("Distribución de variables categóricas")
 
   fig5 = px.histogram(wage, x='genero')
   st.plotly_chart(fig5)
 
   fig6 = px.histogram(wage, x='estadocivil')
   st.plotly_chart(fig6)
 
 
 
with Tab2:
    st.subheader("Relación entre variables y salario")

    fig1 = px.scatter(wage, x='educ', y='salario_prom', title='Educación vs Salario')
    st.plotly_chart(fig1)

    fig2 = px.scatter(wage, x='exper', y='salario_prom', title='Experiencia vs Salario')
    st.plotly_chart(fig2)

    fig3 = px.scatter(wage, x='permanencia', y='salario_prom', title='Permanencia vs Salario')
    st.plotly_chart(fig3)

    fig4 = px.box(wage, x='genero', y='salario_prom', title='Salario por Género')
    st.plotly_chart(fig4)

    fig5 = px.box(wage, x='estadocivil', y='salario_prom', title='Salario por Estado Civil')
    st.plotly_chart(fig5)

 
with Tab3:
    st.title("Modelo")
 
    educ = st.slider("Años de educación", 0, 18)
 
    exper = st.slider("Años de experiencia", 1, 51)
 
    Permanencia= st.slider("Años en la empresa", 0, 44)
 
    sexo = st.selectbox('genero', ['mujer', 'hombre'])
 
    if sexo == 'mujer':
        sexo = 1
    else:
        sexo = 0
 
    Estado_civil = st.selectbox('estadocivil', ['casado', 'soltero'])
 
    if Estado_civil == 'casado':
        Estado_civil = 1
    else:
        Estado_civil = 0
 
    if st.button ("Predecir"):
        Predecir = modelo.predict(np.array([[educ, exper, Permanencia, sexo, Estado_civil]]))
        st.write(Predecir [0])
 
print(10)