import streamlit as st
import pandas as pd
import math
from pathlib import Path

st.title("model testing")
engine_size=st.number_input('engine_size',min_value=0,max_value=10,value=1)
clylinder=st.number_input('clylinder',min_value=0,max_value=10,value=1)
fuelcompution=st.number_input('fuelcompution',min_value=0,max_value=10,value=1)

                            

