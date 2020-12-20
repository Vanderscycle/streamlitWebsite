import streamlit as st
import sys
sys.path.append('/home/henri/Documents/Post Lighthouse-Lab work/streamlitWebsiteCVProject/projects')
#if the file was in the same location as this one we don't need to append the path
from customPandas import *
#importing pages
import cv
import projects
import contact


def helloworld():
    st.title('Henri Vandersleyen, P.eng')
    #
    PAGES = {
        "Project showcase": projects,
        "Skills and Work History": cv,
        "Contact me": contact
    }
    # sidebar
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page.app()




if __name__ == "__main__":
    helloworld()