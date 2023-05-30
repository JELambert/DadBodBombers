import streamlit as st
import pandas as pd
import os
from PIL import Image

@st.cache_data()
def get_dadimage_1():
    image = Image.open('assets/dadbod_3_9_23.jpg')
    return image

@st.cache_resource()
def get_sideBar(title):
    st.sidebar.title(title)
    image = get_image()
    st.image(image)
    st.markdown("## [Click here for Schedule](https://teamsideline.com/sites/georgetown/schedule/450570/2680885/0/Dad-Bod-Bombers)")
    st.markdown("")
    st.markdown('## [Click here for Budget](https://docs.google.com/spreadsheets/d/1AYZyMQNMqUqAaN0m9aw4U5Uc73Vi5PNcn7pKeOcFMOg/edit?usp=sharing)')

@st.cache_data()
def get_image():
    image = Image.open('assets/logo.png')
    return image

def standings():
    with st.sidebar: get_sideBar('Standings Page')

    st.markdown("-------")
    st.write("### Game 1 - 3/9/2023")
    col1, col2 = st.columns(2)
    with col1:
        st.metric('Away', "Dad Bod Bombers", 21, )
    with col2:
        st.metric('Home', "Dr. Unks", -8)
    with st.expander("See the evidence:"):
        evidence1 = get_dadimage_1()
        st.image(evidence1)
    st.markdown("--------")

    st.write("### Game 2 - 3/30/2023")
    col1, col2 = st.columns(2)
    with col1:
        st.metric('Away', "Dad Bod Bombers", -15, )
    with col2:
        st.metric('Home', "Team Ramrod", 16)
    with st.expander("See the evidence:"):
        st.markdown('NO evidence of losses')
    st.markdown("--------")

    

    st.write("### Game 3 - 4/13/2023")
    col1, col2 = st.columns(2)
    with col1:
        st.metric('Away', "Mad Lads", 22, )
    with col2:
        st.metric('Home', "Dad Bod Bombers", -11)
    with st.expander("See the evidence:"):
        st.markdown('NO evidence of losses')
    st.markdown("--------")


    st.write("### Game 4 - 4/27/2023")
    col1, col2 = st.columns(2)
    with col1:
        st.metric('Away', "Coors Inc.", 16, )
    with col2:
        st.metric('Home', "Dad Bod Bombers", -5)
    with st.expander("See the evidence:"):
        st.markdown('NO evidence of losses')
    st.markdown("--------")



    st.write("### Game 5a - 5/4/2023 -- Score Unexact")
    col1, col2 = st.columns(2)
    with col1:
        st.metric('Away', "Ramrod", 14, )
    with col2:
        st.metric('Home', "Dad Bod Bombers", -13)
    with st.expander("See the evidence:"):
        st.markdown('NO evidence of losses')
    st.markdown("--------")


    st.write("### Game 5b - 5/4/2023 -- Score Unexact")
    col1, col2 = st.columns(2)
    with col1:
        st.metric('Away', "Ramrod", 14, )
    with col2:
        st.metric('Home', "Dad Bod Bombers", -13)
    with st.expander("See the evidence:"):
        st.markdown('NO evidence of losses')
    st.markdown("--------")
if __name__ == "__main__":
    standings()
