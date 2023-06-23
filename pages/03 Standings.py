import streamlit as st
import pandas as pd
from PIL import Image
from utils import *

@st.cache_data()
def get_dadimage_1():
    image = Image.open('assets/dadbod_3_9_23.jpg')
    return image

def standings():
    with st.sidebar: get_sideBar('Standings Page')

    st.markdown('# SEASON 2 - (1-1)')
    st.write("### Game 9 - 6/22/2023")
    col1, col2 = st.columns(2)
    with col1:
        st.metric('Away', "Dad Bod Bombers", -8)
    with col2:
        st.metric('Home', "T.O.P.E", 9, )
    with st.expander("See the evidence:"):
        st.markdown('NO evidence of losses')
    st.markdown("--------")

    st.write("### Game 8 - 6/15/2023")
    col1, col2 = st.columns(2)
    with col1:
        st.metric('Away', "Dad Bod Bombers", -3)
    with col2:
        st.metric('Home', "Dr. Unks", 13, )
    with st.expander("See the evidence:"):
        st.markdown('NO evidence of losses')
    st.markdown("--------")

    st.write("### Game 7 - 6/8/2023")
    col1, col2 = st.columns(2)
    with col1:
        st.metric('Away', "Pitch Slaps", -4)
    with col2:
        st.metric('Home', "Dad Bod Bombers", 17, )
    with st.expander("See the evidence:"):
        video_file = open('assets/dadbod_6_8_23.mov', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)    
    st.markdown("--------")



    st.markdown('')
    st.markdown("-------")
    st.markdown('# SEASON 1 (1-6)')
    st.markdown('')
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
