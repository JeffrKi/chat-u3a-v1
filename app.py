import os
from embedchain import App
import streamlit as st
os.environ["OPENAI_API_KEY"] = "sk-jXSkm_rAxM0X2CaOIKr47JK3riv3Eb5NS6yT-QQXgOT3BlbkFJwgizcB7985D5XcArCBB8n_w5BPZqWorwlkgC9z9gMA"

st.title("💬 Chatbot")
st.caption("🚀 An Embedchain app")
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": """
        Hi, I can answer questions about the South West Herts u3a\n
        Ask me anything!
        """,
        }
    ]
app = App.from_config(config_path="config.yaml")
def load_db():       
    docs_to_add = [


    ]
    docs_added = [
        "https://www.swhertsu3a.org.uk/components/com_u3a/Documents/Licence_Conditions.pdf",
        "https://www.swhertsu3a.org.uk/components/com_u3a/Documents/Complaints_Procedure.pdf",
        "https://www.swhertsu3a.org.uk/components/com_u3a/Documents/Equalities_&amp;_Diversity_Policy.pdf",
        "https://www.swhertsu3a.org.uk/components/com_u3a/Documents/Stanborough_Centre_SWHu3a_Meeting_Arrangements.pdf",
        "https://www.swhertsu3a.org.uk/components/com_u3a/Documents/Signed_Annual_Report_and_Accounts_for_period_2023-2024.pdf",
        "https://www.swhertsu3a.org.uk/components/com_u3a/Documents/Member_Disciplinary_Procedure.docx",
        "https://www.swhertsu3a.org.uk/components/com_u3a/Documents/Grievance_Procedure.docx",
        "https://www.swhertsu3a.org.uk/components/com_u3a/Documents/General_Data_Protection_Regulation.pdf",
        "https://www.swhertsu3a.org.uk/components/com_u3a/Documents/Business_Secretary_PDF.pdf",
        "https://www.swhertsu3a.org.uk/components/com_u3a/Documents/Archivist.pdf",
        "https://www.swhertsu3a.org.uk/components/com_u3a/Documents/Chairman.pdf",
        "https://www.swhertsu3a.org.uk/components/com_u3a/Documents/Fire_Officer.pdf",
        "https://www.swhertsu3a.org.uk/components/com_u3a/Documents/Speaker_Secretary.pdf",
        "https://www.swhertsu3a.org.uk/components/com_u3a/Documents/Membership_Secretary.pdf",
        "https://www.swhertsu3a.org.uk/components/com_u3a/Documents/Social_Secretary.pdf",
        "https://www.swhertsu3a.org.uk/components/com_u3a/Documents/Vice-Chairperson_PDF.pdf",
        "https://www.swhertsu3a.org.uk/components/com_u3a/Documents/Film_Production_Companies_PDF_for_MPLC_Licence.pdf",
        "https://www.swhertsu3a.org.uk/components/com_u3a/Documents/Venues.docx",
        "https://www.swhertsu3a.org.uk/components/com_u3a/Documents/Risk_Assessment.docx",
        "https://www.swhertsu3a.org.uk/components/com_u3a/Documents/SWHerts_u3a_Constitution_dated_June_2024.pdf",
        "https://www.swhertsu3a.org.uk/components/com_u3a/Documents/Computer_&amp;_Audio-Visual_Loan_Equipment.pdf",
        "https://www.swhertsu3a.org.uk/components/com_u3a/Documents/TAT_FAQs_on_Insurance.pdf",
        "https://www.swhertsu3a.org.uk/components/com_u3a/Documents/Insurance_Cover_Note_2024.pdf",
        "https://www.swhertsu3a.org.uk/components/com_u3a/Documents/Managing_study_group_web_and_newsletter_display.pdf",

    ]

    for doc in docs_to_add:
        app.add(doc)   

#load_db()
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything!"):


    if prompt.startswith("/add"):
        with st.chat_message("user"):
            st.markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})
        prompt = prompt.replace("/add", "").strip()
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            message_placeholder.markdown("Adding to knowledge base...")
            app.add(prompt)
            message_placeholder.markdown(f"Added {prompt} to knowledge base!")
            st.session_state.messages.append({"role": "assistant", "content": f"Added {prompt} to knowledge base!"})
            st.stop()

    with st.chat_message("user"):
        st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        msg_placeholder = st.empty()
        msg_placeholder.markdown("Thinking...")
        full_response = ""

        for response in app.chat(prompt):
            msg_placeholder.empty()
            full_response += response

        msg_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

