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
@st.cache_resource()
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

    st.markdown("# Home Page")
    st.markdown("--------")

    with st.sidebar:
        st.sidebar.title('Home Page')

        image = get_image()
        st.image(image)

    project_id = 'dadbod_3_9_23'
    df = get_data(project_id)
    df = batting_average(df)

    st.write("### Game 1 - 3/9/2021")
    st.write("Dad Bod Bombers 21 - 3 Dr. Unks")


if __name__ == "__main__":
    labeler()
