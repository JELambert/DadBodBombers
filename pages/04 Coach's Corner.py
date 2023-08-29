import streamlit as st
from utils import *

def return_markdown(filepath):
    with open(filepath, 'r') as file:
        content = file.read()
    # Split the content on 'SKIPABOVE' and get everything below it
    _, content_to_display = content.split('SKIPABOVE', 1)
    # Display it in Streamlit
    return content_to_display

def coaching():
    st.markdown("# Coach's Corner")
    with st.sidebar: get_sideBar("Coach's Corner")

    st.markdown("* This will serve as our wiki for coaching philsophy, decisions, and feedback.")
    st.markdown("* Caveat: If you have strong thoughts and opinions let them be heard and we will figure it out. This is just a starting point, but I think it's important to be transparent. I will try to keep this updated as we go.")
    
    battingPhilosophy, battingJustification, fieldingPhilosophy, fieldingJustification, tab5 = st.tabs(["Batting Order Philosophy", "Batting Order Justification", "Fielding Philosophy", "Fielding Justification", "Personalized Feedback"])

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
    
    with tab5:
        placeholder = st.empty()
    
        with placeholder.form(key="login"):
            user = st.text_input("Username")
            password = st.text_input("Password")
            st.form_submit_button("Login")
                    
        users = ['Beep', 'Tyler', 'LambertDBB', 'Grace', 'Ben', 'Forrest','Spangler',
                 'Sweet', 'Cody',  'Niko',  'Dan', 'Renzo', 'Sean', 'Shack', 'Frank']

        usernames = [st.secrets[x]['username'] for x in users]
        passwords = [st.secrets[x]['password'] for x in users]
        users_usernames_andPasswords = dict(zip(users, zip(usernames, passwords)))

        if user and password:
            for k in users_usernames_andPasswords:
                if user == users_usernames_andPasswords[k][0] and password == users_usernames_andPasswords[k][1]:
                    st.markdown("### Welcome {} to your personalized Coach's Corner".format(k.capitalize()))

                    path = 'assets/docs/dontlookhere/{}.md'.format(k.capitalize())
                    st.markdown(return_markdown(path))

                    placeholder.empty()

if __name__ == "__main__":
    coaching()
