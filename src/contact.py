import streamlit as st
from PIL import Image

import sys, os
lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../images'))
sys.path.append(lib_path)
#print(lib_path)
def app():
    # Online footprint
    # Not the most beautiful wayto list
    st.subheader('Find me')
    st.markdown('[Github](https://github.com/Vanderscycle)')
    st.markdown('[Linkdin](https://www.linkedin.com/in/henri-vandersleyen-a25a8312b/)')
    # traditional 
    st.subheader('Contact me')
    st.markdown('[Email](hvandersleyen@gmail.com)')
    st.write('Phone: 1 250 886 5099')
    st.write('Home city: Victoria, BC, Canada')
    
    image = Image.open(f'{lib_path}/bio.jpg')
    st.image(image, caption='When not coding or learning, I spend time with my lovely wife savoring coffee',use_column_width=True)