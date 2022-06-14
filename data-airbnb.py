import streamlit as st
import pandas as pd
import numpy as np
from csv import reader

@st.cache
def get_data(listatotal):
  with open('calendar.csv', 'r') as df:
      
      csv_reader = reader(df)
      
      lista = list(csv_reader)
      
      for alojamiento in lista:
          listatotal.append(alojamiento)

def tiene_alojamiento_enfecha(alojamiento, fecha):
    return alojamiento[1] == fecha

def esta_ocupado(alojamiento):
    return alojamiento[2] == "t"
                    
def filter_añonuevo_abiertos(total, listaabiertos):
    for alojamiento in total:
        if tiene_alojamiento_enfecha(alojamiento, "2022-12-31"):
            listaabiertos.append(alojamiento)

def filter_ocupados_añonuevo(alojamientosañonuevo, alojamientosocupadosañonuevo):
    for alojamiento in alojamientosañonuevo:
        if esta_ocupado(alojamiento):
            alojamientosocupadosañonuevo.append(alojamiento)
    
    
def promedio_abiertos_añonuevo(totalalojamientos, alojamientosañonuevo):
    return ((alojamientosañonuevo * 100) / totalalojamientos)

def promedio_ocupados_añonuevo(alojamientosañonuevo, alojamientosocupadosañonuevo):
    return ((alojamientosocupadosañonuevo * 100) / alojamientosañonuevo)

def show_dataframe(option, listageneral):
    mostrarendataframe = listageneral[2]
    
    if option == 'New Year':
        mostrarendataframe = listageneral[2]
    else:
        mostrarendataframe = mostrarendataframe
    
    st.dataframe(mostrarendataframe)        

def main():
        
    totalalojamientos = []
    
    alojamientosañonuevo = []
    
    alojamientosocupadosañonuevo = []
    
    get_data(totalalojamientos)
    
    filter_añonuevo_abiertos(totalalojamientos, alojamientosañonuevo)
    
    filter_ocupados_añonuevo(alojamientosañonuevo, alojamientosocupadosañonuevo)
    
    listageneral = [totalalojamientos, alojamientosañonuevo, alojamientosocupadosañonuevo]
    
    option = st.selectbox(
     'Day:',
     ('New Year', 'Christmas'))
    
    st.write('You selected:', option)
    
    show_dataframe(option, listageneral)
    
    
main()

  
                 
                 
                 
                 
