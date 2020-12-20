import streamlit as st
from pathlib import Path

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

def app():
    st.title('Skills and work history')


    intro_markdown = read_markdown_file("/home/henri/Documents/Post Lighthouse-Lab work/streamlitWebsiteCVProject/src/cv.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)

    