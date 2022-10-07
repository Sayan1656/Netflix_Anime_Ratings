from pathlib import Path  # Python Standard Library
import xlwings as xw  # pip install xlwings
import streamlit as st
import pandas as pd
import os
import plotly_express as px

pwd=os.getcwd()
df=pd.read_excel(pwd+'\\Data_clean.xlsx').astype(str)
st.dataframe(df)