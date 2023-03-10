import streamlit as st
import pandas as pd
import os
import random
import datetime
import json
from PIL import Image

from google.oauth2 import service_account
from gsheetsdb import connect
import gspread

from Home import get_data

credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ],
)

client = gspread.authorize(credentials)

@st.cache_data()
def get_image():
    image = Image.open('assets/logo.png')
    return image



@st.cache_data()
def batting_average(df):
    df.fillna(0, inplace=True)
    df.replace('', 0, inplace=True)
    df[['atbats', 'walks', 'single', 'double', 'triple', 'homerun']] = df[['atbats', 'walks', 'single', 'double', 'triple', 'homerun']].astype(int)
    df['batting_average'] = (df['single'] + df['double'] + df['triple'] + df['homerun'])  / (df['atbats'] - df['walks']) * (1000)
    df['hits'] = df['single'] + df['double'] + df['triple'] + df['homerun']
    df['onbase'] = (df['hits'] + df['walks']) / df['atbats'] * (1000)
    df['slugging'] = (df['single'] + (2 * df['double']) + (3 * df['triple']) + (4 * df['homerun'])) / df['atbats'] * (1000)
    df['onbase_plus_slugging'] = df['onbase'] + df['slugging']
    df['total_bases'] = df['single'] + (2 * df['double']) + (3 * df['triple']) + (4 * df['homerun'])

    return df

def labeler():

    st.markdown("# Dad Bod Bombers")
    st.markdown("--------")

    project_id = 'dadbod_3_9_23'
    df = get_data(project_id)
    df = batting_average(df)
            
    with st.sidebar:
        st.sidebar.title('Player Stats')

        image = Image.open('assets/logo.png')
        st.image(image)


    
    player = st.selectbox('Select a player', sorted(df['name'].unique()))


    df = df[df['name'] == player]

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("Player Batting Average:")
        st.write(df['batting_average'].astype(int).mean())
        
        st.markdown('')
        st.markdown('Player Runs Scored:')
        st.write(df['run'].astype(int).sum())
        
        st.markdown('')

        st.markdown('Player Hits:')
        st.write(df['hits'].astype(int).sum())

        st.markdown('')

        st.markdown("Player On Base Percentage:")
        st.write(df['onbase'].astype(int).mean())
        
        st.markdown('')

        st.markdown("Player Slugging Percentage:")
        st.write(df['slugging'].astype(int).mean())
    with col2:

        st.markdown('Player RBI:')    
        st.write(df['rbi'].astype(int).sum())

        st.markdown('')

        st.markdown('Player HR:')
        st.write(df['homerun'].astype(int).sum())

        st.markdown('')

        st.markdown('Player Triples:')
        st.write(df['triple'].astype(int).sum())

        st.markdown('')

        st.markdown('Player Doubles:')
        st.write(df['double'].astype(int).sum())

        st.markdown('')

        st.markdown('Player Singles:')
        st.write(df['single'].astype(int).sum())

    #st.write(df)    


if __name__ == "__main__":
    labeler()
