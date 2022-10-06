import streamlit as st 
import pandas as pd
from PIL import Image

st.title('Curva de Phillips')

st.write(''' Aquí se encuentran los datos del IPC, desempleo, inflación y variación de la inflación para el periodo de 1948 - 2017. By: Gerardo pardo & Juan Bohórquez ''')
image1 = Image.open('Curva de Phillips (1948-1970).png')
image2 = Image.open('Curva de Phillips (1971-2017).png')
image11 = Image.open('Curva de Phillips (1948-1970) (1).png')
image22 = Image.open('Curva de Phillips (1971-2017) (1).png')

datos = pd.read_csv('UNRATE - MENSUAL.csv')
datos1 = pd.read_csv('CPIAUCSL MENSUAL.csv')

datos.rename(columns={'DATE':'fecha', 'UNRATE':'desempleo'}, inplace = True)
datos1.rename(columns={'DATE':'fecha','CPIAUCSL':'IPC'}, inplace = True)

datos['IPC']=datos1['IPC']

a = []
for i in range(0,840):
  if type(datos['IPC'][i]) == str:
    datos['IPC'][i] = float(datos['IPC'][i])

b = []
for i in range(0,840):
  if type(datos['desempleo'][i]) == str:
    datos['desempleo'][i] = float(datos['desempleo'][i])


datos1 = datos1[:70]

d = []
for i in range(11,840, 12):
  d.append(datos['fecha'][i])
datos1['fecha']=d
s = []
for i in range(11,840, 12):
  s.append(datos['IPC'][i])
datos1['IPC']=s
f = []
for i in range(11,840, 12):
  f.append(datos['desempleo'][i])
datos1['desempleo']=f

count = 0
inflacion = []

for i in datos1['IPC']:
  count += 1
  if count <= 69:
    inflacion.append(((datos1['IPC'][count]-datos1['IPC'][count-1])/(datos1['IPC'][count-1]))*100)
if len(inflacion) < 70:
  inflacion.insert(0,0)
datos1['inflacion']=inflacion

count = 0
var_inf= []
for j in datos1['inflacion']:
  count += 1
  if count <= 69:
    var_inf.append(datos1['inflacion'][count]-datos1['inflacion'][count-1])
if len(var_inf) < 70:
  var_inf.insert(0,0)
datos1['var_inf']=var_inf


st.table(datos1)

st.image(image11)
st.image(image1)
st.image(image22)
st.image(image2)