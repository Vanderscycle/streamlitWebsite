import streamlit as st
from PIL import Image

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
    
    image = Image.open('/home/henri/Documents/Post Lighthouse-Lab work/streamlitWebsiteCVProject/images/bio.jpg')
    st.image(image, caption='When not coding or learning, I spend time with my lovely wife savoring coffee',use_column_width=True)