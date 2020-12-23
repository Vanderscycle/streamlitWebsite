import streamlit as st
from pathlib import Path
import sys, os
# not entirely sure why but this work (adding relative path)
lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../ressources'))
sys.path.append(lib_path)
def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

def app():
    st.title('Skills and work history')


    intro_markdown = read_markdown_file(f"{lib_path}/cv.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)

    