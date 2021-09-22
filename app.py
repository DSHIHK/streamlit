import streamlit as st
import numpy as np
import pandas as pd
st.title("Darryl's Web App")
st.write("Not gonna lie, haven't done coding in a hell long time. I'm probably going to screw this up... big time")
with st.form(key='my_form'):
    text_input = st.text_input(label='Enter your name')
    submit_button = st.form_submit_button(label='Submit')