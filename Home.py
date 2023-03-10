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
def get_dadimage_1():
    image = Image.open('assets/dadbod_3_9_23.jpg')
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
    st.markdown("### Team Leaders")

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("#### Singles")
        singles = df.loc[df.single>0].sort_values(by=['single'], ascending=False).head(5)[['name', 'single']]
        st.write(singles)

    with c2:
        st.markdown("#### Doubles")
        doubles = df.loc[df.double>0].sort_values(by=['double'], ascending=False).head(5)[['name', 'double']]
        st.write(doubles)
    with c3:
        st.markdown("#### Triples")
        triples = df.loc[df.triple>0].sort_values(by=['triple'], ascending=False).head(5)[['name', 'triple']]
        st.write(triples)
    with c4:
        st.markdown("#### Homeruns")
        homers = df.loc[df.homerun>0].sort_values(by=['homerun'], ascending=False).head(5)[['name', 'homerun']]
        st.write(homers)

    st.markdown("--------")
    cl1, cl2, cl3, cl4 = st.columns(4)
    with cl1:
        st.markdown("#### Batting Average")
        baframe = df.sort_values(by=['batting_average'], ascending=False).head(5)[['name', 'batting_average']]
        st.write(baframe)
    with cl2:
        st.markdown("#### On Base %")
        onbase = df.sort_values(by=['onbase'], ascending=False).head(5)[['name', 'onbase']]
        st.write(onbase)
    with cl3:
        st.markdown("#### Runs")
        runs = df.sort_values(by=['run'], ascending=False).head(5)[['name', 'run']]
        st.write(runs)
    with cl4:
        st.markdown("#### RBI")
        rbi = df.sort_values(by=['rbi'], ascending=False).head(5)[['name', 'rbi']]
        st.write(rbi)


    st.markdown("-------")
    st.write("### Game 1 - 3/9/2021")
    col1, col2 = st.columns(2)
    with col1:
        st.metric('Away', "Dad Bod Bombers", 21, )
    with col2:
        st.metric('Home', "Dr. Unks", -8)
    with st.expander("See the evidence:"):
        evidence1 = get_dadimage_1()
        st.image(evidence1)
    st.markdown("--------")



if __name__ == "__main__":
    labeler()
