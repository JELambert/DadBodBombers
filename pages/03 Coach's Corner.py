import streamlit as st
from utils import *
#import streamlit_analytics
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

def coaching():
    #get_file_store()
    #streamlit_analytics.start_tracking(firestore_key_file="temp_json.json", firestore_collection_name="coach")

    st.markdown("# Coach's Corner")
    with st.sidebar: get_sideBar("Coach's Corner")

    st.markdown("* This will serve as our wiki for coaching philsophy, decisions, and feedback.")
    st.markdown("* Caveat: If you have strong thoughts and opinions let them be heard and we will figure it out. This is just a starting point, but I think it's important to be transparent. I will try to keep this updated as we go.")
    

    # Assuming you have the file ID of the markdown file on Google Drive
# Fetch the file and display its content





    feedback, battingPhilosophy, battingJustification, fieldingPhilosophy, fieldingJustification, baserunningPhilosophy, numberofplayers = st.tabs([ "Personalized Feedback", "Batting Order Philosophy", "Batting Order Justification", "Fielding Philosophy", 
                                                                                                                                   "Fielding Justification", "Baserunning Philosophy", "Number of Players"])
    
    with feedback:
        placeholder = st.empty()
        with placeholder.form(key="login"):
            user = st.text_input("Email")
            st.form_submit_button("Login")
                    
        users = ['Beep', 'Tyler', 'LambertDBB', 'Grace', 'Ben', 'Forrest','Spangler',
                 'Sweet', 'Cody',  'Niko',  'Dan', 'Renzo', 'Sean', 'Shack', 'Frank',
                 'Blake', 'Todd', 'Taylor', 'Connor', 'Ryan']

        emails = [st.secrets[x]['email'] for x in users]
        fileIds = [st.secrets[x]['fileid'] for x in users]
        emails_ids = dict(zip(users, zip(emails, fileIds)))

        if user:
            for k in emails_ids:
                email_non_capitalized = emails_ids[k][0].lower()
                if user.lower() == email_non_capitalized:
                    st.markdown("### Welcome {} to your personalized Coach's Corner".format(k.capitalize()))
                    st.markdown(return_google_markdown(emails_ids[k][1]))

                    placeholder.empty()
    with battingPhilosophy:
        path = 'assets/docs/Batting Order Philosophy.md'
        st.markdown(return_markdown(path))
    with battingJustification:
        path = 'assets/docs/Batting Order Justification.md'
        st.markdown(return_markdown(path))
    with fieldingPhilosophy:
        path = 'assets/docs/Fielding Philosophy.md'
        st.markdown(return_markdown(path))

    with fieldingJustification:
        path = 'assets/docs/Fielding Justification.md'
        st.markdown(return_markdown(path))
    
    with baserunningPhilosophy:
        path = 'assets/docs/Baserunning Philosophy.md'
        st.markdown(return_markdown(path))

    with numberofplayers:
        path = 'assets/docs/Number of players.md'
        st.markdown(return_markdown(path))    


    #streamlit_analytics.stop_tracking(firestore_key_file="temp_json.json", firestore_collection_name="coach")
    #delete_file_store()
if __name__ == "__main__":
    coaching()
