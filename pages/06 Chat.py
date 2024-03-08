import streamlit as st
import pandas as pd
from PIL import Image
from utils import *

import os
os.environ['OPENAI_API_KEY'] = st.secrets['openai_key']

#from llama_index.llms.openai import OpenAI
#from llama_index.core.query_engine import PandasQueryEngine
from llama_index.core import Document
from llama_index.core import VectorStoreIndex

import re

from utils import data_munging, add_cumulative_stats



import streamlit as st
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Set up credentials
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/drive.readonly",
        "https://www.googleapis.com/auth/spreadsheets.readonly"
    ]
)

# Use the Drive API
service = build('drive', 'v3', credentials=credentials)

def return_markdown(filepath):
    with open(filepath, 'r') as file:
        content = file.read()
    # Split the content on 'SKIPABOVE' and get everything below it
    _, content_to_display = content.split('SKIPABOVE', 1)
    # Display it in Streamlit
    return content_to_display

def return_google_markdown(file_id):
    request = service.files().get_media(fileId=file_id)
    content = request.execute()
    _, content_to_display = content.decode("utf-8").split('SKIPABOVE', 1)
    return content_to_display


@st.cache_data()
def make_doc_index():

    users = ['Beep', 'Tyler', 'LambertDBB', 'Grace', 'Ben', 'Forrest','Spangler',
                    'Sweet', 'Cody',  'Niko',  'Dan', 'Renzo', 'Sean', 'Shack', 'Frank',
                    'Blake', 'Todd', 'Taylor', 'Connor']

    emails = [st.secrets[x]['email'] for x in users]
    fileIds = [st.secrets[x]['fileid'] for x in users]
    emails_ids = dict(zip(users, zip(emails, fileIds)))
    return_google_markdown(emails_ids['Beep'][1])

    documents = []
    for k in emails_ids.keys():

        text = return_google_markdown(emails_ids[k][1])
        cleaned_text = re.sub(r'\n+', ' ', text)  # Remove multiple consecutive newlines
        cleaned_text = re.sub(r'#+\s*', '', cleaned_text)  # Remove hash symbols and spaces at the beginning of the line

        document = Document(
            text=cleaned_text,
            metadata={"filename": emails_ids[k][1], "category": "coachnotes", "person": k}
        )
        documents.append(document)


    extras = { 'battingPhilosophy': 'assets/docs/Batting Order Philosophy.md',
                'battingJustification': 'assets/docs/Batting Order Justification.md',
                'fieldingPhilosophy': 'assets/docs/Fielding Philosophy.md',
                'fieldingJustification': 'assets/docs/Fielding Justification.md',
                'baserunningPhilosophy': 'assets/docs/Baserunning Philosophy.md'
        }


    for k in extras.keys():
        text = return_markdown(extras[k])
        cleaned_text = re.sub(r'\n+', ' ', text)  # Remove multiple consecutive newlines
        cleaned_text = re.sub(r'#+\s*', '', cleaned_text)  # Remove hash symbols and spaces at the beginning of the line

        document = Document(
            text=cleaned_text,
            metadata={"filename": k, "category": "philosophy", "name": k}
        )
        documents.append(document)
    vector_index = VectorStoreIndex.from_documents(documents)
    return vector_index

@st.cache_data()
def get_dadimage_1():
    image = Image.open('assets/dadbod_3_9_23.jpg')
    return image

def chat():

    st.markdown("# Chat")
    #df_full, df_full_nums = data_munging()
    #df_agg = df_full.groupby(['id', 'name'])[['atbats', 'run', 'rbi', 'walks', 'single', 'double', 'triple', 'homerun', 'games_played']].sum().reset_index()

    #df = add_cumulative_stats(df_agg)
    
    vector_index = make_doc_index()
    coachnotes = vector_index.as_query_engine()
    with st.sidebar: get_sideBar('Team Stats')

    #llm = OpenAI(api_key= st.secrets.openai_key)

    if "messages" not in st.session_state.keys():
        st.session_state.messages = [
            {"role":"assistant", "content":"Hello! I'm the assistant here to analyze baseball data and coach's notes. What can I help you with today?"}
        ]
    #query_engine = PandasQueryEngine(df=df, verbose=True)

    if prompt:= st.chat_input("Ask a question"):
        st.session_state.messages.append({"role":"user", "content": prompt})

    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.write(message['content'])
    
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = coachnotes.query(prompt)
                st.write(response.response)
                message = {"role":"assistant", "content": response.response}
                st.session_state.messages.append(message)
    
    # response = query_engine.query(
    #     "What is Josh's batting average?",
    # )

    #st.write(response)
if __name__ == "__main__":
    chat()
