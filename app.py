import streamlit as st
import streamlit.components.v1 as components

st.title("Análisis de Trauma")

with open("fig1.html", "r") as f:
    grafica1 = f.read()

with open("fig2.html", "r") as f:
    grafica2 = f.read()

with open("fig3.html", "r") as f:
    grafica3 = f.read()

with open("fig4.html", "r") as f:
    grafica4 = f.read()
    
with open("fig5.html", "r") as f:
    grafica5 = f.read()
    
with open("fig6.html", "r") as f:
    grafica6 = f.read()

with open("fig8.html", "r") as f:
    grafica8 = f.read()
    
with open("fig9.html", "r") as f:
    grafica9 = f.read()
    
with open("fig10.html", "r") as f:
    grafica10 = f.read()
    
with open("fig12.html", "r") as f:
    grafica12 = f.read()
    
contenedor_unido = f"""
<div style="display: flex; flex-direction: column; gap: 10px;">
    <div>{grafica1}</div>
    <div>{grafica2}</div>
    <div>{grafica3}</div>
    <div>{grafica4}</div>
    <div>{grafica5}</div>
    <div>{grafica6}</div>
    <div>{grafica8}</div>
    <div>{grafica9}</div>
    <div>{grafica10}</div>
    <div>{grafica12}</div>
</div>
"""

components.html(contenedor_unido, height=4800)
