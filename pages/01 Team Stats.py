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



st.set_page_config(layout="wide")

credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ],
)

client = gspread.authorize(credentials)
@st.cache_data()
def get_data(project_id):
    sheet = client.open(project_id).sheet1
    dataframe = pd.DataFrame(sheet.get_all_records())
    return dataframe

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

    st.markdown("# Team Stats")
    st.markdown("--------")


    project_id = 'dadbod_3_9_23'
    df = get_data(project_id)

            
    with st.sidebar:
        st.sidebar.title('Team Stats')
        image = get_image()
        st.image(image)

    project_id = 'dadbod_3_9_23'

    
    df = get_data(project_id)
    #st.write(df)    


    df = batting_average(df)



    col1, col2 = st.columns(2)
    with col1:
        st.markdown("Team Batting Average:")
        st.write(df['batting_average'].astype(int).mean())
        
        st.markdown('')
        st.markdown('Team Runs Scored:')
        st.write(df['run'].astype(int).sum())
        
        st.markdown('')

        st.markdown('Team Hits:')
        st.write(df['hits'].astype(int).sum())

        st.markdown('')

        st.markdown("Team On Base Percentage:")
        st.write(df['onbase'].astype(int).mean())
        
        st.markdown('')

        st.markdown("Team Slugging Percentage:")
        st.write(df['slugging'].astype(int).mean())
    with col2:

        st.markdown('Team RBI:')    
        st.write(df['rbi'].astype(int).sum())

        st.markdown('')

        st.markdown('Team HR:')
        st.write(df['homerun'].astype(int).sum())

        st.markdown('')

        st.markdown('Team Triples:')
        st.write(df['triple'].astype(int).sum())

        st.markdown('')

        st.markdown('Team Doubles:')
        st.write(df['double'].astype(int).sum())

        st.markdown('')

        st.markdown('Team Singles:')
        st.write(df['single'].astype(int).sum())

if __name__ == "__main__":
    labeler()
