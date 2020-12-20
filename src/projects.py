import streamlit as st

import sys
sys.path.append('/home/henri/Documents/Post Lighthouse-Lab work/streamlitWebsiteCVProject/projects')
from customPandas import *

def app():
    st.header('Completed Work')
    st.subheader("Paper written")
    st.markdown('[Using Scrapy from beginner to advanced topics](https://github.com/Vanderscycle/lighthouse-data-notes/blob/master/paper/paper/HowToGetDataDraft.md)')