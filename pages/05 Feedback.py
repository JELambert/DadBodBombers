import streamlit as st
import pandas as pd
from PIL import Image
from utils import *
import streamlit_analytics
import matplotlib.pyplot as plt

@st.cache_data()
def get_dadimage_1():
    image = Image.open('assets/dadbod_3_9_23.jpg')
    return image

def feedback():
    get_file_store()
    streamlit_analytics.start_tracking(firestore_key_file="temp_json.json", firestore_collection_name="feedback")

    st.markdown("### End of Season Feedback")
    with st.sidebar: get_sideBar('Feedback')

    feed = pd.read_excel('./data/Spring23 Survey (Responses).xlsx')
    feed = feed[['Overall Vibes', 'Coaching quality', 'Did you agree with the lineups?', 'Did you agree with where you played in the field?']]

    col1, col2 = st.columns(2)
    with col1:
        st.metric('0=Bad, 10=Best', "Overall Team Vibes", feed['Overall Vibes'].mean(), )
        #feed['Did you agree with the lineups?'].value_counts().plot(kind='barh')
        st.markdown('----------')

        category_counts = feed['Did you agree with the lineups?'].value_counts()
        st.markdown('#### Did you agree with the lineups?')
        # Plot the pie chart
        fig, ax = plt.subplots(figsize=(6,6))
        ax.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%')
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        # Display the chart using Streamlit
        st.pyplot(fig)
        #st.pyplot(feed['Did you agree with where you played in the field?'].value_counts().plot(kind='barh'))
    with col2:
        st.metric('0=Bad, 10=Best', "Coaching Quality", feed['Coaching quality'].mean(), )
        st.markdown('----------')


        category_counts = feed['Did you agree with where you played in the field?'].value_counts()
        st.markdown('#### Did you agree with where you played in the field?')
        # Plot the pie chart
        fig, ax = plt.subplots(figsize=(6,6))
        ax.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%')
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        # Display the chart using Streamlit
        st.pyplot(fig)


    st.markdown('----------')
    st.markdown("#### Open response feedback")
    openresponse = Image.open('assets/wordcloud.png')

    st.image(openresponse)

    st.markdown('----------')


    streamlit_analytics.stop_tracking(firestore_key_file="temp_json.json", firestore_collection_name="feedback")
    delete_file_store()
if __name__ == "__main__":
    feedback()
