import streamlit as st
import numpy as np

paginas = [
    st.Page("src/atv1.py", title = "Atv 1"),
    st.Page("src/atv2.py", title = "Atv 2"),
]

st.navigation(paginas).run()