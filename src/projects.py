import streamlit as st
import sys, os
lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../projects'))
sys.path.append(lib_path)

def app():
    st.header('Completed Work')
    st.subheader("Paper written")
    st.markdown('[Using Scrapy from beginner to advanced topics](https://github.com/Vanderscycle/lighthouse-data-notes/blob/master/paper/paper/HowToGetDataDraft.md)')